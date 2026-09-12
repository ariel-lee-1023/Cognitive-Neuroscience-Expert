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
# Standard advantage and exact-critic TD identity in a continuing one-state MDP.
# The transition returns to the same state; policy is fixed during this check.
policy = [.25, .75]
rewards = [1., 3.]
gamma = .5
v = sum(p*r for p,r in zip(policy,rewards))/(1-gamma)
q = [r+gamma*v for r in rewards]
advantage = [x-v for x in q]
td = [r+gamma*v-v for r in rewards]
assert all(abs(a-d)<1e-12 for a,d in zip(advantage,td))
assert advantage[0]<0<advantage[1]
assert abs(sum(p*a for p,a in zip(policy,advantage)))<1e-12
# For a softmax actor, a small positive-advantage policy-gradient step
# increases probability of the selected action, not a stored advantage table.
logits = [math.log(p) for p in policy]
selected = 1
updated = [z+.1*advantage[selected]*((1 if j==selected else 0)-policy[j]) for j,z in enumerate(logits)]
weights = [math.exp(z) for z in updated]
new_policy = [w/sum(weights) for w in weights]
assert new_policy[selected]>policy[selected]
results['advantage_td_actor'] = dict(policy=policy, rewards=rewards, gamma=gamma, state_value=v, action_values=q, advantages=advantage, conditional_td=td, policy_weighted_advantage=sum(p*a for p,a in zip(policy,advantage)), selected_action=selected, updated_policy=new_policy, conditions='Fixed on-policy continuing one-state MDP with exact critic; no general claim for approximate critics or arbitrary finite updates.')
# Exponential is straight in log-response / linear-time; power in log/log.
times = [1.,2.,4.,8.]
a=.8;b=.9
log_exponential=[math.log(a*b**t) for t in times]
log_power=[math.log(a*t**(-b)) for t in times]
exp_slopes=[(y2-y1)/(t2-t1) for t1,t2,y1,y2 in zip(times,times[1:],log_exponential,log_exponential[1:])]
power_slopes=[(y2-y1)/(math.log(t2)-math.log(t1)) for t1,t2,y1,y2 in zip(times,times[1:],log_power,log_power[1:])]
wrong_slopes=[(a*b**t2-a*b**t1)/(math.log(t2)-math.log(t1)) for t1,t2 in zip(times,times[1:])]
assert all(abs(s-math.log(b))<1e-12 for s in exp_slopes)
assert all(abs(s+b)<1e-12 for s in power_slopes)
assert max(wrong_slopes)-min(wrong_slopes)>.01
results['decay_axes'] = dict(times=times, exponential_log_y_linear_t_slopes=exp_slopes, expected_exponential_slope=math.log(b), power_log_log_slopes=power_slopes, expected_power_slope=-b, exponential_linear_y_log_t_slopes=wrong_slopes, conditions='a>0, 0<b<1, positive times and responses; algebraic transformations, not fitted evidence.')
results['scope']='Algebraic sanity checks of reconstructed formulas with synthetic values; no source-data replication, clinical claim, or behavioral evaluation.'
Path(__file__).with_name('equation-checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
