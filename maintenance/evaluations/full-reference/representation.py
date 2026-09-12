import json, math, platform
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
# Illustrative calculation, not observed BOLD or a fitted experimental design.
dt, tr, duration, sigma = 0.1, 1.0, 240.0, 1.0
t = np.arange(0, duration, dt)
ht = np.arange(0, 32, dt)
h = ht**5*np.exp(-ht)/math.factorial(5) - ht**15*np.exp(-ht)/(6*math.factorial(15))
h /= h.sum()*dt
onsets = [20, 60, 100, 140, 180]
def column(shift):
    u = np.zeros(t.size)
    for onset in onsets:
        u[(t >= onset + shift - 1e-9) & (t < onset + shift + 10 - 1e-9)] = 1
    x = (np.convolve(u, h)[:t.size]*dt)[::round(tr/dt)]
    x -= x.mean()
    return x/np.sqrt(np.mean(x*x))

x_a, x_b = column(0), column(1)
n = len(x_a)
X = np.column_stack([x_a, x_b, np.ones(n)])
c = np.array([1., -1., 0.])
rho = float(np.corrcoef(x_a, x_b)[0, 1])
variance = float(sigma**2 * np.sum((c@np.linalg.pinv(X))**2))
analytic = float(2*sigma**2/(n*(1-rho)))
assert np.isclose(variance, analytic)
duplicate = np.column_stack([x_a, x_a, np.ones(n)])
row_projector = np.linalg.pinv(duplicate)@duplicate
diff_error = float(np.linalg.norm(c-c@row_projector))
sum_c = np.array([1., 1., 0.])
sum_error = float(np.linalg.norm(sum_c-sum_c@row_projector))
assert diff_error > 1 and sum_error < 1e-10
assert np.linalg.matrix_rank(X) == 3
grid = np.linspace(0, 0.999, 1000)
se = np.sqrt(2*sigma**2/(n*(1-grid)))
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), constrained_layout=True)
axes[0].plot(np.arange(n)*tr, x_a, label='A: blocks starting at 20, 60, ... s', color='#176D9C')
axes[0].plot(np.arange(n)*tr, x_b, label='B: same schedule delayed 1 s', color='#D66B28', linestyle='--')
axes[0].set(xlabel='Time (s)', ylabel='Centered regressor, unit RMS', title=f'Convolved teaching design: r = {rho:.4f}')
axes[0].legend(fontsize=8, loc='upper right')
axes[1].semilogy(grid, se, color='#52525B')
axes[1].scatter([rho], [np.sqrt(variance)], color='#D66B28', zorder=3)
axes[1].annotate(f'Executed design\nSE = {np.sqrt(variance):.3f}', (rho, np.sqrt(variance)), xytext=(0.38, 0.65), textcoords='axes fraction', arrowprops={'arrowstyle':'->'}, fontsize=9)
axes[1].set(xlabel='Correlation r (equal column norm)', ylabel='Standard error of A - B', title='Precision worsens before identifiability fails', xlim=(0, 1))
axes[1].text(0.02, 0.04, 'At r = 1: A - B is not estimable', transform=axes[1].transAxes, fontsize=9)
for ax in axes:
    ax.grid(alpha=.18)
fig.suptitle('Illustrative calculation, not observed fMRI data | n = 240, iid noise SD = 1', fontsize=12)
fig.savefig(out/'representation.png', dpi=180)
metrics = dict(n=n, dt=dt, tr=tr, duration=duration, sigma=sigma, onsets=onsets, block_duration=10, shift=1,
    rho=rho, rank=int(np.linalg.matrix_rank(X)), contrast_variance=variance, contrast_se=float(np.sqrt(variance)),
    analytic_variance=analytic, orthogonal_se=float(np.sqrt(2/n)), duplicate_rank=int(np.linalg.matrix_rank(duplicate)),
    duplicate_difference_rowspace_error=diff_error, duplicate_sum_rowspace_error=sum_error,
    random_seed=None, stochastic_simulation=False, python=platform.python_version(), numpy=np.__version__, matplotlib=matplotlib.__version__)
(out/'representation-metrics.json').write_text(json.dumps(metrics, indent=2))
print(json.dumps(metrics, indent=2))
