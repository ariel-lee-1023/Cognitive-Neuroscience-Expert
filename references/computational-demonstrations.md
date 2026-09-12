# Optional computational demonstrations

Load this guide for a simulation, calculated figure, recovery exercise, or numerical model comparison. A short conceptual answer may need none of these. The examples implement editorial teaching models; they do not reproduce the complete source models.

Before running a demonstration, state the question and the equation that connects inputs to outputs. Define symbols, units, consequential assumptions, input data, parameter values, and a source locator for the rule. Distinguish source-derived structure from teaching choices such as a noise level or reward schedule. Describe what the output can establish and what it cannot.

For a numerical figure, execute the calculation and derive curves, labels, and reported settings from the same results. Record the random seed, numerical time step or search grid, solver or update convention, and software versions where they affect reproduction. Label observed data, fitted predictions, illustrative simulations, and conceptual hypotheses distinctly. For stochastic simulations, separate Monte Carlo variability from numerical approximation error. Inspect the rendered figure, not just its data file.

Four different checks answer four different questions:

- **Implementation correctness:** Does code obey the stated equations, boundary cases, and units?
- **Parameter recovery:** Under the specified observation model, task, noise, and sample sizes, can known generating parameters be recovered? A fitted curve or regularized estimate alone does not establish this.
- **Model comparison:** Can the design distinguish candidate accounts, and does the chosen comparison criterion fit the inferential goal?
- **Empirical adequacy:** Do predictions capture observed behavior or measurements, including uncertainty and relevant alternatives? Passing implementation and recovery checks does not establish this.

When code execution is unavailable, provide the equations, executable code or a proposed procedure, and anticipated qualitative behavior labelled as a prediction. Do not claim to have run it, invent numerical results, or draw a quantitative curve as if it came from a calculation. A clearly labelled conceptual diagram remains useful.

## Included examples

Run from the repository root using [installation and commands](../README.md#optional-python-demonstrations).

### Reward learning

Question: how does a learning rate change tracking, and when is it recoverable?

$V_{t+1}=V_t+\alpha(r_t-V_t)$, where $V_t$ is value before trial $t$, $r_t$ is the externally supplied reward, $\alpha\in[0,1]$, and $V_0=0.5$. Source locator: [O'Reilly, Ch 8, Rescorla-Wagner](reference-oreilly-comp-cog-neuro.md) and [Stocco, RL](reference-stocco-explanatory-models.md). The teaching model uses one cue and no action selection.

All learning rates receive the same [reward sequence](../demos/data/rewards.csv), with no feedback from model choices. Limiting cases: $\alpha=0$ preserves the initial value; $\alpha=1$ sets the next value to the last reward. The bounded recovery exercise observes $y_t\sim\mathcal N(V_t,\sigma^2)$ before the update, with known $\sigma$ and $V_0$, and searches 99 alpha values from 0.01 to 0.99. These are noisy value reports, not binary choices. Full input and short/noisy conditions compare recovery; constant rewards equal to $V_0$ give a flat likelihood and no identifiable alpha. Trial counts, repetitions, seeds, errors, and grid are saved. Multiple free parameters, misspecification, or different observation processes require fresh recovery checks; no clinical claims follow.

### Evidence accumulation

Question: how can drift, boundary, and starting point alter choices and RT distributions?

$dX=v\,dt+s\,dW$ is approximated by $X_{k+1}=X_k+v\Delta t+s\sqrt{\Delta t}\epsilon_k$, with independent standard-normal $\epsilon_k$. $v$ is drift in evidence units/s, $s$ diffusion noise in evidence units/$\sqrt{\mathrm s}$, $X_0$ starting evidence, and absorbing boundaries are $-a,+a$. RT is the first sampled crossing time plus fixed non-decision time. Source locator: [Forstmann & Turner, DDM chapter](reference-forstmann-model-based-cogneuro.md). This Euler example is not a full Ratcliff fitting implementation.

Unfinished trials receive choice 0 and missing RT. Histograms show fractions of **all** trials, with censoring reported; finished-only RT summaries are labelled. Compare steps 0.004, 0.002, and 0.001 s against continuous-time no-deadline results for $X_0=0$: $P(+)=[1+\exp(-2va/s^2)]^{-1}$ and $E[T]=a\tanh(av/s^2)/v$, with limit $a^2/s^2$ at $v=0$. Finite deadlines, sampled crossings, and Monte Carlo variation limit agreement. A reproduced pattern is not identification of a biological mechanism.

### Signal convolution and timing

Question: does response overlap prevent estimating a particular contrast?

$x_j(t)=\int u_j(\tau)h(t-\tau)d\tau$ maps input $u_j$ through an assumed linear, time-invariant response $h$. Use a unit-area double gamma, sampled convolution at 0.1 s, TR=1 s, and $y=X\beta+\epsilon$ with an intercept and iid Gaussian noise of known $\sigma=1$. Source locators: [Nipraxis convolution and GLM](reference-brett-nipraxis.md), [Jahn design optimization](https://andysbrainbook.readthedocs.io/en/latest/SPM/SPM_Short_Course/AppendixD_DesignOptimization.html).

Fixed blocks and jittered events each supply 30 input-area units per condition, but their temporal structures differ; this is not an experiment isolating jitter. A deliberately confounded schedule duplicates the two condition columns. Examine both $c=(1,-1,0)$ and $c=(1,1,0)$. A contrast is estimable when $c$ lies in the row space of $X$; only then report $\operatorname{Var}(c^T\hat\beta)=\sigma^2\|c^TX^+\|^2$. Here $X^+$ is the Moore-Penrose pseudoinverse. Duplicate columns destroy A-B estimation but preserve A+B. A near-confounding series shows large finite variance before exact non-estimability. Numerical rank tolerance is not a threshold for scientifically useful precision. Real studies need appropriate HRFs, nuisance regressors, temporal filtering, noise covariance, and contrast-specific evaluation; jitter is not always superior.
