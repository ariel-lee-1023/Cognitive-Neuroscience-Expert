import math,json
from pathlib import Path
results={}
# Verify independent Poisson log likelihood and Fisher information with finite sums.
s=.3;T=.4
f=lambda z: math.exp(z)+2
rate=f(s);slope=math.exp(s);mu=T*rate
prob=lambda n:math.exp(-mu)*mu**n/math.factorial(n)
J=sum(prob(n)*(n*slope/rate-T*slope)**2 for n in range(60))
expected=T*slope*slope/rate
assert abs(J-expected)<1e-12
results['poisson_fisher']={'summed_score_squared':J,'formula':expected,'absolute_error':abs(J-expected)}
# Synthetic binary confounding table: standardized/IPW identity, not empirical data.
pl=[.3,.7];pa=[.2,.8];means=[[.1,.4],[.2,.6]]
vals=[]
for a in (0,1):
 std=sum(pl[l]*means[a][l] for l in (0,1))
 ipw=sum(pl[l]*(pa[l] if a else 1-pa[l])*means[a][l]/(pa[l] if a else 1-pa[l]) for l in (0,1))
 assert abs(std-ipw)<1e-12;vals.append(std)
results['standardization_ipw']={'means_under_0_1':vals,'effect':vals[1]-vals[0]}
lam=.75;tau=.02;h=2;vstar=h/(1-lam)
assert abs(-vstar+h+lam*vstar)<1e-12
results['linear_recurrent_mode']={'fixed_point':vstar,'effective_time_constant':tau/(1-lam)}
# Oja norm derivative identity, arbitrary finite vectors.
u=[.2,-.4,1.2];w=[.3,.5,-.1];alpha=.8;v=sum(a*b for a,b in zip(u,w));dw=[v*x-alpha*v*v*y for x,y in zip(u,w)]
lhs=2*sum(a*b for a,b in zip(w,dw));rhs=2*v*v*(1-alpha*sum(x*x for x in w));assert abs(lhs-rhs)<1e-12
results['oja_norm_derivative']={'direct':lhs,'identity':rhs}
assert 1-(1+0)==0
results['blocking_limit']={'prediction_error':0,'new_cue_update':0}
results['scope']='Algebraic sanity checks of reconstructed formulas with synthetic values; no source-data replication, clinical claim, or behavioral evaluation.'
Path(__file__).with_name('equation-checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
