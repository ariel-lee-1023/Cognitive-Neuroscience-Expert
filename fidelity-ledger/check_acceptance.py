#!/usr/bin/env python3
"""Validate acceptance evidence completeness and detect stale runtime inputs.

This checks records, hashes and explicit reviewer assessments, not answer truth.
Run after fresh model executions and substantive review, not instead of them.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return 'sha256:' + hashlib.sha256(path.read_bytes()).hexdigest()


def runtime_hash(root=ROOT):
    paths = [root/'SKILL.md', *sorted((root/'references').glob('*.md'))]
    entries = {p.relative_to(root).as_posix(): sha(p) for p in paths}
    return 'sha256:' + hashlib.sha256(json.dumps(entries, sort_keys=True).encode()).hexdigest()


def check(root=ROOT):
    ledger = root/'fidelity-ledger'
    result = json.loads((ledger/'acceptance-results.json').read_text())
    tasks = json.loads((ledger/'acceptance-suite.json').read_text())['tasks']
    tasks += json.loads((ledger/'acceptance-regressions.json').read_text())['tasks']
    expected = {task['id']: task for task in tasks}
    errors = []
    if result.get('status') != 'completed': errors.append('acceptance execution not completed')
    for name, key in [('acceptance-suite.json', 'suite_hash'), ('acceptance-regressions.json', 'regression_suite_hash')]:
        if result.get(key) != sha(ledger/name): errors.append(f'stale {name}')
    if result.get('runtime_content_hash') != runtime_hash(root): errors.append('stale runtime content')
    if not result.get('model') or not result.get('settings'): errors.append('model/settings absent')
    runs = result.get('runs', {}).get('core_references', [])
    ids = [run.get('id') for run in runs]
    if len(ids) != len(set(ids)) or set(ids) != set(expected): errors.append('missing, extra, or duplicate runs')
    context_ids = [run.get('fresh_context_id') for run in runs]
    if None in context_ids or len(context_ids) != len(set(context_ids)): errors.append('case contexts are missing or reused')
    for run in runs:
        case = expected.get(run.get('id'))
        if case is None: continue
        directory = root/run['artifact_directory']
        for name, key in [('answer.md','answer_hash'), ('run.json','execution_record_hash'), ('input-manifest.json','input_manifest_hash')]:
            path = directory/name
            if not path.is_file() or sha(path) != run.get(key): errors.append(f"{case['id']}: stale/missing {name}")
        if not (directory/'input-manifest.json').exists(): continue
        manifest = json.loads((directory/'input-manifest.json').read_text())
        if manifest.get('prompt') != case['prompt']: errors.append(f"{case['id']}: prompt mismatch")
        for relative, digest in manifest.get('source_hashes', {}).items():
            path = root/relative
            if not path.exists() or sha(path) != digest: errors.append(f"{case['id']}: stale source {relative}")
        assessments = run.get('assessments', {})
        if set(assessments) != set(case['criteria']): errors.append(f"{case['id']}: incomplete rubric")
        for key, entry in assessments.items():
            if entry.get('status') not in ('pass', 'limited', 'fail') or not entry.get('rationale'):
                errors.append(f"{case['id']}/{key}: missing status/rationale")
        if not run.get('usefulness_review'): errors.append(f"{case['id']}: missing usefulness review")
        if run.get('accepted') != all(entry.get('status') == 'pass' for entry in assessments.values()):
            errors.append(f"{case['id']}: acceptance inconsistent with reviewer statuses")
    return errors, len(runs)


if __name__ == '__main__':
    failures, count = check()
    print(f'{len(failures)} acceptance-record errors; {count} fresh-context cases recorded')
    for failure in failures: print(failure)
    raise SystemExit(bool(failures))
