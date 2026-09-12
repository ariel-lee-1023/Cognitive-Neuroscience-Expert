import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out = Path(__file__).resolve().parent
n=100
sigma=1.0
t=np.arange(n)
a=np.sqrt(2)*np.sin(2*np.pi*t/n)
z=np.sqrt(2)*np.cos(2*np.pi*t/n)
c=np.array([1.,-1.,0.])
rhos=np.linspace(0,.999,1000)
variances=[]
for rho in rhos:
    b=rho*a+np.sqrt(1-rho*rho)*z
    X=np.column_stack([a,b,np.ones(n)])
    variances.append(sigma**2*np.sum((c@np.linalg.pinv(X))**2))
assert np.allclose(variances,2*sigma**2/(n*(1-rhos)))
records=[]
for rho in [0,.9,.99,.999,1.]:
    b=rho*a+np.sqrt(1-rho*rho)*z
    X=np.column_stack([a,b,np.ones(n)])
    estimable=bool(np.allclose(c,c@np.linalg.pinv(X)@X))
    records.append({'rho':rho,'rank':int(np.linalg.matrix_rank(X)),'estimable_A_minus_B':estimable,'variance':float(sigma**2*np.sum((c@np.linalg.pinv(X))**2)) if estimable else None,'standard_error':float(np.sqrt(sigma**2*np.sum((c@np.linalg.pinv(X))**2))) if estimable else None})
fig,axs=plt.subplots(1,2,figsize=(10,4),layout='constrained')
rho=.99
axs[0].plot(t,a,label='A')
axs[0].plot(t,rho*a+np.sqrt(1-rho*rho)*z,label='B',linestyle='--')
axs[0].set(xlabel='Sample index',ylabel='Regressor value (arbitrary units)',title='Two distinct but similar columns: r = 0.99')
axs[0].legend()
axs[1].semilogy(rhos,np.sqrt(variances),color='#22618a')
for r in records[:-1]:
    axs[1].scatter(r['rho'],r['standard_error'],color='#22618a')
axs[1].axvline(1,color='#b44c3f',linestyle=':')
axs[1].set(xlabel='Correlation between A and B',ylabel='Standard error of A - B',title='Precision falls before rank is lost',xlim=(-.02,1.03))
axs[1].text(.97,.2,'r = 1: A - B not estimable',rotation=90,ha='right',color='#b44c3f')
fig.suptitle('Executed illustrative GLM calculation | n = 100, noise SD = 1')
fig.savefig(out/'representation.png',dpi=160)
(out/'representation-numbers.json').write_text(json.dumps({'n':n,'sigma':sigma,'grid':{'min':0,'max':.999,'points':1000},'random_seed':None,'computation':'Deterministic linear algebra; no random sampling or time integration','numpy':np.__version__,'matplotlib':matplotlib.__version__,'records':records},indent=2))
print((out/'representation-numbers.json').read_text())
