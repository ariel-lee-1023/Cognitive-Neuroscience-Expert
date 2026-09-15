## Independent Poisson counts

Let (s) be a stimulus, (n_i) neuron (i)'s spike count in a fixed window (T), and (f_i(s)>0) its tuning curve in spikes per unit time. Assume

\[
n_i\mid s\sim\operatorname{Poisson}(\mu_i(s)),\qquad \mu_i(s)=Tf_i(s),
\]

with neurons independent **conditional on (s)**. Then

\[
p(\mathbf n\mid s)=\prod_i\frac{e^{-Tf_i(s)}[Tf_i(s)]^{n_i}}{n_i!}.
\]

Taking logarithms and discarding only terms independent of (s), the maximum-likelihood decoder is

\[
\boxed{\hat s_{\rm ML}=\arg\max_s\left\{\sum_i n_i\log f_i(s)-T\sum_i f_i(s)\right\}.}
\]

The first term rewards stimuli that predict high rates in neurons that fired. The second penalizes predicted spikes that did not materialize: silence is evidence too. Drop that second term only if the summed tuning curves are constant across candidate stimuli.

For differentiable tuning curves and a scalar stimulus, an interior optimum satisfies

\[
0=\sum_i\left[\frac{n_i}{f_i(s)}-T\right]f_i'(s).
\]

This need not have a unique solution; evaluate candidate maxima and boundaries, or maximize directly on a stimulus grid. The derivation treats tuning curves as known; in applications, estimate them using separate training data and assess decoding on held-out trials.

For two candidate stimuli, the log-likelihood ratio becomes

\[
\log\frac{p(\mathbf n\mid s_1)}{p(\mathbf n\mid s_0)}
=\sum_i n_i\log\frac{f_i(s_1)}{f_i(s_0)}
-T\sum_i[f_i(s_1)-f_i(s_0)].
\]

Thus independent Poisson discrimination uses a weighted sum of counts plus an offset. Equal priors and equal error costs give threshold zero. A prior adds (\log p(s)) to obtain MAP decoding; minimizing squared reconstruction error instead gives the posterior mean. “Optimal” depends on the decision criterion.

## What shared variability changes

Two neurons can covary simply because both prefer the same stimuli. That does **not** violate conditional independence. The relevant dependence is residual covariation across repeated presentations of the same stimulus.

If that dependence exists, tuning curves and Poisson marginal distributions no longer specify the joint likelihood. Replace the product above with an appropriate (p(\mathbf n\mid s)); maximizing the independent product is then a potentially misspecified decoder. Covariance alone generally does not determine a count distribution either.

As an illustrative extension, suppose an unobserved trial-wide gain (g) multiplies all rates:

\[
p(\mathbf n\mid s)=\int p(g\mid s)
\prod_i\operatorname{Poisson}(n_i;Tg f_i(s))\,dg.
\]

Neurons are independent given both (s) and (g), but generally dependent after integrating out (g). Setting (E[g\mid s]=1) preserves the tuning means. This model usually produces overdispersed, non-Poisson marginals, so it changes that assumption as well. The decoder must distinguish population-wide gain fluctuations from stimulus-driven rate changes.

Shared variability is not uniformly harmful: its alignment with stimulus-induced response changes matters. For example, common fluctuations can obscure a stimulus encoded by a common increase, yet cancel when information resides in differences between neurons. Ignoring dependence can misweight evidence and miscalibrate uncertainty; whether it changes the selected stimulus or accuracy depends on the joint model and task.

**Source basis:** Dayan–Abbott, supplied December 2000 draft, Chapters 1 and 3, via [the local reference](../../../references/reference-dayan-abbott-theoretical-neuroscience.md). The shared-gain example is an illustrative derivation. A successful statistical decoder establishes available information, not the animal’s neural readout mechanism.
