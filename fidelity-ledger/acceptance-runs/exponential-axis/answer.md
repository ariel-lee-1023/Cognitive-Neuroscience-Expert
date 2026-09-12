For **\(P(t)=0.8(0.9)^t\), use a linear horizontal time axis and a logarithmic vertical \(P\) axis**: a semilog-y plot. For **\(P(t)=0.8t^{-0.9}\), use logarithmic axes for both time and \(P\)**: a log-log plot.

Taking natural logarithms gives the transformations directly:

| Model | Transformation | Straight-line coordinates | Slope and intercept |
|---|---|---|---|
| Exponential | \(\ln P=\ln[0.8(0.9)^t]=\ln 0.8+t\ln 0.9\) | \(x=t,\ y=\ln P\) | Slope \(\ln 0.9<0\); intercept \(\ln 0.8\) |
| Power law | \(\ln P=\ln[0.8t^{-0.9}]=\ln 0.8-0.9\ln t\) | \(x=\ln t,\ y=\ln P\) | Slope \(-0.9\); intercept \(\ln 0.8\), corresponding to \(t=1\) |

Any logarithm base works if used consistently. Changing the base changes the exponential's numerical slope; the power-law slope remains \(-0.9\) when both logs use the same base. Logging **time alone** does not linearize the exponential. Indeed, on log-log coordinates with \(x=\ln t\), its equation becomes \(y=\ln 0.8+e^x\ln 0.9\), which is curved. Conversely, the power law is curved on semilog-y coordinates because \(\ln P=\ln 0.8-0.9\ln t\).

The models describe different regularities. Exponential decay loses the same **fraction per fixed time interval**: \(P(t+1)/P(t)=0.9\), giving a constant half-life \(\ln(1/2)/\ln(0.9)\). The power law loses the same fraction when time is **multiplied by a fixed factor**: \(P(ct)/P(t)=c^{-0.9}\). Its additional time to halve from age \(t\) is \((2^{1/0.9}-1)t\), which grows with age.

Logs require positive values. The exponential permits \(t=0\) on its linear time axis, where \(P=0.8\). The power law requires \(t>0\) and is undefined at zero. If \(P\) is literally a probability, its power-law domain must also exclude times where \(0.8t^{-0.9}>1\), for example by restricting the application to \(t\geq1\) in the stated time units.

**A straight-looking plot alone does not establish the better model.** Each specified curve is exactly straight under its own transformation. With observations, a short time range and noise can make competing curves look similar. Log transformation also changes the error structure: least squares on \(\ln P\) weights discrepancies differently from least squares on \(P\).

Compare the candidates against the same observations using a justified observation model, such as binomial likelihood for independent recall successes out of known trial counts. Inspect residual patterns and predictive performance on held-out data, especially across delays where the predictions diverge. Do not compare visual straightness or \(R^2\) values computed for different response transformations as though they were the same criterion. Even a predictive winner would not, by itself, identify the biological mechanism. No observations were supplied here, so these equations establish the appropriate axes, not an empirical winner.

The plotting and model-comparison principles follow the supplied Stocco reference's “shape of forgetting” discussion; the substitutions and contrasts above are direct algebraic derivations.
