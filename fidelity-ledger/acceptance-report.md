# Current-version acceptance, 2026-09-12

All 10 prepared cases and both added mathematical regression cases passed criterion-level review of actual fresh-context answers. This is bounded acceptance evidence for the corrected runtime based on commit `1867409`, not a measured improvement over a baseline or a general reliability estimate.

## Protocol and reproducibility

The original [version-2 suite](acceptance-suite.json) was preserved byte-for-byte, including its development/final partitions. The two [regression cases](acceptance-regressions.json) were defined after the mathematical errors were identified and are not held-out evidence. The previous `unrun` record is [archived](acceptance-results-before-followup.json).

Each selected answer came from a newly spawned evaluator with `fork_turns=none`, one case per context, using **gpt-6-astra, reasoning effort high**, inherited without overrides from the parent session metadata. Temperature, seed and output-token settings were not exposed. Local file reads, writes and optional calculations were allowed. Evaluators received the expert core, their exact case prompt and source fixtures; they did not receive the rubric, parent conversation, previous answers or correction audit. Internet use and cross-case access were excluded for these bounded source-fidelity tests.

Most fixtures contained preselected relevant references. The current-work boundary case used the core alone, as permitted by its case specification. The mechanism-fit fixture was repaired after its first evaluator requested a Stocco file omitted from the curated inputs: the replacement was a new context with the full current reference directory. The [initial answer](acceptance-runs/excluded-mechanism-fixture/answer.md) and exclusion reason are retained. Thus 13 contexts ran and 12 were selected; the repair did not edit an answer into a pass.

The maintaining agent read each actual answer after completion and assessed every frozen criterion, usefulness, and attribution. The reviewer was not blinded. [Machine-readable results](acceptance-results.json) contain individual rationales, source and artifact hashes, context identifiers, settings and limitations. Each case directory retains the answer, execution record and input manifest. Only local fixture paths and Markdown link targets were normalized for publication; answer substance was not rewritten.

## Reviewed outcomes

| Case | Result | Observed behavior |
|---|---|---|
| [mechanism-fit](acceptance-runs/mechanism-fit/answer.md) | Pass | Separates predictive fit, possible mechanism and established mechanism; proposes discriminating evidence without treating added detail as proof. |
| [poisson-decoding](acceptance-runs/poisson-decoding/answer.md) | Pass | Derives the count likelihood with its total-rate term and specifies conditional independence and readout limits. |
| [feedback-treatment](acceptance-runs/feedback-treatment/answer.md) | Pass | Identifies treatment-confounder feedback and states g-method identification assumptions. |
| [erp-measurement](acceptance-runs/erp-measurement/answer.md) | Pass | Distinguishes measurement choices from component interpretations and addresses noise, jitter and overlap. |
| [edition-boundary](acceptance-runs/edition-boundary/answer.md) | Pass | Preserves the supplied edition boundary and does not invent later-edition additions. |
| [lesion-necessity](acceptance-runs/lesion-necessity/answer.md) | Pass | Qualifies necessity by perturbation specificity, system organization and task conditions. |
| [information-count](acceptance-runs/information-count/answer.md) | Pass | Distinguishes count information from full spike-train information and observed behavior. |
| [selected-eeg](acceptance-runs/selected-eeg/answer.md) | Pass | Explains selection after randomization and the assumptions needed to recover a target effect. |
| [erp-latency-final](acceptance-runs/erp-latency-final/answer.md) | Pass | Addresses filter-induced timing shifts, latency measurement and prespecification. |
| [newest-trial](acceptance-runs/newest-trial/answer.md) | Pass | Reports the current-evidence gap instead of fabricating a protocol or replicated effect size. |
| [advantage-sign](acceptance-runs/advantage-sign/answer.md) | Pass | Computes `A = Q - V = +2`; separates actor/critic updates and conditions the TD identity. |
| [exponential-axis](acceptance-runs/exponential-axis/answer.md) | Pass | Derives semilog-y versus log-log axes and explains why visual straightness cannot select a scientific model. |

## Limits and future reruns

One answer per case, a single model configuration, curated source fixtures and an unblinded reviewer limit generalization. This run does not test complete reference routing, all original-book claims, clean installation, clinical validity, or all possible user questions. The baseline and core-only comparative arms remain unrun; no baseline gain, reference gain or pre/post improvement is claimed.

For a repeat, start a fresh context per prompt, supply the current core and declared source fixture, record the actually exposed model/settings and files read, and retain the actual answer before applying the rubric. Keep earlier runs rather than overwriting their evidence. A changed runtime requires a new behavioral execution; changing hashes alone cannot refresh its acceptance.

To verify the retained evidence and algebra locally:

```bash
python fidelity-ledger/check_acceptance.py
python fidelity-ledger/equation_checks.py
python -m unittest discover -s tests -v
python scripts/check_references.py
```

The evidence checker validates hashes and completeness, not scientific truth. The [follow-up validation record](acceptance-validation.json) records numerical, metadata and structural checks and their limits.
