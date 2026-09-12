#!/usr/bin/env python3
"""Check local links, provenance, and known regressions; flag prose for review.

No language is replaced automatically. --external probes HTTP links separately;
network errors are reported as unverified rather than proof of broken content.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
KNOWN = [r'A\(s,\s*a\)\s*=\s*V\(s\)\s*-\s*Q\(s,\s*a\)',
         r'exponential is straight only with the \*x\*-axis logged', r'jitter is not decoration', r'HRFs are confounded by construction',
         r'eye tracking contaminates EEG/fMRI', r'electrical artifacts in EEG and fMRI',
         r'MRI-compatible eye trackers are hard to obtain', r'switch to MAP',
         r'>\s*5\s+conclusive', r'conclusive if greater than 5',
         r'Cognitive control is excitatory biasing of the weak pathway',
         r'Directed inhibition is rare', r'Bonferroni.{0,70}assumes each test is independent']
CATEGORICAL = re.compile(r'\b(must|always|never|only|requires?|guarantees?|impossible|conclusive|causal(?:ly)?|diagnos\w*)\b', re.I)
FIELDS = {'id','group','location','original_line','base_commit','original','source_locator',
          'verification_status','revised','reason','evidence','attribution','reviewed_on'}


def local_links(path):
    text = path.read_text()
    links = re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text)
    links += re.findall(r'!\[[^\]\n]*\]\(([^\s)]+)\)', text)
    for wiki in re.findall(r'\[\[([^\]]+)\]\]', text):
        links.append(wiki.split('|')[0] + '.md')
    return links


def check(root=ROOT):
    errors, flags, external = [], [], set()
    files = [root/'SKILL.md', root/'README.md', *sorted((root/'references').glob('*.md')),
             *sorted((root/'maintenance').rglob('*.md'))]
    for path in files:
        if not path.exists():
            errors.append(f'missing {path.relative_to(root)}'); continue
        text = path.read_text()
        for link in local_links(path):
            target = urlsplit(link)
            if target.scheme in ('http','https'):
                external.add(link); continue
            if target.scheme or not target.path:
                continue
            resolved = (path.parent / unquote(target.path)).resolve()
            if not resolved.exists(): errors.append(f'{path.relative_to(root)}: missing link {link}')
            elif target.fragment and resolved.suffix == '.md':
                headings = re.findall(r'^#+\s+(.+)', resolved.read_text(), re.M)
                anchors = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
                if unquote(target.fragment) not in anchors:
                    errors.append(f'{path.relative_to(root)}: missing anchor {link}')
        if path.parent.name == 'references':
            for pattern in KNOWN:
                if re.search(pattern, text, re.I): errors.append(f'{path.name}: known regression {pattern}')
            for number, line in enumerate(text.splitlines(), 1):
                matches = sorted(set(m.group().lower() for m in CATEGORICAL.finditer(line)))
                if matches:
                    flags.append(dict(file=str(path.relative_to(root)), line=number, terms=matches, text=line))
    records = json.loads((root/'maintenance/audit/corrections.json').read_text())
    seen = set()
    for item in records:
        missing = FIELDS - item.keys()
        if missing: errors.append(f"audit {item.get('id')}: missing {sorted(missing)}"); continue
        if item['id'] in seen: errors.append(f"duplicate audit id {item['id']}")
        seen.add(item['id'])
        for key in FIELDS:
            if not item[key]: errors.append(f"audit {item['id']}: empty {key}")
        target = root / item['location']
        if not target.exists() or item['revised'] not in target.read_text():
            errors.append(f"audit {item['id']}: revised passage no longer matches; re-review provenance")
        for url in item['evidence']:
            if urlsplit(url).scheme not in ('https','http'): errors.append(f"invalid evidence URL {url}")
            external.add(url)
    master = (root/'SKILL.md').read_text()
    if len(list(root.glob('SKILL.md'))) != 1 or '\nname: cognitive-neuroscience\n' not in master:
        errors.append('canonical name/entrypoint changed')
    return dict(errors=errors, corrections=len(records), review_flags=flags,
                external_urls=sorted(external),
                reference_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root/'references').glob('reference-*.md'))})


def probe(url):
    try:
        with urlopen(Request(url, headers={'User-Agent':'reference-maintenance-check/1.0'}), timeout=12) as response:
            return dict(url=url, status=response.status, resolved_url=response.url)
    except Exception as error:
        return dict(url=url, status='unverified', reason=str(error))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--external', action='store_true')
    args = parser.parse_args()
    report = check()
    if args.external:
        with ThreadPoolExecutor(max_workers=6) as pool:
            report['external_checks'] = list(pool.map(probe, report['external_urls']))
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
    print(f"{len(report['errors'])} errors; {report['corrections']} audited corrections; {len(report['review_flags'])} prose flags for human review")
    for error in report['errors']: print(error)
    if not args.external: print('External reachability not tested; use --external when network access is available.')
    raise SystemExit(bool(report['errors']))


if __name__ == '__main__': main()
