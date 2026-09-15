# Validation — Dehaene extension

Validated in staging on 2026-09-15 before integration into the existing checkout.

| Check | Actual result |
|---|---|
| Metatool `tools/validate_library.py <stage> --layout published-repo --json` | **Not a generic clean pass:** five existing directory-layout errors, identical to the baseline; no new errors or warnings. |
| Existing-architecture audit | **Pass under the user-authorized existing-architecture override.** All 103 baseline tracked entries other than the intentionally changed SKILL.md and README.md are preserved. See the hash/symlink manifest. |
| New source count and budgets | 18 full sources; four new references approximately 5,236 / 5,497 / 5,560 / 5,585 tokens, each below its computed budget and 14,000 cap. Core body approximately 4,301 tokens. These are script estimates. |
| Skill-creator frontmatter check | `Skill is valid!` under the installed Anaconda Python. Initial system Python lacked PyYAML; no package or source change was needed. |
| Separate strict scans of SKILL.md and references/ | Core: no findings. References: 18 LOW external-link notices, zero HIGH findings. URLs are source/teaching citations, not source-supplied execution instructions. |
| Existing `scripts/check_references.py` | Zero local-link/provenance errors; 34 historical correction records checked. Lexical prose flags remain advisory; they do not imply automatic replacement or evidence verification. |
| Existing numerical demonstrations | 19 unittest cases passed in 51.020 seconds; actual log retained. Font-cache warnings did not affect the result. No demo implementation or tests were changed. |
| Behavioral probes | See the separate report: one three-arm development case, four initial full-condition final cases, two prior-capability regressions, and one new repair follow-up. Original mirror-assessment failure retained. |
| Reading ledger | Audit script completed; no unresolved recorded verification questions or per-source 4× budget alerts. Three overlapping reads needed retrospective purpose annotations, clearly labeled. Whole-book coverage is not claimed. |

## Existing layout exceptions

The generic validator rejects `demos/`, `maintenance/`, ignored local `outputs/`, `scripts/`, and `tests/`. All five were already present before this extension. Existing warnings concern the demo requirements file, computational-demonstrations reference, two older source planning budgets, and a missing older section count. Existing sources stay below the absolute 14,000-token cap. The user's instruction to preserve an existing destination's architecture applies; the metatool was not modified to manufacture a clean result.

`structural-baseline.json`, `structural-final.json`, `existing-architecture-check.json`, scan reports, `reference-check.json`, and the numerical test log preserve the actual outputs. Machine-local staging prefixes were normalized in JSON reports. Root runtime hashes record the delivered candidate. Remote commit/tree and final discovery-link verification are performed after publication; a committed report cannot truthfully contain its own future commit hash.
