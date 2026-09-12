For independent Poisson counts, the likelihood decoder chooses the stimulus whose tuning curves make the observed population response most probable. Shared variability requires a **joint response model**: the tuning curves alone no longer specify the likelihood.

Let \(s\) be a static stimulus, \(n_i\) the spike count of neuron \(i\) in a fixed window \(T\), and \(f_i(s)\) its tuning curve in spikes per unit time. Define the dimensionless expected count \(\mu_i(s)=T f_i(s)\). Assume the tuning curves are known and

\[
n_i\mid s\sim\operatorname{Poisson}(\mu_i(s)),\qquad
p(\mathbf n\mid s)=\prod_{i=1}^N p(n_i\mid s).
\]

The second assumption is independence **conditional on the stimulus**, not independence after pooling different stimuli.

The product likelihood is

\[
p(\mathbf n\mid s)=\prod_i
\frac{e^{-\mu_i(s)}\mu_i(s)^{n_i}}{n_i!}.
\]

Taking logs turns the product into a sum:

\[
\ell(s)=\sum_i\left[n_i\log\mu_i(s)-\mu_i(s)-\log(n_i!)\right].
\]

The factorial terms do not depend on the candidate stimulus, so the maximum-likelihood estimate is

\[
\boxed{\hat s_{\mathrm{ML}}
=\arg\max_s\sum_i\left[n_i\log\mu_i(s)-\mu_i(s)\right].}
\]

The first term rewards candidate stimuli that predict firing in the neurons that fired. The second penalizes predicted spikes that did not occur: silent neurons also contribute evidence. It can be dropped only if the total expected count \(\sum_i\mu_i(s)\) is constant across candidates. If \(\mu_i(s)=0\) but \(n_i>0\), that candidate has zero likelihood; use the limiting convention \(0\log0=0\) when both are zero.

For discrete stimuli, evaluate this score for each candidate. For a continuous scalar stimulus and positive differentiable rates, an interior optimum satisfies

\[
\frac{\partial\ell}{\partial s}
=\sum_i[n_i-\mu_i(s)]\frac{\mu_i'(s)}{\mu_i(s)}
=\sum_i[n_i-Tf_i(s)]\frac{f_i'(s)}{f_i(s)}=0.
\]

A root need not be the global maximum, so compare competing extrema and boundaries. For two stimuli, the log likelihood ratio becomes a linear function of counts:

\[
\log\frac{p(\mathbf n\mid s_1)}{p(\mathbf n\mid s_0)}
=\sum_i n_i\log\frac{f_i(s_1)}{f_i(s_0)}
-T\sum_i[f_i(s_1)-f_i(s_0)].
\]

With equal priors and equal error costs, choose \(s_1\) when this is positive. For a prior \(p(s)\), MAP decoding adds \(\log p(s)\) to the score. Other losses give other decisions: squared-error loss selects the posterior mean, not generally ML or MAP. These results decode counts; using spike timing would require an appropriate spike-train likelihood.

Shared variability changes the factorization, not the principle of maximizing a likelihood. Distinguish two kinds of covariation:

- **Signal covariation:** neurons respond similarly as the stimulus changes. This is compatible with conditional independence.
- **Noise covariation:** responses covary across repetitions of the same stimulus. Nonzero conditional covariance violates the independent model; zero covariance alone does not establish independence.

One illustrative joint model introduces an unobserved shared state \(z\), such as a fluctuating gain:

\[
p(\mathbf n\mid s)
=\int p(z\mid s)\prod_i
\operatorname{Poisson}\!\left(n_i;\mu_i(s,z)\right)\,dz.
\]

Counts are independent given both \(s\) and \(z\), but generally dependent after integrating out \(z\). The tuning means satisfy \(E_z[\mu_i(s,z)]=Tf_i(s)\). Under this model,

\[
\operatorname{Cov}(n_i,n_j\mid s)
=\delta_{ij}E_z[\mu_i(s,z)]
+\operatorname{Cov}_z(\mu_i(s,z),\mu_j(s,z)).
\]

This mixture generally also makes individual counts non-Poisson. It is a proposed extension, not a consequence of knowing the tuning curves. If Poisson marginals must be retained, a different joint model can be specified; those marginals still do not determine its dependence structure.

To see why the *pattern* of sharing matters, consider an explicitly approximate multivariate Gaussian count model with mean \(\boldsymbol\mu(s)\) and positive-definite covariance \(\Sigma(s)\). Its log likelihood, up to a stimulus-independent constant, is

\[
\ell_G(s)=-\tfrac12(\mathbf n-\boldsymbol\mu(s))^\top
\Sigma(s)^{-1}(\mathbf n-\boldsymbol\mu(s))
-\tfrac12\log\det\Sigma(s).
\]

The decoder discounts deviations along noisy population directions and gives more weight to reliable directions. If covariance varies with stimulus, its determinant term cannot generally be discarded. This approximation is most plausible when counts are sufficiently large; covariance alone does not specify an exact joint count likelihood.

For example, a common fluctuation in two neurons interferes with distinguishing stimuli that raise both means together. If the stimulus instead raises one mean and lowers the other, taking their difference can cancel that common fluctuation. Thus correlations do not universally reduce information; their effect depends on their alignment with stimulus-dependent response changes and on the comparison being made. Ignoring them can double-count evidence, miscalibrate uncertainty, and reduce decoding accuracy, though some decision boundaries may remain unchanged.

The independent model's local Fisher information is

\[
J(s)=E[(\partial_s\ell)^2]
=\sum_i\frac{\mu_i'(s)^2}{\mu_i(s)}
=T\sum_i\frac{f_i'(s)^2}{f_i(s)}.
\]

This follows because conditional count variances equal their means and the cross-covariances vanish. With shared variability, derive Fisher information from the **joint** likelihood; simply inserting correlated counts into the independent score does not produce the true information. The bound \(\operatorname{Var}(\hat s\mid s)\ge1/J(s)\) requires an unbiased estimator and regularity conditions, and need not be attained.

In data, fit tuning and variability models on training trials and compare likelihood calibration and decoding on held-out, simultaneously recorded trials. A successful analyst's decoder demonstrates accessible information under its assumptions; it does not establish that the animal uses that readout.

Source basis: the independent Poisson likelihood, ML/MAP distinction, and Fisher expression follow the supplied [Dayan–Abbott reference, Chapters 1 and 3](../../../references/reference-dayan-abbott-theoretical-neuroscience.md). The latent-state and Gaussian examples are analytic extensions illustrating its requirement to specify a joint distribution. No empirical data, numerical simulation, or external verification was used.
