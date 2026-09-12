# Executed validation — 2026-09-12

## Historical integration checks (before the acceptance follow-up)

Validation was performed in `/Users/AI products/Git-deliverables/Cognitive-Neuroscience-Expert` before file-level integration into the existing checkout. The baseline was the saved local working version, including its uncommitted reference corrections, demonstration guide, programs, and maintenance records.

| Check | Actual result | Interpretation |
|---|---|---|
| `tools/validate_library.py <staging> --layout published-repo --json` | 14 references; core body 3,529 tokens against 4,000 planning budget and 4,500 hard cap; **four layout errors** | Every error concerns a pre-existing `demos/`, `maintenance/`, `scripts/`, or `tests/` directory. The generic output contract does not represent this existing architecture. The raw report is retained, not called a clean pass. |
| Existing-architecture audit | Passed; 36 baseline files preserved byte-for-byte; no unexpected structural errors | The user's explicit saved-local architecture instruction overrides the generic directory restriction. Existing references were not rewritten. |
| Four new references | Approximately 4,767 / 6,085 / 6,745 / 6,409 tokens; all below computed budgets and caps | The generic heuristic classifies inline-equation references as text; they pass even those stricter budgets. Provenance separately records their technical source types. |
| Repository reference checker | 0 errors; 29 prior correction records still match; 330 categorical-language review flags | Flags are screening cues, not established errors. New causal and measurement rules were reviewed with their adjacent conditions. |
| Separate core and references injection scans, strict mode | Core: no findings. References: seven LOW external-link findings in existing files; no HIGH findings | Existing source links were retained. No finding came from a new book reference. A clean high-risk scan is not proof against all injection. |
| Existing demonstration tests | 19 passed using `/opt/anaconda3/bin/python`, NumPy 1.26.4, Matplotlib 3.9.2 | Confirms existing numerical examples still execute in the integrated version; no new demo behavior was introduced. |
| Reconstructed formula sanity checks | Five checks passed: Poisson/Fisher identity, standardization/IPW identity, recurrent fixed point/time constant, Oja norm derivative, blocking limit | Synthetic/algebraic checks, not replications of book datasets or scientific validation. |
| Reading audit | Four source records, source-local spans and expenditure recorded; Craver alerts above provisional 4× budget | Totals conservatively count submitted cleaned slices, some of which were display-truncated; exact visible/provider usage is unavailable. |
| Independent behavioral acceptance | **Unrun** | No fresh-context endpoint/model comparison was configured. No baseline gain, reference gain, or controlled behavioral non-regression is claimed. |

The first two test attempts used Python environments without NumPy and failed during import. The final run used the already installed numerical environment and passed all 19 tests. Font-cache warnings did not prevent execution. No packages or demonstration files were changed to make the tests pass.

## Existing warnings and scope limits

The generic validator also warns about the pre-existing optional guide and requirements file, two existing reference planning-budget overruns (Byrne and O'Reilly), and the absent section-count field in Stocco. These are preserved baseline conditions; none is a new reference hard-cap violation. The source files were not exhaustively reread, all external links were not revalidated, and later editions/current clinical or hardware claims remain outside verified scope.

## Publication scope

The initial commit published the four-book additions separately. The user subsequently explicitly requested publication of **all saved local changes**, including the existing demonstrations, reference corrections, core and README revisions, and maintenance records. The complete non-ignored working tree is therefore included in the follow-up publication. The saved-local integration checks above apply to that complete runtime. Generated `outputs/`, virtual environments, and caches remain governed by the repository's existing ignore rules.

The publication-projection report records the narrower initial commit only; it is historical evidence, not a clean generic-layout result for the complete repository. The complete publication retains the existing architecture and its documented validator exceptions.

See the raw JSON and test logs in this directory. The final checkout and publication projection checks are recorded in `delivery-checks.json`; remote commit/tree identity is verified after pushing.

## Final location check

Final reference check: 0 errors. All 36 retained baseline files and all new runtime files match the validated staging content. The generic final-location validator additionally flags the pre-existing ignored `outputs/` directory (five architecture diagnostics total); no generated output was moved or committed. The initial scoped publication projection passed with **zero errors** and three unchanged baseline warnings; the full saved-local publication uses the existing-architecture audit above.

## Acceptance follow-up on the corrected runtime

The [current-version report](acceptance-report.md) supersedes the historical behavioral `unrun` status above for the core-plus-reference arm: 10 original cases and two mathematical regressions were executed in fresh contexts and passed substantive review. Comparative baseline and core-only arms remain unrun. Exact settings, inputs, answers and criterion-level assessments are retained in [acceptance-results.json](acceptance-results.json).

The Stocco runtime now uses `A = Q - V`, separates policy/preference updates from advantage estimation, and places exponential decay on semilog-y axes. Adjacent biological mapping is explicitly an analogy. Five new correction records bring the audit to 34, with original-source attribution limits preserved. Installation documentation now targets Python 3.10–3.12. No dependency upgrade or clean-install matrix is claimed.

All 19 existing tests and seven algebraic checks passed in the existing Python 3.12.7 environment. The reference checker returned zero errors and 329 review flags, which remain screening cues. The acceptance checker verifies 12 complete records and current source hashes. The generic structure validator reports the same five existing architecture errors and five warnings before and after these changes; it is not a clean generic-layout pass. The strict core scan has zero findings; the reference scan has eight LOW external-link findings and no HIGH findings, including the added primary policy-gradient documentation link. Detailed execution evidence is in [acceptance-validation.json](acceptance-validation.json).
