High stimulus information means the cell's measured response can help distinguish the stimuli. It does not, by itself, establish how well the animal discriminates them.

First define “information”: assume mutual information between stimulus identity \(S\) and response \(R\), with a stated stimulus frequency, response feature (such as spike count or spike timing), and observation window. For two equally frequent stimuli, the maximum is 1 bit per response window. High firing rate or high response entropy alone does not imply high stimulus information. These distinctions follow Dayan and Abbott, Chapters 1 and 4 of the supplied reference.

To predict discrimination, we need the trial-to-trial response distributions \(p(r\mid s_0)\) and \(p(r\mid s_1)\), and a decision rule. An ideal observer compares their likelihood ratio against a threshold determined by stimulus priors and error costs. For equally likely stimuli and equal error costs, the minimum possible error using this response is

\[
P_e^*=\frac12\sum_r\min\{p(r\mid s_0),p(r\mid s_1)\}.
\]

Here the sum is over possible responses; use an integral for continuous responses. This is an analytic consequence of the likelihood-ratio framework in Chapter 3: error comes from the overlap of the two response distributions. Mutual information alone generally does not specify an exact percentage correct, though information near the binary maximum constrains ideal-observer error to be small.

Actual behavior additionally depends on whether downstream circuits access and use this response feature within the decision time, their readout rule, and added variability or lapses. Fit a decoder on training trials and assess its predictions on held-out trials under the same stimulus and timing conditions as the behavior. Matching neural and behavioral performance shows compatibility, not proof that this cell drives the decision. Population information also depends on redundancy, synergy, and conditional correlations; individual-cell information cannot simply be added. Evidence for the animal's readout needs additional behavioral and neural tests.

Limited trials affect both bias and precision. Empirical response probabilities miss rare responses and fluctuate across samples. Plug-in entropy estimates are generally biased downward. Because mutual information subtracts conditional entropy from total entropy, these biases do not reliably cancel: a naive information estimate is often biased upward, even when stimuli and responses are independent. The direction and size depend on the estimator and sampling regime; limited data do not guarantee upward bias in every realization.

This problem becomes severe with fine temporal bins or long spike words because the number of possible responses grows rapidly. To assess it, report trials per stimulus and response resolution; examine estimates across sample sizes and reasonable bin widths or word lengths; use an appropriate bias correction or regularized estimator; and quantify uncertainty. Label shuffling that respects trial dependence can reveal a finite-sample null baseline, but is not a universal bias correction. Resampling observed trials cannot establish the probabilities of responses never observed. If estimates remain unstable, collect more trials or simplify the response representation and acknowledge the information that simplification may discard.

Source: [Dayan and Abbott reference](../../../references/reference-dayan-abbott-theoretical-neuroscience.md), Chapters 3 and 4, supplied December 2000 draft summaries. The error expression and practical estimation checks above are analytic synthesis; no data or numerical information estimate were supplied or calculated.
