# Cognitive Neuroscience Expert

An [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) that turns an agent into a senior, rigorous, **mechanism-oriented cognitive neuroscientist** — capable of mechanism explanation, theoretical comparison, evidence evaluation, experimental-design reasoning, methodological boundary-setting, and cross-level integration.

It is a distillation of **fourteen open or standard sources** across three layers: how the brain implements cognition, how formal models are built and linked to neural data, and what the methods will and will not support.

## Layout

```
SKILL.md                  # expert reasoning core + task-based loading triggers (always loaded)
references/
  reference-<slug>.md     # fourteen source distillations, loaded on demand
  computational-demonstrations.md  # optional numerical-work guide
fidelity-ledger/          # four-book provenance, coverage, and validation records
demos/                    # reusable Python models, plotting entrypoint, reward input
tests/                    # analytical, numerical, and plotting-data checks
scripts/check_references.py # links, provenance, known regressions, prose review flags
maintenance/              # audit and evaluation records, not domain loading
outputs/                  # ignored generated figures and settings
```

`SKILL.md` is the expert entrypoint; root `AGENTS.md` also guides work when this repository is opened as a project. It establishes the expert’s reasoning stance, then routes tasks to reference files that load only when needed.

## Sources

### Mechanism & systems
| Source | Distillation |
|---|---|
| **Computational Cognitive Neuroscience, 4th ed.** — O'Reilly, Munakata, Hazy, Frank et al. ([CompCogNeuro/ed4](https://github.com/CompCogNeuro/ed4)) | [`reference-oreilly-comp-cog-neuro.md`](references/reference-oreilly-comp-cog-neuro.md) |
| **Neuroscience Online** — Byrne, Wright, Dougherty et al., UTHealth ([nba.uth.tmc.edu](https://nba.uth.tmc.edu/neuroscience/)) | [`reference-byrne-neuroscience-online.md`](references/reference-byrne-neuroscience-online.md) |
| **Open Neuroscience Initiative** — Austin Lim ([austinlim.com](https://www.austinlim.com/open-neuroscience-initiative)) | [`reference-lim-open-neuroscience.md`](references/reference-lim-open-neuroscience.md) |
| **Explaining the Brain: Mechanisms and the Mosaic Unity of Neuroscience** — Carl F. Craver, OUP 2007 | [`reference-craver-explaining-brain.md`](references/reference-craver-explaining-brain.md) |

### Formal models
| Source | Distillation |
|---|---|
| **An Introduction to Model-Based Cognitive Neuroscience, 2nd ed.** — Forstmann & Turner (eds.), Springer 2024 | [`reference-forstmann-model-based-cogneuro.md`](references/reference-forstmann-model-based-cogneuro.md) |
| **Explanatory Computational Models in Cognitive Neuroscience** — Andrea Stocco | [`reference-stocco-explanatory-models.md`](references/reference-stocco-explanatory-models.md) |
| **Computational Psychiatry: A Primer** — Peggy Seriès (ed.), MIT Press 2020 | [`reference-series-computational-psychiatry.md`](references/reference-series-computational-psychiatry.md) |
| **Theoretical Neuroscience** — Peter Dayan & L. F. Abbott, supplied December 2000 chapter drafts | [`reference-dayan-abbott-theoretical-neuroscience.md`](references/reference-dayan-abbott-theoretical-neuroscience.md) |

### Methods & inference
| Source | Distillation |
|---|---|
| **Andy's Brain Book** — Andrew Jahn ([readthedocs](https://andysbrainbook.readthedocs.io/)) | [`reference-jahn-brain-book.md`](references/reference-jahn-brain-book.md) |
| **Nipraxis: Practical Neuroimaging in Python** — Matthew Brett et al. ([textbook.nipraxis.org](https://textbook.nipraxis.org/)) | [`reference-brett-nipraxis.md`](references/reference-brett-nipraxis.md) |
| **Fundamentals of Brain Network Analysis** — Fornito, Zalesky & Bullmore, Academic Press 2016 | [`reference-fornito-brain-network-analysis.md`](references/reference-fornito-brain-network-analysis.md) |
| **The Oxford Handbook of Event-Related Potential Components** — Kappenman & Luck (eds.), OUP | [`reference-kappenman-luck-erp-components.md`](references/reference-kappenman-luck-erp-components.md) |
| **Causal Inference: What If** — Miguel A. Hernán & James M. Robins, February 21, 2020 version | [`reference-hernan-robins-causal-inference.md`](references/reference-hernan-robins-causal-inference.md) |
| **An Introduction to the Event-Related Potential Technique** — Steven J. Luck, supplied **first edition (2005)** | [`reference-luck-erp-technique.md`](references/reference-luck-erp-technique.md) |

## Four-book extension (2026-09-12)

The extension strengthens four linked capabilities: distinguishing a mechanism sketch from an established biological mechanism; deriving neural coding, dynamics, and learning results with their assumptions; identifying causal effects before estimating them; and tracing ERP conclusions through experimental design, acquisition, preprocessing, and measurement. The core now uses these distinctions in its reasoning, with four new source references and combined-loading guidance.

The source files determine the edition labels. In particular, the provided Luck book is the **2005 first edition**, although the requested capability table names the second edition. No second-edition additions are claimed. Dayan–Abbott is a December 2000 draft rather than a verified final-edition transcription. Equations were reconstructed from imperfect Markdown and checked selectively; chapter/section locators and limitations accompany the methods.

The repository keeps its existing root `SKILL.md` and one canonical reference per source. `.agents/skills/cognitive-neuroscience` points to the root. Existing local demonstrations and maintenance records remain in place; new provenance, coverage, reading, and validation records are in [fidelity-ledger](fidelity-ledger/README.md). The [executed acceptance report](fidelity-ledger/acceptance-report.md) records fresh-context answers for all 10 prepared cases and two mathematical regressions, with model settings and criterion-level review. All 12 selected answers passed that review. Baseline/core-only comparative arms remain **unrun**, so these results establish bounded current-version acceptance, not measured reasoning improvement.

## Install

Clone into your agent's skill directory. For Claude Code:

```bash
git clone https://github.com/ariel-lee-1023/Cognitive-Neuroscience-Expert.git ~/.claude/skills/cognitive-neuroscience
```

For another host, use its configured skill directory and keep the complete `SKILL.md` and `references/` tree together; include `demos/` and `requirements-demo.txt` to run the optional examples. Match the installed folder name to the `name:` field in `SKILL.md`.

## Usage

```
cognitive-neuroscience                          # reason from the expert core
cognitive-neuroscience about <topic>            # answer using relevant source depth
cognitive-neuroscience for <book>               # open one distillation directly
```

Load the smallest set of references that can support the question. Combine mechanism, formal-model, and method sources when the claim crosses those levels; a narrow question may need only one module.

## What kind of distillation this is

Structure, not summary. Each reference preserves source framework names, defines terms inline, and condenses mechanisms and procedures into worked examples and decision rules. These are editorial syntheses, not authoritative transcriptions of an author's universal advice. Preserve task, model, and measurement conditions when reusing a passage. Corrections distinguish source-specific positions from added methodological evidence; exact source verification remains incomplete for some passages.

Each file also carries an explicit **coverage note** recording what was compressed or dropped and why, so the gaps are visible rather than silent.

## Scope

Strong on perception and attention, memory systems, PFC/BG executive function, language, reinforcement learning, sequential-sampling decision models, network/connectome analysis, ERP/EEG temporal dynamics, computational psychiatry, fMRI methodology, mechanistic explanation standards, neural encoding/decoding and information theory, causal identification, and ERP acquisition and measurement.

Thinner on MEG source modelling, naturalistic/large-scale datasets, deep-learning models of cognition beyond classical connectionism, and post-2024 work (newest source is 2024). `SKILL.md` instructs the agent to **name the gap and search rather than extrapolate** when a question falls outside the corpus, and to mark which part of an answer rests on the library versus on retrieval.

## Optional Python demonstrations

The expert core has no Python dependency. For calculations, use Python 3.10–3.12 (execution tested with 3.12), create a virtual environment, and install the two pinned packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-demo.txt
python -m demos.run all --out outputs
```

The supported interpreter range is limited by the pinned dependencies: [NumPy 1.26.4 supports Python 3.9–3.12](https://numpy.org/doc/2.3/release/1.26.4-notes.html), and this repository targets 3.10–3.12. Execution in an existing environment does not establish clean-install compatibility on every supported platform.

Individual entry points:

```bash
python -m demos.run reward --rewards demos/data/rewards.csv --out outputs
python -m demos.run accumulation --out outputs
python -m demos.run timing --out outputs
```

An external rewards file has a `reward` header and one finite numeric reward per row. Every learning rate receives the identical sequence. The included 120-trial sequence is fixed teaching input, not participant data. Replace it to inspect how recovery depends on task information.

The commands generate five PNG figures, three JSON result/settings records, and three sampled design-matrix CSV files. Results record seeds, parameter values, numerical resolution, input values or settings, and runtime versions. `demos/models.py` contains reusable calculations; `demos/run.py` handles plotting and output. No notebooks are required.

- **Reward:** delta-rule dynamics, alpha=0/1 limits, bounded one-parameter recovery under noisy Gaussian value reports, deteriorated recovery, and an exactly flat likelihood.
- **Accumulation:** an illustrative Euler diffusion model showing drift, boundary, and starting-point effects on choice and RT distributions. It reports unfinished trials and checks time-step sensitivity against analytic no-deadline results.
- **Timing:** a fixed block schedule, jittered events, and duplicate condition regressors. It displays convolved signals and actual design matrices, evaluates A-B and A+B, and separates non-estimability from large finite variance.

Read the [optional guide](references/computational-demonstrations.md) for equations, assumptions, source locators, and limitations. These are illustrative calculations, not fitted empirical findings or clinical tools. A recovered teaching-model parameter does not establish an individual's biological mechanism. The diffusion implementation has discretization bias; the timing example assumes a known linear HRF and iid noise and does not prove jitter superiority.

## Verification and maintenance

```bash
python -m unittest discover -s tests -v
python scripts/check_references.py --report outputs/reference-check.json
# Optional HTTP reachability check, requiring network access:
python scripts/check_references.py --external --report outputs/reference-check-external.json
```

Local checks validate links, required provenance fields, and known problematic formulations, and flag categorical language for substantive review. External HTTP failures are recorded as unverified; passing link checks does not establish source accuracy. Numerical tests cover analytical limits, identifiability, seed repeatability, sampling conventions, and figure/data consistency. Passing these tests is implementation evidence, not scientific validation.

The [maintenance audit](maintenance/audit/README.md) explains the correction process and unresolved source checks. The [validation report](maintenance/validation.md) records executed checks and limitations; [conversation evaluations](maintenance/evaluations/README.md) retain prompts, actual responses, and reviewer assessments. These records are not part of routine domain loading.

## Provenance

Built with [`books-to-skill-refs`](https://github.com/ariel-lee-1023/Books-to-Skill-Refs), which distills multiple sources in one pass into a single shared, cross-referenced library. Web-hosted sources were fetched and consolidated before extraction; every reference file was checked against the skill's own contract validator and injected-instruction scanner.

## License

[MIT](LICENSE) — covering the original work here: the skill structure, expert core, loading guidance, README, and the distillation text as written.

The underlying sources keep their own terms and are not relicensed by this. Several are open educational resources (Open Neuroscience Initiative is CC BY-NC 4.0; CompCogNeuro ed4, Nipraxis and Andy's Brain Book carry their own); others are commercially published (Springer, MIT Press, OUP, Academic Press). The reference files are structural summaries — frameworks, terminology and decision rules restated in condensed form — not reproductions. Check the individual source before redistributing or building on this.
