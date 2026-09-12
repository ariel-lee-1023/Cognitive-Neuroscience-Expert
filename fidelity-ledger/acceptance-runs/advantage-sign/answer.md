For the same policy \(\pi\), the advantage is

\[
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s)=6-4=2.
\]

Its positive sign means that taking action \(a\) in state \(s\), then following \(\pi\), has expected return 2 units above following \(\pi\) from \(s\). It does not mean that every trial produces a positive reward, or that this is the best available action. Negative advantage means below the policy baseline; zero means equal to it.

For an on-policy transition, sample \(a_t\sim\pi_\theta(\cdot\mid s_t)\), observe reward \(r_t\) and next state \(s_{t+1}\), and compute

\[
\delta_t=r_t+\gamma V_\phi(s_{t+1})-V_\phi(s_t),
\]

where \(\gamma\) is the discount factor and \(V_\phi\) is the critic's estimate. The bootstrap term is zero at a true terminal state. With exact \(V^\pi\) and a matching Markov environment,

\[
\mathbb E[\delta_t\mid s_t=s,a_t=a]
=Q^\pi(s,a)-V^\pi(s)=A^\pi(s,a).
\]

Thus the conditional expected TD error here is 2; its individual realized value cannot be calculated without the reward, discount, and next-state value. An approximate critic can bias this advantage estimate.

An elementary actor-critic uses the same TD error in two distinct updates:

\[
\begin{aligned}
\text{Tabular critic:}\quad
V(s_t)&\leftarrow V(s_t)+\alpha\delta_t,\\
\text{Stochastic actor:}\quad
\theta&\leftarrow\theta+\eta\delta_t\nabla_\theta\log\pi_\theta(a_t\mid s_t),
\end{aligned}
\]

with positive learning rates \(\alpha,\eta\). The critic adjusts the state-value estimate; the actor uses the TD error as a fixed sampled advantage signal for its policy-gradient step. A positive signal locally reinforces the selected action, and a negative signal discourages it.

**No: adding TD errors to a stored quantity called \(A(s,a)\) does not necessarily estimate advantage.** An update \(H(s,a)\leftarrow H(s,a)+\beta\delta_t\) accumulates signals and can serve as a policy-preference update. Under a fixed policy and exact critic, repeated visits to this pair have mean increment \(2\beta\); the stored value need not approach 2. Calling it \(A\) does not change that.

To estimate advantage directly under those fixed-policy assumptions, an averaging update would instead be

\[
\widehat A(s_t,a_t)\leftarrow\widehat A(s_t,a_t)
+\beta_t\bigl[\delta_t-\widehat A(s_t,a_t)\bigr],
\]

with suitable sampling and step sizes. Alternatively, estimate \(Q^\pi\) and \(V^\pi\) consistently and subtract them. A changing policy changes the target advantage too.

Source: the supplied [Stocco reference, actor-critic passage](../../../references/reference-stocco-explanatory-models.md), which explicitly labels these equations an editorial mathematical clarification rather than a verified transcription of Stocco's algorithm. The accumulation counterexample and averaging distinction above are algebraic reasoning from the stated definitions; no external source was checked.
