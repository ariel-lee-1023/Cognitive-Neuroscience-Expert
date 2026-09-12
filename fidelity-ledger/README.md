# Four-book fold-in — 2026-09-12

This ledger documents the addition of Craver, Dayan–Abbott, Hernán–Robins, and Luck to the existing cognitive neuroscience skill. Runtime content remains in root `SKILL.md` and one file per book in `references/`; the discovery alias is `.agents/skills/cognitive-neuroscience -> ../..`. No raw book files are published.

The saved local working version, including demonstrations and prior prose corrections, was the integration baseline. Existing references and `maintenance/` records were preserved. This ledger does not replace or retroactively validate those earlier records.

- [Source provenance](source-provenance.json): source file hashes, versions, chapter counts, and limits.
- [Coverage audit](coverage-audit.md): retained structure, compressed material, sampled exceptions, and editorial corrections.
- [Reading ledger](reading-ledger.json) and [reading report](reading-report.json): targeted source slices and expenditure accounting, with the visibility limitation stated in the ledger.
- [Acceptance report](acceptance-report.md), [frozen suite](acceptance-suite.json), [mathematical regressions](acceptance-regressions.json), and [results](acceptance-results.json): 10 prepared cases and two regressions executed in fresh contexts, all passing criterion-level review. Baseline/core-only comparisons remain unrun; the [previous status](acceptance-results-before-followup.json) is preserved.
- [Acceptance evidence checker](check_acceptance.py): checks answer/input hashes, runtime freshness and review completeness; does not grade scientific correctness.
- [Validation](validation.md): actual structural, link, scanner, and regression checks; these do not prove reasoning quality.

## Edition limits

Luck's supplied book is the first edition (2005), despite the requested table naming the second edition. The reference explicitly labels that mismatch. Dayan–Abbott is a December 2000 chapter draft. Hernán–Robins is dated February 21, 2020. Craver is the 2007 book. Historical examples and equipment discussion are not claims about present consensus or current protocols.

## Extending the collection

Keep a single canonical reference for each supplied source. State the actual version, preserve author-specific distinctions, define reconstructed mathematical notation, and carry conditions with the methods they qualify. Add task-based links to the core and change its judgments only where the material warrants it. Put new provenance and evaluation records in `fidelity-ledger/`, outside runtime references. Preserve earlier acceptance evidence; source and structural audits do not substitute for fresh-context behavioral comparisons.
