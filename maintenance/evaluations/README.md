# Conversation forward tests

Eight actual prompts were answered by two separate evaluators on 2026-09-12: one with access to the relevant full source reference, one restricted to the selected standalone excerpt. Both received the revised expert core; the numerical-representation case could also use the optional computational guide. Neither evaluator received the expected answers, correction audit, sibling arm, or parent conversation. Internet access was excluded for this bounded test, and answers explicitly acknowledge unavailable current/source verification.

The [prompts](prompts.json), actual [full-reference responses](full-reference/responses.json), and actual [excerpt responses](takeaway-only/responses.json) are retained. Each arm has a context manifest with hashes; the excerpt manifest also retains its exact inputs. Local file/runtime prefixes were normalized for portability, without editing answer substance. The numerical cases include executed code, settings/results, and curated evidence figures. These are durable evaluation artifacts, not temporary demo outputs.

These tests used the 28-correction revision. A subsequent mathematical clarification of convolution as a weighted integral rather than necessarily an average was recorded as `convolution-01`; its implementation is covered by numerical convolution tests but these conversation responses were not regenerated for that wording-only clarification.

## Assessment

The maintaining agent reviewed actual outputs for scientific correctness, scope, attribution, and usefulness. Each axis was assessed as pass, limited, or fail; this is qualitative review, not an automated keyword score or a statistical benchmark.

| Case | Full / excerpt scientific correctness | Scope and attribution | Usefulness / evidence |
|---|---|---|---|
| Fixed timing and overlap | Pass / pass | Both condition the answer on the actual design, contrast, HRF and noise. Neither certifies unseen study precision. | Both give actionable contrast-specific checks; neither demands jitter. |
| Ocular artifacts | Pass / pass | Both separate eye movement from recording and EEG voltage artifacts from fMRI effects. Full answer explicitly identifies the editorial correction. | Gaze model examples distinguish prediction from causation. |
| RDoC and diagnosis | Pass / pass | Both reject diagnostic substitution and separate recovery, reliability, validation, and usefulness. | Explain what evidence is missing rather than only refusing the premise. |
| Stroop control | Pass / pass | Both retain asymmetric training, weak color pathway, and lateral competition; neither universalizes control. | Both propose comparing rival mechanisms, labelled as synthesis. |
| Flat likelihood, MAP, BF | Pass / pass | Both explain prior-driven stability and conditional BF odds. Excerpt answer explicitly notes that BF interpretation goes beyond its supplied excerpt. | Both separate parameter identification, model comparison, and empirical adequacy. |
| Simulation and patients | Pass / pass | Both limit the simulated result to model assumptions and require a separate neural link. | Full answer gives additional drift/accuracy conditions. Excerpt's mechanism detail is limited but clearly marked as synthesis. |
| Equation and figure | Pass / pass | Both label actual calculations as illustrative and define independent-noise/equal-norm assumptions. | Both execute code and verify the variance equation against matrix calculations; figures were visually inspected. |
| Simple RPE question | Pass / pass | Full answer distinguishes immediate and TD accounts. Excerpt answer stays within Rescorla-Wagner. | Both satisfy the requested one or two sentences. Excerpt uses one small equation, without unnecessary derivation. |

## Limits and reuse

Each arm shares context across its eight cases, so isolation is between arms, not a fresh model session per prompt. This is one post-change run with no pre-change control, no repeated samples, and no independent human adjudication. It shows the recorded answers handled these prompts; it does not establish a general success rate or validate the scientific library.

The excerpt used for recovery covers MAP but not Bayes-factor conventions, and the excerpt used for simulation has only brief choice/RT guidance. Their answers appropriately mark additional reasoning as synthesis. Future regressions should test different task details and counterexamples, with fresh contexts per case when stronger isolation is needed.

To repeat the two numerical evaluation artifacts:

```bash
python maintenance/evaluations/full-reference/representation.py
python maintenance/evaluations/takeaway-only/representation.py
```

To rerun conversation tests, give a fresh evaluator the root SKILL.md and the corresponding prompt plus its full reference or exact excerpt from the manifest. Keep rubric and audit withheld until answers are recorded. Record model/runtime, context condition, actual answer, actual tool use, and reviewer rationale. Do not fabricate transcript outputs from this rubric. For fixed-input reproduction of the full-reference arm, start from the audit's base commit and apply the first 28 recorded corrections plus the core/guide revision; manifests detect drift.
