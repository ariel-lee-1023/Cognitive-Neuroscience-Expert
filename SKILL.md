---
name: cognitive-neuroscience
description: "Senior, mechanism-oriented cognitive neuroscience across 10 sources spanning mechanism (O'Reilly Computational Cognitive Neuroscience, Byrne Neuroscience Online, Lim Open Neuroscience Initiative), formal models (Forstmann & Turner Model-Based Cognitive Neuroscience, Stocco Explanatory Models, Seriès Computational Psychiatry), and methods (Jahn Andy's Brain Book, Brett Nipraxis, Fornito Brain Network Analysis, Kappenman & Luck ERP Components). Use for mechanism explanation, theoretical comparison, evidence evaluation, experimental design reasoning, methodological boundaries, and cross-level integration on perception, attention, memory, executive function, language, decision-making, and psychopathology. Each source has its own references/reference-<slug>.md, loaded on demand."
---

<!-- argument-hint: [topic, framework name, brain area, method, model, or book] -->

# Cognitive Neuroscience — Mechanisms, Models, and Methods
**Books**: 10 | **Generated**: 2026-08-07 | **Depth**: study

## How to use
- No args → read this router, pick the source(s).
- "about \<topic\>" → use the Topic Index to open the right reference file(s).
- Most good answers need **two or three** files: one for the mechanism, one for the formal model, one for the method or evidence that constrains them.

## Operating stance
1. **Name the mechanism or say you can't.** A labelled function ("attention", "executive control") is not an explanation. Flag homunculi — and remember a *function* is not a *computation* (the chess-knight test).
2. **State the level and the evidence type.** Molecular / cellular / circuit / systems / behavioral; correlational vs. causal; in vivo / ex vivo / in vitro / in silico; and for models, functional / algorithmic / implementational.
3. **Volunteer the boundary conditions.** Every method has a resolution, every model an untested assumption, every lesion an intact remainder, every graph a thresholding choice, every ERP peak a superposition.
4. **Adjudicate, don't survey.** When two accounts fit the same finding, name the manipulation on which they diverge, say which way the data point, and mark what is genuinely unsettled.

## Which book for which job  (front-loaded router)

### Mechanism & systems
| Book (→ file) | Reach for it when you need… | One big idea |
|---|---|---|
| **Computational Cognitive Neuroscience 4e** — O'Reilly, Munakata, Hazy, Frank → [oreilly-comp-cog-neuro](references/reference-oreilly-comp-cog-neuro.md) | An implemented, level-crossing account of *how* a function works, with equations and simulated lesions | One mechanism set reused across all domains; differences come from connectivity |
| **Neuroscience Online** — Byrne, Wright, Dougherty et al. → [byrne-neuroscience-online](references/reference-byrne-neuroscience-online.md) | Cellular/molecular substrate, anatomical pathway, clinical syndrome, patient dissociation | Localized enough that lesions dissociate, distributed enough that nothing works alone |
| **Open Neuroscience Initiative** — Lim → [lim-open-neuroscience](references/reference-lim-open-neuroscience.md) | To choose a method, know its resolution and cost, classify a design, or refute a neuro-myth | Control and generalizability trade off; pick the method from the claim |

### Formal models
| Book (→ file) | Reach for it when you need… | One big idea |
|---|---|---|
| **Model-Based Cognitive Neuroscience 2e** — Forstmann & Turner → [forstmann-model-based-cogneuro](references/reference-forstmann-model-based-cogneuro.md) | Decision-making (DDM, LBA), and how a cognitive model gets *linked* to neural data | The linking structure determines the claim you may make |
| **Explanatory Computational Models** — Stocco → [stocco-explanatory-models](references/reference-stocco-explanatory-models.md) | The craft of modelling: features vs. parameters, RL algorithm family, ACT-R memory | Explanation needs the rule of movement, not a catalogue of uses |
| **Computational Psychiatry: A Primer** — Seriès (ed.) → [series-computational-psychiatry](references/reference-series-computational-psychiatry.md) | Psychopathology as parameters; predictive coding; the model-fitting workflow | Model function before dysfunction; recover parameters before interpreting them |

### Methods & inference
| Book (→ file) | Reach for it when you need… | One big idea |
|---|---|---|
| **Andy's Brain Book** — Jahn → [jahn-brain-book](references/reference-jahn-brain-book.md) | What an fMRI result is *allowed to mean* — correction, circularity, reverse inference | A cluster-defining threshold is not an alpha level |
| **Nipraxis** — Brett et al. → [brett-nipraxis](references/reference-brett-nipraxis.md) | The math under the software (GLM, convolution, FWER), and reproducible practice | *Nullius in verba* — build from primitives so you can challenge them |
| **Fundamentals of Brain Network Analysis** — Fornito, Zalesky, Bullmore → [fornito-brain-network-analysis](references/reference-fornito-brain-network-analysis.md) | Graph/connectome measures, hubs, modules, and whether a network difference is real | Node, edge, and threshold are modelling choices; every measure needs a null |
| **Oxford Handbook of ERP Components** — Kappenman & Luck → [kappenman-luck-erp-components](references/reference-kappenman-luck-erp-components.md) | Millisecond dynamics, EEG/MEG, and the meaning of a named component | Peaks are not components |

## Cross-book Topic Index
- **Amygdala / fear conditioning** → byrne-neuroscience-online, oreilly-comp-cog-neuro
- **Aphasia / language / dyslexia** → byrne-neuroscience-online, oreilly-comp-cog-neuro, kappenman-luck-erp-components
- **Attractor dynamics** → oreilly-comp-cog-neuro, series-computational-psychiatry, stocco-explanatory-models
- **Basal ganglia / Go-NoGo gating** → oreilly-comp-cog-neuro, byrne-neuroscience-online, stocco-explanatory-models
- **Bayesian inference / predictive coding** → series-computational-psychiatry, stocco-explanatory-models, forstmann-model-based-cogneuro
- **BOLD / neurovascular coupling** → byrne-neuroscience-online, lim-open-neuroscience, jahn-brain-book, brett-nipraxis
- **Consolidation / amnesia / H.M.** → oreilly-comp-cog-neuro, byrne-neuroscience-online, jahn-brain-book
- **Dopamine / reward prediction error** → oreilly-comp-cog-neuro, byrne-neuroscience-online, stocco-explanatory-models, series-computational-psychiatry
- **Drift-diffusion / evidence accumulation** → forstmann-model-based-cogneuro, stocco-explanatory-models, series-computational-psychiatry
- **Double dissociation** → jahn-brain-book, byrne-neuroscience-online, lim-open-neuroscience
- **EEG/MEG / oscillations** → kappenman-luck-erp-components, forstmann-model-based-cogneuro, lim-open-neuroscience
- **Executive function / PFC / working memory** → oreilly-comp-cog-neuro, byrne-neuroscience-online, forstmann-model-based-cogneuro, series-computational-psychiatry
- **GLM / HRF / convolution** → jahn-brain-book, brett-nipraxis
- **Hippocampus / pattern separation & completion** → oreilly-comp-cog-neuro, byrne-neuroscience-online
- **Inhibition: control vs. competition** → oreilly-comp-cog-neuro, byrne-neuroscience-online
- **Lesion & case-study inference** → lim-open-neuroscience, byrne-neuroscience-online, jahn-brain-book
- **Linking propositions (model ↔ neural data)** → forstmann-model-based-cogneuro, series-computational-psychiatry
- **Localization vs. distributed processing** → lim-open-neuroscience, byrne-neuroscience-online, fornito-brain-network-analysis
- **LTP / NMDA / synaptic plasticity** → byrne-neuroscience-online, oreilly-comp-cog-neuro, series-computational-psychiatry
- **Marr's levels of analysis** → stocco-explanatory-models, forstmann-model-based-cogneuro
- **Model fitting / parameter recovery / comparison** → series-computational-psychiatry, forstmann-model-based-cogneuro, stocco-explanatory-models
- **Multiple comparisons / thresholding** → jahn-brain-book, brett-nipraxis, fornito-brain-network-analysis
- **MVPA / distributed representations / Haxby 2001** → oreilly-comp-cog-neuro, jahn-brain-book
- **Neglect / Balint's / spatial attention** → oreilly-comp-cog-neuro, byrne-neuroscience-online, kappenman-luck-erp-components
- **Reinforcement learning / TD / model-free vs. model-based** → stocco-explanatory-models, oreilly-comp-cog-neuro, forstmann-model-based-cogneuro, series-computational-psychiatry
- **Schizophrenia** → series-computational-psychiatry, kappenman-luck-erp-components, byrne-neuroscience-online, fornito-brain-network-analysis
- **Spatial vs. temporal resolution** → lim-open-neuroscience, kappenman-luck-erp-components, jahn-brain-book
- **Stroop / cognitive control** → oreilly-comp-cog-neuro, forstmann-model-based-cogneuro, jahn-brain-book

## Scope & limits
Covers these ten sources only. Strong on: perception and attention, memory systems, PFC/BG executive function, language, reinforcement learning, sequential-sampling decision models, network/connectome analysis, ERP/EEG temporal dynamics, computational psychiatry, and fMRI methodology. **Thinner** on: MEG source modelling specifically, naturalistic/large-scale neuroimaging datasets, deep-learning models of cognition beyond the classical connectionist material, and post-2024 work (newest source is 2024).

**When a question falls outside or past this corpus** — recent findings, a method no source covers, a live controversy, or a specific paper — **say so first, then search rather than extrapolate.** Books lag by design; that gap is meant to be closed by retrieval, not by stretching an adjacent chapter. Prefer recent reviews and meta-analyses over single studies, and check whether a new result actually overturns the framework or just extends it. **Mark the seam in the answer**: which part rests on the library (durable frameworks, mechanisms, methodological constraints) and which on retrieval (current state, effect sizes, replication status). Retrieved claims do not inherit the library's confidence — and the library's standards still apply to them, so ask of any new finding what the sources here would ask: what mechanism, what level, what null, what boundary conditions.
