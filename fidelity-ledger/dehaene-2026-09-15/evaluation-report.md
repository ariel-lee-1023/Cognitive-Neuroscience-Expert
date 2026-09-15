# Behavioral evaluation

## What actually ran

The original eight-case suite was frozen before semantic extraction. Three development cases (P3, recycling/model disagreement, and current-AI claims) were not run. One development lesson case ran in three fresh agents: plain-role baseline, core only, and core plus relevant references. All three satisfied the two manual criteria. The reference arm gave more explicit source and cross-script qualifications, but this binary tie does **not** demonstrate a measured improvement.

Four final cases ran with the full skill: numerical decomposition, mirror reversals, GNW disagreement, and an unsupported infant effect size. Three passed both criteria. The mirror answer met the diagnostic-boundary criterion but omitted the required recommendation for professional assessment. That original answer and failure are preserved.

After inspecting the failure, a different persistent-reading-difficulty case and its two criteria were frozen before adding a general assessment/support boundary to the reading reference. A fresh agent then passed that follow-up. The original mirror case was not rerun or relabeled as passing; it is now development material for future revisions. This follow-up is a limited check of the repair, not a replacement claim that the original final suite passed unchanged.

Two earlier-capability regressions also ran: Poisson decoding and ERP measurement. Both passed their two manual criteria. The separate existing numerical demo suite passed 19 tests.

## Reproducibility and limits

`evaluation-results.json` records every criterion decision. `evaluation/` retains actual prompts, answers, self-reported file-read traces, and runtime manifests. The parent agent scored answers without blinding; no independent grading or repeated-run variance estimate was obtained. Baseline/core comparisons were run for only one development case, not the whole suite. Exact serving model ID, decoding settings and billed usage were unavailable and are not invented.

Agents were launched with `fork_turns="none"` and instructed not to inspect parent outputs, ledgers or other answers. This is instruction-based context separation on a shared filesystem, not an OS-enforced sealed runner. They retained platform and project setup instructions. Two agents initially described context inheritance by assumption; trace-only follow-ups clarified that no parent substantive conversation was visible. Their answers were unchanged. The reading-support trace reports truncated combined reference output, with the relevant assessment and learning sections visible; no complete-file-reading claim is made.

Portable copies replace staging and scratch path prefixes in answers/traces/manifests. `original-artifact-hashes.json` records the unmodified local artifacts before this mechanical path conversion. Answers were not substantively edited. Earlier runtime manifests record the candidate actually available for those runs; the final root manifest records the delivered runtime after the repair. New citations and the assessment paragraph postdate some tests, so those tests are not represented as exact-byte tests of the final candidate. The two regression references themselves were unchanged.

Final packaging also repaired a routing-table blank line and restored the pre-existing combined-source guidance verbatim. Structural/link/scan checks were rerun after these changes; behavioral answers were not rerun.
