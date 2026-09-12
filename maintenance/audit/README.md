# Reference maintenance audit

This directory is for maintainers, not routine domain loading. The canonical expert remains the root SKILL.md, and the ten source-reference paths are unchanged.

[corrections.json](corrections.json) records each consequential changed passage, its base commit and original line, original wording, source locator, verification status, replacement, reason, external evidence, and attribution. Original quoted text is retained as an audit record, not endorsed advice. Line numbers refer to the recorded base; replacements are checked against the current file. Source locators without verified page numbers are explicitly marked.

## Correction process

1. Start with claims that impose methodological requirements, assert causation, imply clinical use, give numerical cutoffs, or universalize a model. Read the nearby mechanism, worked example, decision rule, and takeaway.
2. Inspect the original source where accessible. Record whether a problem is an extraction error, a source-specific position, or an editorial correction. Do not label an extraction error without checking the original.
3. Attach assumptions and scope directly to each corrected passage. If using later or external evidence, name it separately rather than crediting it to the book.
4. Record unresolved attribution or verification questions. A located source or HTTP success is not verification of its content.
5. Run `python scripts/check_references.py --report outputs/reference-check.json`, review the categorical-language flags manually, and run behavioral cases in both full-reference and excerpt contexts. Keyword checks supplement substantive review.
6. After model or demonstration changes, run the numerical checks and inspect figures. Keep generated outputs, raw books, recovered full text, and local machine paths out of version control.

## Verification status and remaining questions

- **Jahn timing:** Appendix D was inspected. Its introduction uses categorical jitter wording; its efficiency section also conditions comparisons on design scaling and the contrast. The revised general guidance is an editorial synthesis supported by Smith et al. (2007), whose abstract explicitly distinguishes mathematical estimability from practical sensitivity. This is not merely a proven extraction error. The historical Flanker example timing was retained as source-attributed example settings, not independently remeasured.
- **Forstmann & Turner:** The exact 2024 process-tracing passage and page were not accessible. It remains unresolved whether the original conflation originated in extraction or the chapter. Primary eye-tracking/EEG and fMRI studies support separating modalities. No claim about current equipment availability remains.
- **Seriès clinical framing:** Exact chapter text was unavailable. NIMH's official RDoC description explicitly separates the research framework from diagnostic guidance. Added validation requirements are editorial methodological criteria, not results established by the book.
- **Seriès MAP and Bayes factors:** The original threshold attribution, page, and numeric scale remain unverified. The correction distinguishes BF, log BF, and twice log BF without selecting an unsupported cutoff. Kass & Raftery's original paper was located; its table was not reliably extracted in this session, so no new numeric evidence scale is asserted. Wilson & Collins's primary modelling paper and accompanying recovery material support checking the actual model/task and prior sensitivity. MAP does not remedy a structurally flat likelihood.
- **O'Reilly control:** The authors' Stroop simulation documentation was located and its indexed task description supports top-down biasing. The exact fourth-edition chapter text and historical revision were not fully verified. The revised statements are limited to the described training, task, and competition architecture. Claims about the prevalence of directed inhibition were removed.
- **Bonferroni:** The union-bound derivation was checked against NIST and the existing Nipraxis reference. The mathematical independence correction is established; the original Jahn Appendix A phrasing was not rechecked, so this is not labelled a proven extraction error.

## Screening across the ten references

This is a prioritized screening pass, not a claim to have revalidated ten books. The checker scans every source reference and reports categorical or consequential language for review without automatically rewriting it. Many hits are appropriate restrictions; the count is not an error count.

| Reference | Highest-priority scope reviewed | Disposition / next verification |
|---|---|---|
| Jahn | Jitter, overlap, motion confounding, multiplicity | Timing and Bonferroni repaired throughout the targeted passages; convolution now states its weighted-integral definition and scaling assumptions. Revisit the five-criterion selectivity checklist and the simplified BOLD chain against their original sections. |
| Forstmann & Turner | Eye recording, modality artifacts, model-to-mechanism inference | Ocular passages repaired. Revisit categorical two-stage-correlation bias and the apparent hierarchy of linking strategies; sophisticated linkage alone does not establish validity. |
| Seriès | RDoC, MAP, thresholds, clinical and Gaussian-model scope | Targeted passages repaired. Verify chapter-level attributions and disorder-specific causal/mechanistic summaries before clinical reuse. |
| O'Reilly | Excitatory control claims, standalone takeaways | Stroop/A-not-B scope repaired. Revisit broad STDP and dopamine statements, anatomical cerebellar connectivity limits, and architecture-specific numerical defaults. |
| Brett / Nipraxis | GLM, convolution, multiplicity assumptions | Existing Bonferroni versus Sidak distinction is already explicit and was retained. Geometry and registration procedures were not revalidated. |
| Byrne | Lesion inference, biological and diagnostic requirements | Flag current versus historical AD diagnostic wording and universal protein-synthesis claims for source and current-evidence review. No clinical updating inferred from the old text. |
| Lim | Method restrictions, numerical resolution, current availability | Flag the statement that optogenetics and chemogenetics are currently exclusively non-human, fixed resolution limits, and perfusion percentage. Check source date, preparation, and current primary evidence before reuse. |
| Stocco | Equations, measurement interpretation | Advantage sign, actor/critic update distinctions, biological analogy scope, and exponential/log-log plotting guidance corrected in the acceptance follow-up. Standard RL definitions and analytical checks support the changes; exact original Stocco wording remains unverified. |
| Fornito | Graph construction, directionality, signed edges, null models | Preserve dependence on construction and null model. Revisit treating all normalized metrics as ratios, particularly modularity, and interpreting correlation signs as functional antagonism. |
| Kappenman & Luck | Component overlap, inverse problem, timing | Existing inverse-problem qualification retained. Revisit universal ICA alignment claims and absolute fMRI exclusion wording; the measurement question determines appropriate temporal inference. |

The unresolved items are a review queue, not evidence that the whole library is scientifically validated. For a task touching one, consult its original source and relevant primary evidence before adopting the stronger claim.
