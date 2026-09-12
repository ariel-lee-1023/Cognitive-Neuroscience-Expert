# Executed validation

Date: 2026-09-12. This report covers the reference repairs, expert-core changes, optional guide, Python examples, and maintenance checks. Existing AGENTS.md changes were preserved.

## Numerical examples

The three example entry points executed on Python 3.12.7, NumPy 1.26.4, and Matplotlib 3.9.2 using the documented fixed inputs and seeds. The environment already contained these packages; a clean installation was not independently tested. Optional installation requirements pin the two numerical/plotting dependencies. The expert core itself needs neither.

Five demo figures were generated and visually inspected: reward learning/recovery, accumulation distributions, accumulation resolution, timing/design matrices, and near-confounding precision. Axes, legends, censoring labels, matrix column labels, and scientific-status labels were checked against settings and calculations. Outputs stay under the ignored `outputs/` directory when run as documented.

| Check | Executed result | Meaning and limit |
|---|---|---|
| Reward recovery, seed 23 | Mean absolute alpha error 0.0101 for n=120, sigma=0.08; 0.1363 for n=12, sigma=0.35 | Recovery worsens in the combined shorter/noisier condition. This does not isolate the effects of trial count and noise. |
| No information about alpha | NLL range exactly 0 when all rewards equal V0=0.5 | No estimate is reported for the flat likelihood. |
| Diffusion resolution, seed 17 | dt 0.004/0.002/0.001 s: P(upper) 0.7035/0.7000/0.6986; mean RT 1.2591/1.2650/1.2361 s | Continuous no-deadline targets are 0.6900 and 1.1999 s. Sampled crossing bias remains visible, and Monte Carlo variation prevents monotonic convergence. |
| Diffusion deadline during resolution check | No unfinished trials observed in these 8,000-trial runs with 12 s accumulation horizon | This does not prove censoring probability is zero. Main 5 s demonstrations report nonzero censoring where present. |
| Fixed blocks, A-B | Rank 3; contrast variance 0.06751 | Estimable under this HRF, intercept-only design and iid sigma=1 noise. |
| Jittered events, A-B | Rank 3; contrast variance 0.43985 | Different temporal structure, so the comparison does not isolate jitter or establish a universally better schedule. |
| Duplicate event columns | Rank 2; A-B non-estimable, variance omitted; A+B estimable | A pseudoinverse is used only after the contrast's row-space check. |

The diffusion code is an illustrative Euler solver, not a precision fitting engine. The resolution comparison exposes its bias rather than declaring it converged. The tests use explicit tolerances around known continuous results; passing does not establish suitability for arbitrary parameters or empirical inference.

## Automated and behavioral checks

Executed commands completed successfully: `python -m unittest discover -s tests -v` (19 tests), `python scripts/check_references.py` (0 errors, 29 provenance records, 242 review flags), the skill-creator `quick_validate.py` (valid), and `git diff --check` (clean). The review-flag count is a screening result, not 242 established errors. No package manifest existed requiring another repository-specific validator.

- Scientific tests check analytical learning-rule limits, Gaussian recovery, flat likelihoods, repeated seeds, diffusion choice/RT properties and censoring, invalid ranges, convolution scaling and linearity, exact and near confounding, noise scaling, and plotted-data/settings consistency.
- Reference checks validate local links and anchors, provenance fields and exact replacements, canonical skill identity, and known problematic formulations. Categorical-language hits are a review queue, not failures or automatic replacements. HTTP reachability remains separate from scientific verification.
- The skill-creator frontmatter validator checks the canonical entrypoint's naming and metadata; it does not validate neuroscience claims.
- [Conversation evaluations](evaluations/README.md) retain 16 actual answers and two executed numerical figures, assessed for scientific correctness, scope, attribution, and usefulness. The report states arm-isolation and sampling limitations.

Primary web sources were inspected for the targeted corrections, with access and attribution limits recorded in the [audit](audit/README.md). No complete external-link crawl or ten-book revalidation is claimed. Several exact commercial-source passages and the original Bayes-factor threshold attribution remain unresolved.
