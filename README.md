# Cognitive Neuroscience Expert

An [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) that turns an agent into a senior, rigorous, **mechanism-oriented cognitive neuroscientist** — capable of mechanism explanation, theoretical comparison, evidence evaluation, experimental-design reasoning, methodological boundary-setting, and cross-level integration.

It is a distillation of **ten open or standard sources** across three layers: how the brain implements cognition, how formal models are built and linked to neural data, and what the methods will and will not support.

## Layout

```
SKILL.md                  # router + operating stance + cross-book topic index (always loaded)
references/
  reference-<slug>.md     # one dense, standalone distillation per source (loaded on demand)
```

`SKILL.md` is the only file an agent loads automatically. It routes to the reference files, which cost nothing until opened.

## Sources

### Mechanism & systems
| Source | Distillation |
|---|---|
| **Computational Cognitive Neuroscience, 4th ed.** — O'Reilly, Munakata, Hazy, Frank et al. ([CompCogNeuro/ed4](https://github.com/CompCogNeuro/ed4)) | [`reference-oreilly-comp-cog-neuro.md`](references/reference-oreilly-comp-cog-neuro.md) |
| **Neuroscience Online** — Byrne, Wright, Dougherty et al., UTHealth ([nba.uth.tmc.edu](https://nba.uth.tmc.edu/neuroscience/)) | [`reference-byrne-neuroscience-online.md`](references/reference-byrne-neuroscience-online.md) |
| **Open Neuroscience Initiative** — Austin Lim ([austinlim.com](https://www.austinlim.com/open-neuroscience-initiative)) | [`reference-lim-open-neuroscience.md`](references/reference-lim-open-neuroscience.md) |

### Formal models
| Source | Distillation |
|---|---|
| **An Introduction to Model-Based Cognitive Neuroscience, 2nd ed.** — Forstmann & Turner (eds.), Springer 2024 | [`reference-forstmann-model-based-cogneuro.md`](references/reference-forstmann-model-based-cogneuro.md) |
| **Explanatory Computational Models in Cognitive Neuroscience** — Andrea Stocco | [`reference-stocco-explanatory-models.md`](references/reference-stocco-explanatory-models.md) |
| **Computational Psychiatry: A Primer** — Peggy Seriès (ed.), MIT Press 2020 | [`reference-series-computational-psychiatry.md`](references/reference-series-computational-psychiatry.md) |

### Methods & inference
| Source | Distillation |
|---|---|
| **Andy's Brain Book** — Andrew Jahn ([readthedocs](https://andysbrainbook.readthedocs.io/)) | [`reference-jahn-brain-book.md`](references/reference-jahn-brain-book.md) |
| **Nipraxis: Practical Neuroimaging in Python** — Matthew Brett et al. ([textbook.nipraxis.org](https://textbook.nipraxis.org/)) | [`reference-brett-nipraxis.md`](references/reference-brett-nipraxis.md) |
| **Fundamentals of Brain Network Analysis** — Fornito, Zalesky & Bullmore, Academic Press 2016 | [`reference-fornito-brain-network-analysis.md`](references/reference-fornito-brain-network-analysis.md) |
| **The Oxford Handbook of Event-Related Potential Components** — Kappenman & Luck (eds.), OUP | [`reference-kappenman-luck-erp-components.md`](references/reference-kappenman-luck-erp-components.md) |

## Install

Clone into your agent's skill directory. For Claude Code:

```bash
git clone https://github.com/ariel-lee-1023/Cognitive-Neuroscience-Expert.git ~/.claude/skills/cognitive-neuroscience
```

Other hosts use different roots — e.g. `~/.copilot/skills/`, `~/.agents/skills/`, `.claude/skills/` for project scope. The directory name becomes the skill name, so keep it `cognitive-neuroscience` to match the `name:` in `SKILL.md`.

## Usage

```
cognitive-neuroscience                          # router — pick the right source
cognitive-neuroscience about <topic>            # topic index → the relevant reference file(s)
cognitive-neuroscience for <book>               # open one distillation directly
```

Most substantive questions pull **two or three** files: one for the mechanism, one for the formal model, one for the method or evidence that constrains them.

## What kind of distillation this is

Structure, not summary. Each reference file preserves the authors' own framework names and exact formulations, defines key terms inline, folds techniques in as procedures, and ends with a `Decision Rules & Judgment` section — the author's if/then judgment stated so it can be acted on without re-reading. Nothing is copied verbatim at length; everything is synthesized.

Each file also carries an explicit **coverage note** recording what was compressed or dropped and why, so the gaps are visible rather than silent.

## Scope

Strong on perception and attention, memory systems, PFC/BG executive function, language, reinforcement learning, sequential-sampling decision models, network/connectome analysis, ERP/EEG temporal dynamics, computational psychiatry, and fMRI methodology.

Thinner on MEG source modelling, naturalistic/large-scale datasets, deep-learning models of cognition beyond classical connectionism, and post-2024 work (newest source is 2024). `SKILL.md` instructs the agent to **name the gap and search rather than extrapolate** when a question falls outside the corpus, and to mark which part of an answer rests on the library versus on retrieval.

## Provenance

Built with [`books-to-skill-refs`](https://github.com/obra/superpowers), which distills multiple sources in one pass into a single shared, cross-referenced library. Web-hosted sources were fetched and consolidated before extraction; every reference file was checked against the skill's own contract validator and injected-instruction scanner.

## License

The distillations are derivative summaries of their sources and follow those sources' terms — several are CC-licensed open educational resources (CompCogNeuro ed4, Open Neuroscience Initiative CC BY-NC 4.0, Nipraxis, Andy's Brain Book); others distill commercially published books (Springer, MIT Press, OUP, Academic Press) and are structural summaries for personal study, not reproductions. Check the individual source's license before redistributing.
