# Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems — Peter Dayan & L. F. Abbott
**Format**: md | **Pages**: ~631 (extractor estimate, not printed pagination) | **Sections**: 10 chapters | **Depth**: study | **Type**: technical

**Source version:** supplied chapter drafts dated December 2000, principally December 17 with some December 19 headers. Do not present this file as a verified transcription of the final 2001 edition. OCR damages mathematical typography; equations below are reconstructed with defined notation, rather than copied from malformed expressions. Locators use chapter and section numbers because pagination restarts between chapters.

## Mental Model (read first)
Dayan and Abbott distinguish **descriptive** models of what neurons do, **mechanistic** models of how they do it, and **interpretive** models of why a computation or representation might be useful. Select a model's level of detail to answer the question: more biological detail is not automatically a better explanation. Neural coding, membrane and circuit dynamics, and learning constrain one another, but an optimal decoder or fitted generative model does not by itself establish an implemented biological mechanism.

For any equation identify the variables, observable data, units, assumptions, and criterion of success. Neural **encoding** specifies a response distribution given a stimulus; **decoding** reconstructs a stimulus or decision from a response. Information accessible to an analyst is distinct from information the animal actually uses.

**Use for:** spike statistics; receptive-field estimation; likelihood and Bayesian decoding; information theory; membrane, cable and network dynamics; Hebbian, supervised, reinforcement, and representational learning. Pair with [Craver](reference-craver-explaining-brain.md) when a mathematical result is promoted to an actual-mechanism claim.

## Frameworks & Structure

### Chapter 1 — Neural Encoding I: firing rates and spike statistics
**Locator:** §§1.2–1.5, with notation and statistical definitions in §1.6.

Represent a spike train as `ρ(t)=Σi δ(t−ti)`, where `ti` are spike times and the Dirac delta has units of inverse time. Distinguish the time-dependent trial-averaged rate `r(t)`, a single-trial **spike-count rate** `n/T`, and the average rate over the relevant ensemble or interval. A rate always depends on an averaging operation or time scale; treating these quantities as interchangeable conceals variability.

A **tuning curve** `f(s)` describes the mean response to a static stimulus parameter s. Gaussian, cosine, and sigmoidal tuning curves are descriptive families, not distinct biological mechanisms. **Spike-triggered averaging** examines stimulus histories preceding spikes and is conditional on the stimulus ensemble used.

For a **homogeneous Poisson process**, a constant rate r gives

`P(n | r,T)=exp(−rT)(rT)^n/n!`, with `E[n]=Var(n)=rT`.

Its interspike intervals are exponentially distributed. An **inhomogeneous Poisson process** replaces rT with `∫r(t)dt` for the count mean, while allowing stimulus-driven rate changes. Independent increments are part of the model; refractoriness, adaptation, and history effects can violate that assumption.

The **Fano factor** `Var(n)/E[n]` measures count dispersion over a stated window. The **coefficient of variation** of interspike intervals is their standard deviation divided by their mean. Each is one for the homogeneous Poisson benchmark, but matching either statistic does not prove a Poisson process. Autocorrelation, cross-correlation, interval distributions, and power spectra expose different temporal structure.

**Independent-spike**, **independent-neuron**, and **correlation codes** make different independence assumptions. Distinguish stimulus-driven covariation from response covariation conditional on the stimulus. Whether precise timing conveys information is a question about temporal resolution and the stimulus–response relationship, not a choice between saying “spikes” and “rates.”

### Chapter 2 — Neural Encoding II: reverse correlation and receptive fields
**Locator:** §§2.2–2.8 and §2.9 appendices.

A linear response model has the form

`r_lin(t)=r0+∫0∞ D(τ)s(t−τ)dτ`.

Here s is a centered stimulus history, D is the causal **linear filter** or first **Wiener kernel**, and r0 is a baseline. A **static nonlinearity** produces `r_est(t)=F(r_lin(t))`, accommodating nonnegative rates, thresholding, or saturation. A **Volterra expansion** adds higher-order stimulus products; a linear filter followed by one nonlinearity remains a restricted family.

**How to estimate:** define the stimulus ensemble and measured rate; choose D to minimize mean squared prediction error; account for stimulus autocorrelation. For white-noise input the optimal linear kernel is proportional to the spike-triggered average, with rate and stimulus-variance scaling. For correlated stimuli, raw spike-triggered averaging mixes neural selectivity with stimulus covariance; the linear estimation problem must account for that covariance. Nonlinear responses may require higher-order features and can escape a first-order estimate.

**Difference-of-Gaussians** filters describe center–surround organization in retina and LGN. **Gabor functions** combine an envelope with a sinusoidal structure to describe spatial-frequency, phase, and orientation selectivity. Space–time separability is a substantive assumption; nonseparable filters can express direction selectivity. Complex-cell **energy models** combine squared responses of phase-shifted filters to reduce phase sensitivity. These are computational descriptions; a matching receptive field does not uniquely identify its generating circuit.

Retinotopic mapping, sampling, and feedforward models connect the representations to geometry and plausible circuits. Apply **Nyquist** reasoning to the sampling problem actually at issue; adequate temporal sampling does not imply adequate spatial sampling, or vice versa.

### Chapter 3 — Neural decoding: specify what “optimal” means
**Locator:** §§3.2–3.4, especially Bayesian/MAP/ML inference and Fisher information in §3.3.

For binary discrimination, a **likelihood-ratio test** compares `p(r|s1)/p(r|s0)` with a threshold chosen from priors, costs, or a specified false-positive rate. A **receiver operating characteristic** traces hit versus false-alarm rates as the decision threshold varies. The **Neyman–Pearson lemma** specifies the most powerful test for simple hypotheses at a fixed false-positive rate; it does not certify an animal's decision rule.

The **population vector** is a weighted combination of preferred stimulus directions. It can work well with appropriate tuning shapes and population coverage, but it is neither generally optimal nor unbiased under arbitrary tuning and sampling.

Bayes' rule gives `p(s|r) ∝ p(r|s)p(s)`:

- **Maximum likelihood (ML):** maximize `p(r|s)`.
- **Maximum a posteriori (MAP):** maximize `p(s|r)`; a uniform prior makes its optimum match ML in the chosen parameterization.
- **Bayesian decision:** minimize posterior expected loss. Squared-error loss gives the posterior mean; absolute-error loss gives a posterior median. “Bayesian” does not always mean MAP.

For conditionally independent Poisson counts ni in a window T with tuning rates fi(s),

`log p(n|s)=Σi [ni log(T fi(s)) − T fi(s) − log(ni!)]`.

Terms independent of s can be removed for optimization. Conditional independence must be checked or treated as a modeling assumption: when responses share variability, use an appropriate joint response distribution. Rates alone do not determine it.

**Fisher information** measures local sensitivity of the response distribution:

`J(s)=E[(∂s log p(r|s))²]`.

Under the differentiability and regularity assumptions of the bound, an unbiased estimator obeys `Var(ŝ|s) ≥ 1/J(s)`. For a biased estimator with bias `b(s)=E[ŝ|s]−s`, the variance bound is `(1+b′(s))²/J(s)`; mean squared error also includes `b(s)²`. Do not apply the unbiased bound as a universal lower bound on all reconstruction errors.

For the independent Poisson count model, `J(s)=T Σi [fi′(s)]²/fi(s)` where rates are positive. Tuning-curve slope relative to variability can matter more than peak response. A large J characterizes information under a model; it does not demonstrate biological readout or attainable performance for finite samples and a constrained decoder.

**Spike-train reconstruction** uses filters to estimate a time-varying stimulus from spike trains. Its quality depends on the loss, chosen filter family, response statistics, and time resolution; poor linear reconstruction need not imply an absence of nonlinear information.

### Chapter 4 — Information theory: signal, variability, and measurement resolution
**Locator:** §§4.1–4.3; spike-word entropy extrapolation and the H1 example.

For discrete responses R, **entropy** is `H(R)=−Σr p(r)log2 p(r)`. **Noise entropy** is `H(R|S)=Σs p(s)H(R|s)`. **Mutual information** is

`I(S;R)=H(R)−H(R|S)=Σs,r p(s,r)log2[p(s,r)/(p(s)p(r))]`.

It measures the reduction in uncertainty about one variable given the other. Higher response entropy alone can reflect increased noise; it need not mean more stimulus information. **Kullback–Leibler divergence** measures discrepancy between distributions and gives another expression for mutual information averaged over stimuli. It is not a symmetric distance.

Information is defined relative to a stimulus distribution, response representation, recording window, and resolution. Continuous-variable differential entropy depends on coordinates; discretization must be specified when making numerical entropy comparisons. Information estimates for individual neurons cannot simply be added if their responses provide redundant or synergistic information.

**Entropy maximization** and **information maximization** offer interpretive principles for efficient representations. Response equalization, decorrelation or whitening, and noise-dependent filtering can follow under particular constraints. A transformation that removes correlations is not automatically maximally informative under every noise model. PCA and ICA also answer different questions: decorrelation does not guarantee statistical independence.

**Spike-word method:** bin spikes at resolution Δt, define words of duration Ts, and estimate total and stimulus-conditioned word probabilities. Increasing Ts can capture longer dependencies but rapidly worsens sampling demands. Treating short successive words as independent can overestimate entropy rate; sparse empirical counts introduce an additional estimation problem. Examine stability across word length and available trials rather than interpreting every increase in estimated information as new coding structure. The H1 example extrapolates entropy rates in `1/Ts` only over a region supported by data; the breakdown at long words is part of the lesson.

### Chapter 5 — Model Neurons I: neuroelectronics
**Locator:** §§5.2–5.9.

The **Nernst equation**, `Eion=(RT/zF) ln([ion]out/[ion]in)`, defines an equilibrium potential for one ion under its assumptions. R is the gas constant, T absolute temperature, z valence, and F Faraday's constant. A resting membrane with several permeant ions is not described by selecting one arbitrary Nernst potential.

A compact current-balance form is

`C dV/dt = Iext − Σj gj(V,t)(V−Ej)`.

V is membrane voltage, C capacitance, gj conductance, and Ej reversal potential, using outward ionic current as positive in the sum. Use either total or area-specific capacitance and conductance consistently. The driving force `(V−Ej)` matters: changing conductance is not equivalent to adding a fixed current. An inhibitory conductance can shunt an input with little change in resting voltage.

A passive compartment gives a membrane time constant `τm=Rm Cm`. **Leaky integrate-and-fire** combines subthreshold dynamics with an imposed threshold, spike event, reset, and possibly refractoriness. It does not derive the action-potential waveform. The **Hodgkin–Huxley model** describes voltage-dependent conductances using gating variables; a standard gate obeys `dx/dt=αx(V)(1−x)−βx(V)x`, or `(x∞(V)−x)/τx(V)`.

Channel-state models, stochastic opening, synaptic release variability, and synaptic conductance time courses supply different levels of detail. **Short-term facilitation and depression** describe history-dependent efficacy and must be distinguished from persistent learning-induced changes. Pick the simplest level that preserves the phenomenon and intervention contrast being studied.

### Chapter 6 — Model Neurons II: conductances and morphology
**Locator:** §§6.1–6.4.

Additional conductances change firing patterns: transient potassium currents, calcium currents, and calcium-dependent potassium currents can support delays, adaptation, and bursting in particular combinations. A pattern does not uniquely identify the conductance combination that produced it.

The **cable equation** adds spatial current flow to membrane current balance. For a uniform passive cable in normalized voltage notation,

`τm ∂tV = λ² ∂²xV − V + drive`,

where λ is the length constant; geometry and boundary conditions determine the solution. A soma-only model can miss attenuation, delays, and location dependence of dendritic inputs.

**Multi-compartment models** discretize morphology into electrically coupled compartments with local membrane and axial currents. They can represent dendritic processing and propagating spikes, including effects of myelination. Compartment length, time step, parameter identifiability, and boundary conditions matter to a simulation. Morphological detail is useful when the question depends on location; it can otherwise add cost and poorly constrained parameters.

### Chapter 7 — Network models: dynamics before interpretation
**Locator:** §§7.2–7.7, especially linear recurrent networks (§7.4) and excitatory–inhibitory networks (§7.5).

A firing-rate network can be written `τr dv/dt=−v+F(h+Mv)`, with input h, recurrent weights M, and response nonlinearity F. **Feedforward networks** transform inputs without recurrent feedback; **recurrent networks** can amplify, integrate, compete, sustain activity, or oscillate. A behavior generated by recurrence is not necessarily unique to recurrence.

For the linear model with symmetric M, each eigenmode satisfies

`τr dcμ/dt=−(1−λμ)cμ+hμ`.

For `λμ<1`, constant input produces `cμ*=hμ/(1−λμ)`, with effective time constant `τr/(1−λμ)`. A mode approaching one from below becomes both more amplified and slower. At one it acts as an ideal integrator in the linear model; above one it is unstable until some unmodeled or explicit nonlinearity constrains it. Negative modeled activity needs a stated interpretation, such as deviation from baseline; literal rates cannot be negative.

Nonlinear models support **attractors**, **continuous attractors**, **winner-take-all competition**, **gain modulation**, and **content-addressable memory** under appropriate architecture and gain. Analyze fixed points and local stability; for a general continuous-time linearization stability depends on negative real parts of the Jacobian eigenvalues. A static connectivity picture does not establish a trajectory or stable memory state.

Excitatory–inhibitory interactions can support oscillations; delays, time constants, coupling, and gain matter. The **Boltzmann machine** connects stochastic binary networks, energy functions, and probabilistic representations. An energy or Lyapunov argument relies on its connectivity and dynamics assumptions and must not be applied indiscriminately to asymmetric biological networks.

### Chapter 8 — Plasticity and learning: stability and competition
**Locator:** §§8.2–8.4.

With presynaptic activities u and postsynaptic activity v, the **basic Hebb rule** increases weights according to `dw/dt ∝ vu`. For slow learning and a linear steady-state neuron `v=w·u`, averaging gives growth governed by the input correlation matrix. Unconstrained positive feedback can make weights grow without bound; “cells that fire together” does not specify a stable learning system.

**Covariance rules** subtract activity means; principal-component interpretations depend on centering and constraints. **Subtractive normalization** subtracts a shared amount from weight changes and needs appropriate bounds. **Multiplicative normalization**, including the **Oja rule** `τw dw/dt=vu−αv²w`, stabilizes the norm under its assumptions. Its theoretical utility is not evidence that a biological synapse implements that exact expression.

**BCM/sliding-threshold** rules change the sign of plasticity according to activity relative to an adapting threshold. **Spike-timing-dependent rules** introduce order and timing, supporting temporal associations that a time-averaged coactivation measure can miss. State the timing convention and model rather than treating one timing curve as universal.

Multiple output neurons need competition or decorrelation to avoid learning the same feature repeatedly. **Anti-Hebbian learning**, competitive networks, **self-organizing maps**, and the **elastic net** impose different balances of competition and cooperation. These models illustrate ocular dominance and map formation without making a fitted map a complete developmental mechanism.

**Supervised Hebbian**, **perceptron**, and **delta-rule/gradient** methods use a teaching signal with different objectives and constraints. A perceptron convergence argument depends on separability; **backpropagation** and **contrastive Hebbian learning** introduce additional architectures or phases. Keep the availability and biological plausibility of the teaching information explicit.

### Chapter 9 — Classical conditioning and reinforcement learning
**Locator:** §§9.2–9.4 and the Markov decision process appendix.

The **Rescorla–Wagner rule** uses prediction error shared across active cues: with `v=Σi wi ui`, update `Δwi=ηi ui(r−v)`. Blocking follows because a previously predictive cue leaves little error to teach a new cue, even when that cue is paired with reward. Pairing alone therefore does not characterize the learning rule.

**Temporal-difference learning** shifts from predicting immediate reward to predicting return across time. In discounted notation, `δt=rt+γV(st+1)−V(st)`; γ is the discount factor and the update uses the active representation or eligibility trace. The source also uses finite absorbing episodic formulations without an explicit discount; these are not contradictory conventions.

For action choice, distinguish learning values from choosing actions, and a **direct actor** update from selecting actions using an estimated value. An **actor–critic** uses a critic's prediction error to improve a policy. A **Markov decision process** specifies states, actions, transitions, and rewards; the Markov property requires the current state to contain the history needed for predicting transitions and rewards. A poor state representation can break an apparently adequate learning rule.

The **Bellman equation** decomposes current value into immediate reward and expected future value. **Policy iteration** alternates evaluation and improvement. Dopamine findings motivate prediction-error interpretations in the source; they do not prove that every dopamine signal, condition, or brain system implements a single scalar δ.

### Chapter 10 — Representational learning
**Locator:** §§10.1–10.5.

A **generative model** specifies a latent distribution and an observation process; a **recognition model** infers latent variables from observations. In the source's terminology, “causal models” can mean models that generate observations from latent causes. Fitting such a model does not establish intervention identification in Hernán–Robins's sense.

**Maximum-likelihood density estimation** learns parameters of an observation distribution. **Expectation maximization (EM)** alternates posterior inference about hidden variables with parameter updates. With approximate recognition distributions, optimization can improve a variational lower bound without maximizing the exact likelihood; local optima and approximation quality remain consequential.

**Mixtures of Gaussians** represent discrete latent classes; **k-means** is a restrictive clustering limit. **Factor analysis** includes latent factors and observation noise; **PCA** selects variance-preserving directions under its objective. **Sparse coding** favors representations with few active causes; **ICA** seeks statistically independent sources under its generative assumptions. **Helmholtz machines** combine generative and recognition pathways with approximate learning. Similar-looking basis functions can arise under different priors and objectives and are not, by resemblance alone, identified biological components.

## Worked Example — blocking through the Rescorla–Wagner model
**Reconstruction:** §9.2 and its conditioning table, using a unit reward and an idealized asymptotic state; this is an algebraic teaching case, not new data.

Train cue A alone with reward r=1 until its weight approaches `wA=1`. Introduce cue B with initial `wB=0`, and present A+B with the same reward. With both cue indicators one, the model predicts `v=wA+wB=1`; hence `δ=r−v=0` and `ΔwB=ηBδ=0`. B is paired with reward but acquires no additional value at this exact limit. If pretraining is incomplete, some positive error remains and blocking is partial. If the compound produces a larger reward, error returns and B can learn.

This worked case identifies the explanatory commitment: the learning signal is prediction error relative to the combined prediction, not mere co-occurrence. It neither proves a particular neural implementation nor covers every conditioning phenomenon. Temporal conditioning questions require the timing and state representation supplied by the TD extension.

## Decision Rules & Judgment

- Choose descriptive, mechanistic, or interpretive claims explicitly; do not infer an implementation from an optimization principle.
- Define the time window and rate statistic before comparing spike variability. Check the conditional distribution rather than declaring a process Poisson from its mean.
- For receptive fields, examine stimulus covariance and nonlinearities before interpreting a spike-triggered average as the filter.
- For an optimal decoder, state the prior, loss, response likelihood, and independence assumptions. Distinguish theoretical availability from demonstrated readout.
- Apply Fisher bounds with their bias and regularity conditions; report mean squared error separately from variance.
- Treat information estimates as functions of the stimulus ensemble, binning, word duration, and sampling. More entropy can be more noise.
- Match conductance, compartment, and rate-model detail to the question. Keep units, reset rules, boundary conditions, and numerical resolution explicit.
- Inspect dynamics and stability before calling a recurrent state a memory. Symmetry-dependent results do not automatically transfer to asymmetric circuits.
- A learning rule needs stability, competition, and access to its teaching information. An algebraically useful normalization is not already a verified biological process.
- In latent-variable models, preserve the distinction between statistical generation, inferred representation, and identified intervention effects.

## Key Takeaways
Encoding, decoding, information, dynamics, and learning answer connected but different questions. The mathematical foundation is strongest when its assumptions travel with every result: independence with Poisson decoding, loss with Bayesian optimality, bias with Fisher bounds, organization with stability, and learning constraints with plasticity.

**Coverage note:** All ten chapters are represented. Mathematical appendices are used for notation and limits but are not reproduced; long derivations, exercise solutions, and most numerical case studies are omitted. Retinotopic geometry, detailed channel kinetics, and individual map-development models are compressed. This draft does not establish current state of the art, modern deep-learning coverage, or physiological validation of every model.
