Generally, no. An ordinary outcome regression that controls for every symptom measurement does not generally estimate the **total effect of a treatment strategy** when treatment changes later confounders.

Let `A0` be early treatment, `L1` subsequent symptoms, `A1` later treatment, and `Y` the outcome. Your description implies:

- `A0 → L1 → Y`: symptoms carry part of the earlier treatment's effect.
- `L1 → A1` and `L1 → Y`: symptoms also confound the later treatment–outcome relationship.

Controlling for `L1` in a conventional outcome regression blocks the first pathway, removing part of the total effect. If symptoms also have an unmeasured cause that affects the outcome, conditioning on them can additionally open a collider path, such as `A0 → L1 ← U → Y`. That extra bias depends on the underlying causal structure; it is not required for the basic problem. Simply omitting `L1` leaves later treatment confounded. This is **treatment-confounder feedback**. A symptom-adjusted treatment coefficient is not automatically a direct causal effect either.

First define the strategies, target population, outcome, and follow-up horizon. For example, compare sustained treatment with sustained no treatment, or compare two explicit rules that adapt treatment to symptoms. The target is a contrast such as `E[Y under strategy g] − E[Y under strategy h]`, allowing symptoms to evolve under each strategy.

Use a longitudinal **g-method** appropriate to that target:

- **G-computation** models symptom evolution and outcomes, then averages predicted outcomes under each strategy. Regression can be part of this procedure, but post-treatment symptoms must evolve according to the strategy rather than remain fixed at their observed values for both comparisons.
- **Inverse-probability weighting with a marginal structural model** uses treatment probabilities conditional on prior treatment and symptom histories to account for confounding at each treatment decision.

These approaches require consistency for well-defined interventions, sequential exchangeability given measured history, and positivity for the actions each strategy requires, together with adequate estimation of the relevant models. Loss to follow-up needs its own corresponding assumptions and handling. The study description alone cannot establish these conditions or provide an effect estimate.

Source: supplied Hernán–Robins reference, Chapters 19–21, with estimand specification from Chapter 22. This is a methodological assessment of the stated causal structure, not an empirical analysis.
