"""Run with python -m demos.run {reward,accumulation,timing,all}."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from .models import (reward_values, recovery_curve, ddm, symmetric_ddm_moments,
                     timing_designs, contrast_info, response_kernel)


def save(fig, destination):
    fig.savefig(destination, dpi=160, facecolor="white")
    plt.close(fig)


def reward_demo(out, reward_path):
    rewards = np.loadtxt(reward_path, delimiter=",", skiprows=1, ndmin=1)
    alpha_values = [0, 0.1, 0.5, 1]
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), layout="constrained")
    ax = axes[0, 0]
    ax.step(np.arange(len(rewards)), rewards, where="post", color="0.7", label="supplied reward")
    for alpha in alpha_values:
        ax.plot(reward_values(rewards, alpha), label=f"alpha={alpha:g}")
    ax.set(xlabel="Trial / update", ylabel="Value or reward", title="Same external reward sequence; V0=0.5")
    ax.legend(ncol=2)
    seed, grid, truths, reps = 23, np.linspace(0.01, 0.99, 99), np.linspace(0.1, 0.9, 5), 30
    rng = np.random.default_rng(seed)
    recovery = {}
    for index, (name, length, sigma) in enumerate((("informative", len(rewards), 0.08), ("short and noisy", min(12, len(rewards)), 0.35))):
        stimulus = rewards[:length]
        recovered, target = [], []
        for truth in truths:
            expected = reward_values(stimulus, truth)[:-1]
            for _ in range(reps):
                observed = expected + rng.normal(0, sigma, length)
                curve = recovery_curve(stimulus, observed, grid, sigma)
                recovered.append(float(grid[np.argmin(curve)]))
                target.append(float(truth))
        ax = axes[0, 1] if index == 0 else axes[1, 0]
        ax.scatter(target, recovered, alpha=0.25, s=14)
        ax.plot([0, 1], [0, 1], "k--", lw=1)
        mae = float(np.mean(np.abs(np.array(recovered) - target)))
        ax.set(xlabel="Generating alpha", ylabel="Grid ML estimate", xlim=(0, 1), ylim=(0, 1),
               title=f"{name}: n={length}, sigma={sigma}; MAE={mae:.3f}")
        recovery[name] = dict(n=length, sigma=sigma, mae=mae, truths=target, estimates=recovered)
    constant = np.full(len(rewards), 0.5)
    observations = 0.5 + rng.normal(0, 0.08, len(rewards))
    curve = recovery_curve(constant, observations, grid, 0.08)
    axes[1, 1].plot(grid, curve - curve.min())
    axes[1, 1].set(xlabel="Candidate alpha", ylabel="NLL minus minimum", ylim=(-0.1, 1),
                   title="r=V0=0.5: alpha is unidentifiable")
    fig.suptitle("Illustrative reward learning and Gaussian value observations (not empirical data)")
    save(fig, out / "reward.png")
    return dict(seed=seed, observation_model="y[t] ~ Normal(V[t], sigma^2), pre-update; known sigma and V0",
                reward_sha256=hashlib.sha256(reward_path.read_bytes()).hexdigest(), rewards=rewards.tolist(),
                initial=0.5, alpha_values=alpha_values, grid=grid.tolist(), replicates=reps,
                recovery=recovery, flat_nll_range=float(np.ptp(curve)),
                limitations="One parameter, known observation noise and initial value; grid estimates are not clinical validation. No estimate is reported for the flat likelihood.")


def ddm_summary(choice, rt, settings):
    finished = choice != 0
    n = len(choice)
    return dict(settings=settings, n=n, upper_all=float(np.mean(choice == 1)),
                lower_all=float(np.mean(choice == -1)), unfinished=float(np.mean(~finished)),
                upper_given_finished=float(np.mean(choice[finished] == 1)) if finished.any() else None,
                mean_rt_finished=float(np.mean(rt[finished])) if finished.any() else None,
                median_rt_finished=float(np.median(rt[finished])) if finished.any() else None)


def accumulation_demo(out):
    base = dict(drift=0.4, boundary=1., noise=1., start=0., nondecision=0.25,
                dt=0.002, horizon=5., trials=4000, seed=17)
    configurations = [("baseline", {}), ("higher drift", {"drift": 1.0}),
                      ("wider boundary", {"boundary": 1.4}), ("upper start bias", {"start": 0.35})]
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), layout="constrained")
    reports = {}
    bins = np.linspace(0, base["horizon"] + base["nondecision"], 55)
    for ax, (name, changes) in zip(axes.flat, configurations):
        settings = base | changes
        choice, rt = ddm(**settings)
        report = ddm_summary(choice, rt, settings)
        reports[name] = report
        for label, code in (("upper", 1), ("lower", -1)):
            data = rt[choice == code]
            ax.hist(data, bins=bins, weights=np.full(len(data), 1 / len(choice)), histtype="step", label=label)
        ax.set(xlabel="Response time (s)", ylabel="Fraction of all trials / bin",
               title=f"{name}: v={settings['drift']}, a={settings['boundary']}, x0={settings['start']}\nP(upper)={report['upper_all']:.2f}, unfinished={report['unfinished']:.2%}")
        ax.legend()
    fig.suptitle("Illustrative diffusion: dx=v dt + s dW; s=1, dt=0.002 s, Tnd=0.25 s")
    save(fig, out / "accumulation.png")
    sensitivity = []
    for dt in (0.004, 0.002, 0.001):
        settings = base | dict(dt=dt, trials=8000, horizon=12.)
        choice, rt = ddm(**settings)
        row = ddm_summary(choice, rt, settings)
        row["upper_mc_se"] = float(np.sqrt(row["upper_all"] * (1 - row["upper_all"]) / len(choice)))
        finished_rt = rt[np.isfinite(rt)]
        row["mean_rt_mc_se"] = float(np.std(finished_rt, ddof=1) / np.sqrt(len(finished_rt)))
        sensitivity.append(row)
    p, mean = symmetric_ddm_moments(base["drift"])
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    for ax, key, error, target, label in ((axes[0], "upper_all", "upper_mc_se", p, "P(upper), all trials"),
                                            (axes[1], "mean_rt_finished", "mean_rt_mc_se", mean + base["nondecision"], "Mean RT, finished (s)")):
        axes_dt = [row["settings"]["dt"] for row in sensitivity]
        ax.errorbar(axes_dt, [row[key] for row in sensitivity], yerr=[1.96 * row[error] for row in sensitivity], fmt="o-", capsize=4)
        ax.axhline(target, color="k", ls="--", label="continuous, no deadline")
        ax.set(xlabel="Time step (s)", ylabel=label)
        ax.legend()
    fig.suptitle("Resolution check: 8,000 trials per step; bars = 1.96 Monte Carlo SE")
    save(fig, out / "accumulation-resolution.png")
    return dict(configurations=reports, sensitivity=sensitivity,
                analytic_no_deadline=dict(upper=p, mean_rt=mean+base["nondecision"]),
                limitations="Euler grid crossings overshoot boundaries. Resolution runs are not paired Brownian paths. Monte Carlo intervals do not cover discretization bias; finite deadlines censor trials. Patterns do not identify a neural mechanism.")


def timing_demo(out):
    settings = dict(seed=41, dt=0.1, tr=1., duration=240.)
    designs = timing_designs(**settings)
    contrasts = {"A-B": [1, -1, 0], "A+B": [1, 1, 0]}
    reports = {}
    fig, axes = plt.subplots(3, 3, figsize=(13, 10), layout="constrained")
    for row, (name, item) in enumerate(designs.items()):
        x = item["design"]
        for column, label in enumerate(("A", "B")):
            axes[row, 0].plot(item["time"], item["inputs"][:, column], label=label, alpha=0.75)
            axes[row, 1].plot(item["sampled_time"], x[:, column], label=label, alpha=0.75)
        axes[row, 0].set(title=name+": inputs", xlabel="Time (s)", ylabel="Input / s")
        axes[row, 1].set(title="Convolved, sampled at TR=1 s", xlabel="Time (s)", ylabel="Assumed response")
        for ax in axes[row, :2]: ax.legend()
        picture = axes[row, 2].imshow(x, aspect="auto", origin="upper", cmap="viridis", interpolation="nearest")
        axes[row, 2].set(xticks=[0, 1, 2], xticklabels=["A", "B", "intercept"], ylabel="Sample index", title="Design matrix (actual scale)")
        fig.colorbar(picture, ax=axes[row, 2], shrink=0.7)
        results = {label: contrast_info(x, c) for label, c in contrasts.items()}
        reports[name] = dict(contrasts=results, input_area=(item["inputs"].sum(axis=0)*settings["dt"]).tolist(),
                             regressor_correlation=float(np.corrcoef(x[:, :2].T)[0, 1]))
        np.savetxt(out / (name.replace(" ", "-") + "-matrix.csv"), x, delimiter=",", header="A,B,intercept", comments="")
    fig.suptitle("Illustrative linear convolution: unit-area double gamma; iid noise sigma=1")
    save(fig, out / "timing.png")
    # Preserve an estimable contrast while approaching exact dependence.
    x = designs["jittered events"]["design"]
    epsilons = [1., .1, .01, .001, 0.]
    near = []
    for eps in epsilons:
        modified = x.copy()
        modified[:, 1] = x[:, 0] + eps * (x[:, 1] - x[:, 0])
        near.append(dict(epsilon=eps, **contrast_info(modified, contrasts["A-B"])))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    kernel_time, kernel = response_kernel(settings["dt"])
    axes[0].plot(kernel_time, kernel)
    axes[0].set(xlabel="Time after unit input (s)", ylabel="Response / s", title="Assumed response kernel, area=1")
    axes[1].loglog(epsilons[:-1], [row["variance"] for row in near[:-1]], "o-")
    axes[1].set(xlabel="Distinct component in regressor B (epsilon)", ylabel="Variance of A-B estimate", title="Estimable can still mean poor precision")
    axes[1].text(.05, .08, "epsilon=0: A-B not estimable\nNo pseudoinverse variance reported", transform=axes[1].transAxes)
    save(fig, out / "timing-precision.png")
    return dict(settings=settings, contrasts=contrasts, designs=reports, near_confounding=near,
                response="Gamma(shape=6,scale=1s) - Gamma(shape=16,scale=1s)/6; unit integral, 32s support",
                limitations="Known linear time-invariant HRF; iid Gaussian noise sigma=1; intercept only, no filtering, drift or autocorrelation. Equal input areas do not match temporal structure. These schedules do not isolate the causal effect of jitter or optimize a real study.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("demo", choices=["reward", "accumulation", "timing", "all"])
    parser.add_argument("--out", type=Path, default=Path("outputs"))
    parser.add_argument("--rewards", type=Path, default=Path(__file__).parent / "data" / "rewards.csv")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    functions = {"reward": lambda: reward_demo(args.out, args.rewards),
                 "accumulation": lambda: accumulation_demo(args.out), "timing": lambda: timing_demo(args.out)}
    for name in functions if args.demo == "all" else [args.demo]:
        result = functions[name]()
        result["runtime"] = dict(python=platform.python_version(), numpy=np.__version__, matplotlib=matplotlib.__version__)
        result["status"] = "executed illustrative simulation, not empirical data"
        (args.out / f"{name}.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
        print(f"{name}: figures and settings written to {args.out}")


if __name__ == "__main__":
    main()
