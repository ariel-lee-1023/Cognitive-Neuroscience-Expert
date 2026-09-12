"""Reusable calculations. No plotting, file writes, or implicit random state."""
from math import factorial
import numpy as np


def finite_scalar(value, name, low=None, high=None, strict_low=False):
    if not np.isscalar(value) or not np.isfinite(value):
        raise ValueError(f"{name} must be a finite scalar")
    if low is not None and (value <= low if strict_low else value < low):
        raise ValueError(f"{name} outside allowed range")
    if high is not None and value > high:
        raise ValueError(f"{name} outside allowed range")


def vector(values, name):
    result = np.asarray(values, dtype=float)
    if result.ndim != 1 or not len(result) or not np.isfinite(result).all():
        raise ValueError(f"{name} must be a nonempty finite vector")
    return result


def integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, (int, np.integer)) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def reward_values(rewards, alpha, initial=0.5):
    """V[t+1] = V[t] + alpha*(r[t]-V[t]); return initial plus updates."""
    rewards = vector(rewards, "rewards")
    finite_scalar(alpha, "alpha", 0, 1)
    finite_scalar(initial, "initial")
    values = np.empty(len(rewards) + 1)
    values[0] = initial
    for t, reward in enumerate(rewards):
        values[t + 1] = values[t] + alpha * (reward - values[t])
    return values


def recovery_curve(rewards, observations, grid, sigma, initial=0.5):
    """Gaussian observation y[t] ~ N(V[t], sigma^2), BEFORE reward t.

    Sigma and initial value are fixed and known. Return full Gaussian NLL.
    A flat curve means no information about alpha, not successful recovery.
    """
    rewards = vector(rewards, "rewards")
    observations = vector(observations, "observations")
    grid = vector(grid, "grid")
    finite_scalar(sigma, "sigma", 0, strict_low=True)
    if len(rewards) != len(observations):
        raise ValueError("one pre-update observation per reward is required")
    predictions = np.array([reward_values(rewards, a, initial)[:-1] for a in grid])
    return 0.5 * np.sum(((observations - predictions) / sigma) ** 2, axis=1) + len(rewards) * np.log(sigma * np.sqrt(2 * np.pi))


def ddm(*, drift=0.7, boundary=1.0, noise=1.0, start=0.0,
        nondecision=0.25, dt=0.002, horizon=5.0, trials=3000, seed=17):
    """Euler first passage for dx=v dt+s dW; absorbing bounds +/-boundary.

    No between-step bridge correction. First sampled crossing time is used.
    Choice +1/-1 is boundary hit; choice 0 and RT NaN mark deadline censoring.
    Horizon is accumulation time, excluding nondecision time.
    """
    for name, value in (("drift", drift), ("start", start)):
        finite_scalar(value, name)
    for name, value in (("boundary", boundary), ("noise", noise), ("dt", dt), ("horizon", horizon)):
        finite_scalar(value, name, 0, strict_low=True)
    finite_scalar(nondecision, "nondecision", 0)
    integer(trials, "trials")
    integer(seed, "seed", 0)
    if abs(start) >= boundary or dt > horizon:
        raise ValueError("start must be inside bounds and dt <= horizon")
    steps = round(horizon / dt)
    if not np.isclose(steps * dt, horizon, rtol=0, atol=1e-10):
        raise ValueError("horizon must be an integer multiple of dt")
    rng = np.random.default_rng(seed)
    x = np.full(trials, start, dtype=float)
    choice = np.zeros(trials, dtype=int)
    rt = np.full(trials, np.nan)
    for step in range(1, steps + 1):
        active = np.flatnonzero(choice == 0)
        if not len(active):
            break
        x[active] += drift * dt + noise * np.sqrt(dt) * rng.standard_normal(len(active))
        hit = active[np.abs(x[active]) >= boundary]
        choice[hit] = np.where(x[hit] > 0, 1, -1)
        rt[hit] = step * dt + nondecision
    return choice, rt


def symmetric_ddm_moments(drift, boundary=1.0, noise=1.0):
    """Infinite-deadline continuous-time P(upper) and mean decision time; x0=0."""
    finite_scalar(drift, "drift")
    finite_scalar(boundary, "boundary", 0, strict_low=True)
    finite_scalar(noise, "noise", 0, strict_low=True)
    scaled = drift * boundary / noise ** 2
    p_upper = (1 + np.tanh(scaled)) / 2
    mean = boundary ** 2 / noise ** 2 if abs(scaled) < 1e-10 else boundary / drift * np.tanh(scaled)
    return p_upper, mean


def response_kernel(dt=0.1, support=32.0):
    """Illustrative unit-area double gamma h=Gamma(6,1)-Gamma(16,1)/6.

    Shape parameters are integers, scale is 1 second. This is an assumed
    linear response, not an estimated participant-specific HRF.
    """
    finite_scalar(dt, "dt", 0, strict_low=True)
    finite_scalar(support, "support", 0, strict_low=True)
    if dt >= support:
        raise ValueError("dt must be smaller than support")
    time = np.arange(0, support + dt / 2, dt)
    h = np.exp(-time) * (time ** 5 / factorial(5) - time ** 15 / factorial(15) / 6)
    return time, h / (h.sum() * dt)


def convolve_signal(signal, kernel, dt):
    signal, kernel = vector(signal, "signal"), vector(kernel, "kernel")
    finite_scalar(dt, "dt", 0, strict_low=True)
    return np.convolve(signal, kernel)[:len(signal)] * dt


def contrast_info(design, contrast, sigma=1.0, rtol=1e-10):
    """Estimability and variance under iid Gaussian noise with known sigma.

    A contrast is estimable iff it lies in row(X). For such contrasts,
    Var(c'beta_hat)=sigma^2 * ||c'X+||^2. Never interpret a pseudoinverse
    variance for a non-estimable contrast. rtol is numerical, not scientific.
    """
    design = np.asarray(design, dtype=float)
    contrast = vector(contrast, "contrast")
    finite_scalar(sigma, "sigma", 0, strict_low=True)
    finite_scalar(rtol, "rtol", 0, 1, strict_low=True)
    if design.ndim != 2 or min(design.shape) == 0 or not np.isfinite(design).all() or design.shape[1] != len(contrast):
        raise ValueError("finite design matrix and matching contrast required")
    singular = np.linalg.svd(design, compute_uv=False)
    cutoff = rtol * singular[0]
    rank = int(np.sum(singular > cutoff))
    pinv = np.linalg.pinv(design, rcond=rtol)
    residual = float(np.linalg.norm(contrast - contrast @ pinv @ design))
    estimable = residual <= rtol * max(1.0, float(np.linalg.norm(contrast)))
    variance = float(sigma ** 2 * np.sum((contrast @ pinv) ** 2)) if estimable else None
    return dict(rank=rank, columns=design.shape[1], estimable=bool(estimable),
                projection_error=residual, variance=variance,
                singular_values=singular.tolist(), rtol=rtol, sigma=sigma)


def timing_designs(seed=41, dt=0.1, tr=1.0, duration=240.0):
    """Fixed 10 s blocks, jittered unit-area events, and duplicate regressors.

    Each non-confounded design supplies 30 input-area units per condition.
    Different temporal structures mean this is not an isolated jitter effect.
    """
    integer(seed, "seed", 0)
    for name, value in (("dt", dt), ("tr", tr), ("duration", duration)):
        finite_scalar(value, name, 0, strict_low=True)
    if duration < 240 or dt > 1 or not np.isclose(tr / dt, round(tr / dt)) or not np.isclose(duration / dt, round(duration / dt)):
        raise ValueError("duration >=240, dt <=1, and integral sampling ratios required")
    time = np.arange(round(duration / dt)) * dt
    block = np.zeros((len(time), 2))
    for column, starts in enumerate(([10, 90, 170], [50, 130, 210])):
        for onset in starts:
            block[(time >= onset) & (time < onset + 10), column] = 1
    rng = np.random.default_rng(seed)
    onsets = np.cumsum(rng.uniform(2.0, 4.5, 60)) + 5
    conditions = np.repeat([0, 1], 30)
    rng.shuffle(conditions)
    event = np.zeros_like(block)
    for onset, column in zip(onsets, conditions):
        event[round(onset / dt), column] += 1 / dt
    confounded = np.column_stack([event[:, 0], event[:, 0]])
    _, kernel = response_kernel(dt)
    stride = round(tr / dt)
    result = {}
    for name, inputs in (("fixed block", block), ("jittered events", event), ("confounded events", confounded)):
        regressors = np.column_stack([convolve_signal(inputs[:, c], kernel, dt)[::stride] for c in range(2)])
        design = np.column_stack([regressors, np.ones(len(regressors))])
        result[name] = dict(time=time, inputs=inputs, sampled_time=time[::stride], design=design)
    return result
