import unittest
from pathlib import Path
import tempfile
import json
import numpy as np
from demos.models import (reward_values, recovery_curve, ddm, symmetric_ddm_moments,
                          response_kernel, convolve_signal, contrast_info, timing_designs)


class RewardTests(unittest.TestCase):
    def test_limits_and_geometric_solution(self):
        rewards = [0, 1, 0.2, 0.8]
        np.testing.assert_array_equal(reward_values(rewards, 0), np.full(5, 0.5))
        np.testing.assert_allclose(reward_values(rewards, 1)[1:], rewards)
        expected = 1 - 0.5 * 0.8 ** np.arange(21)
        np.testing.assert_allclose(reward_values(np.ones(20), 0.2), expected)

    def test_bounded_values(self):
        rng = np.random.default_rng(1)
        v = reward_values(rng.uniform(0, 1, 200), 0.73)
        self.assertTrue(((v >= 0) & (v <= 1)).all())

    def test_noiseless_recovery_and_flat_likelihood(self):
        rewards = np.tile([0, 0, 1, 1, 1, 0], 10)
        grid = np.linspace(0, 1, 101)
        values = reward_values(rewards, 0.37)[:-1]
        self.assertAlmostEqual(grid[np.argmin(recovery_curve(rewards, values, grid, .1))], .37)
        flat = recovery_curve(np.full(60, .5), np.full(60, .5), grid, .1)
        self.assertEqual(float(np.ptp(flat)), 0)

    def test_observation_is_pre_update(self):
        curve = recovery_curve([1], [.5], [0, .5, 1], .1)
        np.testing.assert_allclose(curve, curve[0])

    def test_invalid_inputs(self):
        for args in (([], .5), ([1], -.1), ([1], 1.1), ([np.nan], .5)):
            with self.subTest(args=args), self.assertRaises(ValueError): reward_values(*args)
        with self.assertRaises(ValueError): recovery_curve([1], [1, 2], [.1], .1)
        with self.assertRaises(ValueError): recovery_curve([1], [1], [.1], 0)


class AccumulationTests(unittest.TestCase):
    def test_repeatability_and_censoring(self):
        kwargs = dict(trials=100, seed=4, dt=.01, horizon=.02, boundary=3.)
        c, rt = ddm(**kwargs)
        c2, rt2 = ddm(**kwargs)
        np.testing.assert_array_equal(c, c2)
        np.testing.assert_array_equal(rt, rt2)
        self.assertTrue(np.isnan(rt[c == 0]).all())
        self.assertTrue(np.any(c == 0))

    def test_zero_drift_and_analytic_moments(self):
        self.assertEqual(symmetric_ddm_moments(0), (.5, 1.))
        c, rt = ddm(drift=0, dt=.002, horizon=12, trials=6000, seed=42, nondecision=0)
        self.assertLess(abs(np.mean(c == 1) - .5), .025)
        self.assertLess(abs(np.nanmean(rt) - 1), .10)
        self.assertLess(np.mean(c == 0), .001)

    def test_drift_probability_and_numerical_error(self):
        p, mean = symmetric_ddm_moments(.7)
        c, rt = ddm(drift=.7, dt=.001, horizon=12, trials=6000, seed=22, nondecision=.25)
        self.assertLess(abs(np.mean(c == 1) - p), .025)
        self.assertLess(abs(np.nanmean(rt) - (mean + .25)), .08)
        finished = c != 0
        self.assertTrue(np.all((rt[finished] >= .251) & (rt[finished] <= 12.25)))
        np.testing.assert_allclose((rt[finished] - .25) / .001, np.round((rt[finished] - .25) / .001), atol=1e-8)

    def test_nondecision_only_shifts_rt(self):
        c, t = ddm(trials=50, seed=3, nondecision=0)
        c2, t2 = ddm(trials=50, seed=3, nondecision=.4)
        np.testing.assert_array_equal(c, c2)
        np.testing.assert_allclose(t2, t + .4)

    def test_invalid_inputs(self):
        for kwargs in ({'dt': 0}, {'noise': 0}, {'boundary': -1}, {'start': 1}, {'trials': 2.5}, {'horizon': .001}, {'drift': np.inf}, {'seed': -1}, {'nondecision': -.1}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError): ddm(**kwargs)


class TimingTests(unittest.TestCase):
    def test_impulse_zero_and_linearity(self):
        _, h = response_kernel()
        impulse = np.zeros(400); impulse[0] = 10
        np.testing.assert_allclose(convolve_signal(impulse, h, .1)[:len(h)], h, atol=1e-15)
        np.testing.assert_array_equal(convolve_signal(np.zeros(30), h, .1), np.zeros(30))
        a = np.arange(40.)
        np.testing.assert_allclose(convolve_signal(3*a, h, .1), 3*convolve_signal(a, h, .1))
        self.assertAlmostEqual(h.sum() * .1, 1)

    def test_exact_confounding_preserves_sum_not_difference(self):
        t = np.arange(20.)
        x = np.column_stack([t, t, np.ones(20)])
        difference = contrast_info(x, [1, -1, 0])
        self.assertFalse(difference['estimable'])
        self.assertIsNone(difference['variance'])
        total = contrast_info(x, [1, 1, 0])
        self.assertTrue(total['estimable'])
        self.assertAlmostEqual(total['variance'], 1 / np.sum((t-t.mean())**2))

    def test_full_rank_matches_inverse_and_noise_scaling(self):
        x = np.random.default_rng(8).normal(size=(50, 3))
        c = np.array([1, -1, 0])
        result = contrast_info(x, c, sigma=2)
        self.assertAlmostEqual(result['variance'], 4 * c @ np.linalg.inv(x.T @ x) @ c)

    def test_near_collinearity_is_imprecise_not_nonestimable(self):
        x = timing_designs()['jittered events']['design']
        base = contrast_info(x, [1, -1, 0])
        x[:, 1] = x[:, 0] + .001*(x[:, 1]-x[:, 0])
        near = contrast_info(x, [1, -1, 0])
        self.assertTrue(near['estimable'])
        self.assertGreater(near['variance'], base['variance']*10000)

    def test_design_repeatability_area_and_fixed_estimability(self):
        a, b = timing_designs(), timing_designs()
        for name in a:
            np.testing.assert_array_equal(a[name]['design'], b[name]['design'])
            np.testing.assert_allclose(a[name]['inputs'].sum(axis=0)*.1, [30, 30])
        self.assertTrue(contrast_info(a['fixed block']['design'], [1, -1, 0])['estimable'])
        self.assertFalse(contrast_info(a['confounded events']['design'], [1, -1, 0])['estimable'])

    def test_invalid_inputs(self):
        for x,c in (([[1, np.nan]], [1, 0]), ([[1, 2]], [1]), ([], [1])):
            with self.assertRaises(ValueError): contrast_info(x, c)
        with self.assertRaises(ValueError): timing_designs(dt=.3, tr=1.)
        with self.assertRaises(ValueError): response_kernel(dt=32)


class FigureDataTests(unittest.TestCase):
    def test_reward_plot_labels_and_saved_settings(self):
        # Check real artist labels and plotted arrays against calculations.
        from unittest.mock import patch
        from demos.run import reward_demo
        import matplotlib.pyplot as plt
        path = Path(__file__).resolve().parents[1] / 'demos/data/rewards.csv'
        captured = []
        with tempfile.TemporaryDirectory() as directory, patch('demos.run.save', side_effect=lambda fig, dest: captured.append(fig)):
            result = reward_demo(Path(directory), path)
        fig = captured[0]
        for line, alpha in zip(fig.axes[0].lines[1:], result['alpha_values']):
            self.assertEqual(line.get_label(), f'alpha={alpha:g}')
            np.testing.assert_array_equal(line.get_ydata(), reward_values(result['rewards'], alpha))
        self.assertGreater(result['recovery']['short and noisy']['mae'], result['recovery']['informative']['mae'] * 3)
        self.assertEqual(result['flat_nll_range'], 0)
        plt.close(fig)


class OtherFigureDataTests(unittest.TestCase):
    def test_accumulation_histogram_labels_match_calculated_fractions(self):
        from unittest.mock import patch
        from demos.run import accumulation_demo
        import matplotlib.pyplot as plt
        figures = []
        with tempfile.TemporaryDirectory() as directory, patch('demos.run.save', side_effect=lambda fig, dest: figures.append(fig)):
            result = accumulation_demo(Path(directory))
        for ax, (name, report) in zip(figures[0].axes, result['configurations'].items()):
            self.assertIn(f"v={report['settings']['drift']}", ax.get_title())
            self.assertIn(f"unfinished={report['unfinished']:.2%}", ax.get_title())
            # Histtype=step is a polygon with each bin height repeated twice.
            for polygon, key in zip(ax.patches, ('upper_all', 'lower_all')):
                y = polygon.get_xy()[:, 1]
                self.assertAlmostEqual(float(y[1:-1:2].sum()), report[key])
        for fig in figures: plt.close(fig)

    def test_timing_matrix_images_equal_saved_calculations(self):
        from unittest.mock import patch
        from demos.run import timing_demo
        import matplotlib.pyplot as plt
        figures = []
        with tempfile.TemporaryDirectory() as directory, patch('demos.run.save', side_effect=lambda fig, dest: figures.append(fig)):
            result = timing_demo(Path(directory))
            axes_with_images = [ax for ax in figures[0].axes if ax.images]
            for ax, name in zip(axes_with_images, result['designs']):
                matrix = np.loadtxt(Path(directory)/(name.replace(' ', '-')+'-matrix.csv'), delimiter=',', skiprows=1)
                np.testing.assert_array_equal(ax.images[0].get_array(), matrix)
                self.assertEqual([label.get_text() for label in ax.get_xticklabels()], ['A','B','intercept'])
        for fig in figures: plt.close(fig)


if __name__ == '__main__': unittest.main()
