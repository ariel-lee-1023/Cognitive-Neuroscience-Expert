# Causal Inference: What If — Miguel A. Hernán & James M. Robins
**Format**: md | **Pages**: ~610 (extractor estimate, not printed pagination) | **Sections**: 22 chapters, 3 parts | **Depth**: study | **Type**: technical

**Source version:** February 21, 2020, as printed in the supplied Markdown. Locators refer to its chapters, sections, Fine Points, and Technical Points. OCR interleaves marginal notes and damages equations; the notation below is reconstructed explicitly. Clinical examples explain methods and are not current treatment recommendations.

## Mental Model (read first)
Start with a causal question precise enough to describe the intervention comparison, population, outcome, and time horizon. Then distinguish **identification**—whether the causal quantity can be expressed using the observed distribution under stated assumptions—from **estimation**—how to learn that quantity from a finite sample. More data, a better predictor, or a smaller p-value cannot repair an unidentified question.

The organizing device is the **target trial**. Observational analysis attempts to emulate a specified trial using available data; credibility depends on that emulation and its identifying assumptions. A causal diagram makes proposed relationships explicit but cannot certify its own correctness.

**Use for:** causal estimands, confounding, selection, measurement, standardization, inverse probability weighting, propensity scores, instrumental variables, longitudinal treatment strategies, and target-trial emulation. A valid intervention effect does not by itself reveal the organized mechanism producing the effect; pair with [Craver](reference-craver-explaining-brain.md) when making that stronger claim.

## Frameworks & Structure

### Chapters 1–3 — Define the effect and identify it
**Locator:** Chs 1–2; Ch 3 §§3.1–3.6.

Let A denote treatment, Y the outcome, L measured pretreatment covariates, and `Y^a` the outcome under intervention setting A to a. An individual effect compares counterfactual outcomes for the same individual, but both are not observed under a single treatment assignment. An average effect such as `E[Y^1]−E[Y^0]` is a different, potentially identifiable target. A zero average effect does not imply zero effect for every individual.

**Risk difference**, **risk ratio**, and **odds ratio** are different effect scales. State the outcome horizon and scale before comparing effect sizes or heterogeneity. An associational contrast `E[Y|A=1]−E[Y|A=0]` equals a causal contrast only under the relevant conditions.

For the standard treatment-adjustment route:

- **Exchangeability:** `Y^a ⟂ A | L` for the interventions being compared, or the weaker mean condition sufficient for the chosen mean estimand. Measured L must make groups comparable in their counterfactual outcomes. It is not demonstrated merely by balancing observed covariates.
- **Positivity:** each treatment value required by the target comparison has positive probability within the relevant covariate strata represented in the target population. A structural zero cannot be repaired by a larger sample or an extreme weight. Practical near-zeros make estimation unstable.
- **Consistency:** if an individual receives the intervention version represented by a, observed Y corresponds to `Y^a`. First define interventions meaningfully, then connect their versions to the observed data. Different ways of changing weight, brain activity, or exposure may have different effects.

Random assignment supports exchangeability for assignment in the randomized population. Nonadherence, post-assignment selection, measurement error, and a mismatch between assignment and receipt still require analysis. **No interference** is an additional simplifying condition for counterfactuals indexed only by one's own treatment; when others' treatments matter, the intervention and counterfactual notation need to represent that dependence.

Under the assumptions, **standardization** identifies

`E[Y^a]=Σl E[Y|A=a,L=l]P(L=l)`.

This averages conditional outcomes over the **target** covariate distribution rather than over the potentially different distributions in the observed treatment groups. Integrals replace sums for continuous covariates.

**Inverse probability weighting (IPW)** expresses the same mean as

`E[1(A=a)Y / P(A=a|L)]`.

This unnormalized population identity uses the indicator for the intervention of interest. Finite-sample normalized and unnormalized estimators need not coincide. The pseudo-population is a mathematical representation of reweighting, not new independent participants.

### Chapters 4–5 — Effect modification is not the same question as interaction
**Locator:** Ch 4 §§4.1–4.6; Ch 5 §§5.1–5.6.

**Effect modification** means that the effect of A differs across values of another variable V on a specified scale. Additive effect modification can coexist with no multiplicative modification. A subgroup result needs adequate exchangeability and positivity within the subgroup; a coefficient alone does not supply these.

**Interaction** in this framework concerns a joint intervention on two treatments, using counterfactuals such as `Y^(a,b)`. A comparison of treatment effects by a nonmanipulated attribute is not automatically evidence about the effect of intervening on that attribute. Statistical product terms depend on the model link and effect scale.

**Sufficient-component cause models** represent combinations sufficient to produce an outcome and clarify causal coaction. Their relationship to counterfactual interaction depends on assumptions such as monotonicity and the selected effect scale. Do not infer a biological molecular interaction solely from a nonzero regression interaction, or infer no causal interaction because one product term is nonsignificant.

### Chapters 6–7 — Draw causal structure before selecting adjustment variables
**Locator:** Ch 6 §§6.1–6.5; Ch 7 §§7.1–7.6, including the backdoor criterion and single-world intervention graphs.

A **directed acyclic graph (DAG)** encodes proposed direct causal relations among represented variables. A path is not necessarily directed. Along a path, conditioning on a noncollider blocks transmission of association; conditioning on a **collider** or its descendant can open a path that was otherwise blocked. The collider role is path-specific.

A **backdoor path** enters A through an incoming arrow. A sufficient **backdoor adjustment set** blocks all such paths without including descendants of A under the criterion's conditions. A confounder is not defined by having a significant association with both A and Y or by changing a regression coefficient. Different sufficient sets may exist; a common cause need not itself be measured if an observed variable blocks the relevant path.

**Confounding** violates the relevant exchangeability condition. Absence of association with measured covariates does not establish absence of confounding by unmeasured variables. Conversely, adding a pretreatment collider can introduce bias; “measured before treatment” is not enough to justify adjustment.

**Single-world intervention graphs (SWIGs)** split a treatment node into random and fixed parts to express independences involving counterfactual outcomes under one intervention. They help state assumptions precisely; they do not infer the graph from associations alone.

**How:** define treatment time; identify causes of treatment and outcome; represent selection, measurement, and relevant histories; trace open paths; state the adjustment set and the knowledge supporting it. Keep plausible alternative graphs when their differences change identification.

### Chapters 8–9 — Selection and measurement can defeat otherwise good assignment
**Locator:** Ch 8 §§8.1–8.6; Ch 9 §§9.1–9.5.

**Selection bias** can arise by restricting analysis to a collider or its descendant. Completion, hospital attendance, survival, clean EEG, or adherence can be selection events; whether they bias a particular estimand depends on the causal structure. Selection is not invariably bias, and representativeness and internal causal validity are not interchangeable.

Let C=0 mean uncensored. Weighting retained observations by `1/P(C=0|A,L)` can correct a specified selection mechanism only with exchangeability for censoring, positivity of remaining observed, and consistency. When both treatment and censoring require adjustment, weights can be multiplied if the corresponding joint or sequential assumptions hold. Post-treatment predictors require longitudinal reasoning rather than mechanically inserting them into a baseline formula.

Reweighting cannot reconstruct outcomes for a stratum that is never observed. If selection depends on unmeasured outcome causes not accounted for by available history, name that remaining identification problem. A balanced table after weighting is useful diagnostic evidence, not proof that these causes are absent.

**Measurement error** concerns observed proxies for treatment, outcome, or confounders. Errors can be differential or dependent across variables. Error in a confounder can leave residual confounding after adjustment; even nondifferential error does not universally attenuate an effect toward the null. Match any directional claim to its assumptions.

An **intention-to-treat effect** concerns assignment. A **per-protocol effect** concerns adherence to the treatment strategies specified in the protocol. Restricting to observed adherers does not automatically identify the latter: adherence is often affected by evolving prognosis. The estimand, rather than a preferred analysis label, determines how these events should be handled.

### Chapters 10–11 — Identification precedes statistical modeling
**Locator:** Ch 10 §10.1 and §10.5; Ch 11 §§11.1–11.5.

An **estimand** is the target quantity, an **estimator** a rule mapping samples to estimates, and an **estimate** its realized value. Statistical consistency of an estimator as sample size increases is distinct from causal consistency linking observed and counterfactual outcomes.

**Random variability** is not confounding or selection bias. Confidence intervals quantify sampling uncertainty under assumptions; they do not ordinarily include uncertainty about an incorrect causal diagram or unmeasured confounding. A narrow interval can surround the wrong target.

The **curse of dimensionality** makes fully stratified nonparametric estimation impractical with rich covariates. Parametric and smoothing models trade flexibility, bias, and variance. These models estimate parts of an identified functional; predictive fit alone does not establish the causal assumptions that licensed the functional.

### Chapter 12 — IP weighting and marginal structural models
**Locator:** §§12.2–12.6, including positivity diagnostics and censoring weights.

A **marginal structural model (MSM)** describes a marginal counterfactual mean, such as `E[Y^a]=β0+β1a`; it is not the treatment-assignment model. Estimate the **propensity** or treatment density to construct weights, then fit the weighted outcome model appropriate to the causal contrast.

For a time-fixed exposure, **stabilized weights** have numerator `P(A)` and denominator `P(A|L)` in the simple marginal case. Including baseline variables in the numerator changes the required conditioning in the structural analysis. Stabilization does not magically repair lack of overlap or misspecification. In a saturated binary-treatment model, stabilized and unstabilized estimates can be identical; variance benefits are not universal.

Inspect weight distributions, outliers, overlap, and the covariate balance relevant to the target. A stabilized mean near one is an expected diagnostic under the model, not sufficient evidence of validity. **Truncating weights** trades instability for bias and may change the effective population; disclose it and assess sensitivity instead of presenting truncation as a cure for structural nonpositivity.

### Chapter 13 — Standardization and the parametric g-formula
**Locator:** §§13.1–13.5.

**How:** fit `m(a,l)=E[Y|A=a,L=l]` in observed data; set A to a for every member of the target covariate sample; predict each outcome; average predictions; repeat for the alternative intervention and compare. This estimates a marginal effect even though the nuisance outcome model is conditional.

The parametric **g-formula** depends on the outcome model's adequate specification, the identifying assumptions, and a supported target population. A regression coefficient is not generally the standardized marginal contrast; nonlinear links and effect modification make this especially apparent. Compare IPW and standardization through their different modeling burdens, not through a claim that one removes the need for assumptions.

### Chapter 14 — G-estimation of structural nested models
**Locator:** §§14.2–14.6 and Technical Point 14.1.

A **structural nested model (SNM)** describes treatment effects relative to a reference strategy, potentially conditional on treatment and covariate history. **G-estimation** searches for effect parameters that, after removing the hypothesized treatment effect, make the resulting counterfactual-like outcome satisfy the exchangeability restrictions with respect to treatment assignment.

**Rank preservation** assumes a strong relationship between individuals' potential outcomes; additive versions may impose a common effect within strata. It is a useful pedagogical construction, not a generally credible assumption about individual biological responses, and mean-model g-estimation need not assert identical individual effects.

Keep mean, multiplicative, and logistic structural models distinct. The source specifically cautions that the straightforward g-estimation procedure for mean models does not directly extend to structural nested logistic models. Do not present a generic “subtract the coefficient and regress” recipe as valid for every outcome type.

### Chapter 15 — Outcome regression and propensity scores
**Locator:** §§15.1–15.5.

The **propensity score** `e(L)=P(A=1|L)` is a balancing score for measured covariates in the setting where its theory applies. Matching, stratification, weighting, and regression adjustment use it differently and can target different populations or require further modeling choices.

Propensity-score balance does not balance unknown confounders by definition. Matching can discard people, changing the supported target; residual within-stratum imbalance can remain after coarse stratification. Predicting treatment extremely accurately can reflect poor overlap, not excellent causal identification. Keep the treatment model, structural effect model, and outcome prediction model conceptually separate.

### Chapter 16 — Instrumental variables: a different assumption set
**Locator:** §§16.1–16.6.

A candidate **instrument Z** needs **relevance** for treatment, an **exclusion restriction** ruling out outcome effects outside the treatment pathway, and appropriate **exchangeability** for the instrument–outcome relation. The latter two generally cannot be established from observed associations alone. Genetic variation, physician preference, and access are proposed instruments whose substantive assumptions still need defense.

For binary Z, the usual **Wald estimand** is

`[E(Y|Z=1)−E(Y|Z=0)] / [E(A|Z=1)−E(A|Z=0)]`.

The three instrumental conditions alone do not generally identify the population average treatment effect. Additional homogeneity assumptions can support a population interpretation. With suitable binary-treatment conditions and **monotonicity** (no defiers), the ratio can identify the average effect among **compliers**, not automatically among everyone. Always-takers, never-takers, compliers, and defiers are counterfactual compliance types, not directly observed subgroups.

A weak first-stage difference makes estimation unstable. An instrument is not a general escape from causal assumptions; it substitutes assumptions and may change the identifiable target.

### Chapters 17–18 — Survival and variable selection
**Locator:** Ch 17 §§17.1–17.5; Ch 18 §§18.1–18.5.

**Hazard** is conditional on surviving to the interval; **risk** is cumulative by a specified time. In discrete time, `S(k)=∏m≤k[1−h(m)]` and cumulative risk is `1−S(k)`. A hazard ratio is not a risk ratio and can compare treatment-dependent survivor populations. For a causal question about survival, define the intervention-specific survival or risk contrast and handle censoring appropriately.

Person-time data arrange one row per individual per interval until the event or follow-up ends. The outcome, covariates, and treatment must preserve temporal order. Kaplan–Meier and regression models do not remove informative-censoring problems merely by accepting this data format.

**Variable selection for causal inference** differs from selection for prediction. Including all measured pretreatment variables can open a collider path or amplify residual confounding through an instrument-like variable. Statistical association alone cannot establish which graph is correct.

**Doubly robust estimators** combine outcome and treatment models so that, under their conditions, adequate specification of one nuisance part can suffice. This is not robustness to failure of consistency, positivity, exchangeability, or arbitrary misspecification of both parts. Machine learning can improve nuisance estimation; it cannot determine the causal structure from predictive accuracy alone.

### Chapters 19–20 — Treatment histories and treatment-confounder feedback
**Locator:** Ch 19 §§19.1–19.6; Ch 20 §§20.1–20.5 and Fine Point 20.2.

A **static strategy** prespecifies treatment over time; a **dynamic strategy** assigns treatment using measured history, such as initiating treatment when an observed marker crosses a threshold. “Ever treated” is not an adequate replacement for a clearly timed strategy.

With histories `Āk−1` and `L̄k`, **sequential exchangeability** requires that current treatment be exchangeable with the relevant future counterfactual outcomes conditional on appropriate past history. Positivity is needed for the actions required by the strategy at histories the strategy can generate. Identification can hold for some strategies but not all.

**Treatment-confounder feedback** arises when Lk predicts subsequent treatment and outcome and is itself affected by prior treatment; the source also treats related structures in which Lk shares an unmeasured cause with prior treatment. Time-varying confounding alone does not necessarily imply feedback.

Ordinary adjustment faces two problems: conditioning on Lk may block an earlier treatment's mediated effect, and it may open a collider path such as `A0 → L1 ← U1 → Y`. Omitting Lk can leave confounding for later treatment. Adding more covariates or interactions to the same conditional contrast does not generally solve this problem. The correct response is to choose an estimand and a method that handles the histories coherently, rather than deciding that all post-treatment covariates should always be ignored.

### Chapter 21 — G-methods for time-varying treatments
**Locator:** §§21.1–21.5; Technical Point 21.2 (g-null paradox).

For a static strategy ā and discrete histories, the longitudinal **g-formula** has the schematic form

`E[Y^ā]=Σl̄ E[Y|Ā=ā,L̄=l̄] ∏k P(Lk=lk | Āk−1=āk−1,L̄k−1=l̄k−1)`.

Baseline L0 uses its baseline distribution. Sequential exchangeability, consistency, and strategy-specific positivity license the causal interpretation. Dynamic strategies replace each fixed action by the action prescribed for that simulated history. The g-formula's assembled functional may have a causal interpretation even when individual regression components do not.

**Parametric g-computation:** model covariate evolution and outcome; sample baseline histories; simulate each history forward under the chosen strategy, allowing covariates to evolve; average outcomes and contrast strategies. Hold the intervention rule fixed while allowing its consequences to propagate.

**Longitudinal IPW** multiplies treatment-probability factors over time. A common stabilized treatment weight is `∏k P(Ak|Āk−1)/P(Ak|Āk−1,L̄k)`, with appropriate baseline conditioning when used. Add censoring weights under the corresponding sequential assumptions. Model adequacy and support become more demanding as histories grow.

**Longitudinal doubly robust methods** and **g-estimation of structural nested models** provide alternatives with their own nuisance-model and structural assumptions. Do not collapse them into one algorithm. Censoring can itself be treated as a time-varying intervention when defining outcomes under remaining observed.

The **g-null paradox** warns that common independently parameterized, nonsaturated models for the g-formula can be incompatible with a sharp causal null under feedback, producing misspecification even when identification holds. It is a modeling limitation, not proof that the g-formula is causally invalid or that it always yields appreciable bias in finite samples.

### Chapter 22 — Target-trial emulation and time zero
**Locator:** §§22.1–22.5 and Technical Points 22.1–22.2.

Specify the target protocol: eligibility, treatment strategies, assignment procedure, start and end of follow-up, outcome, causal contrast, and analysis. Then map each component to the observed data and list deviations. A scientifically appealing protocol may be unemulable with the available treatment versions, measurement schedule, or covariates.

**Time zero** must align eligibility, treatment-strategy assignment, and start of follow-up. Defining treatment by future survival or starting outcome counting after the intervention can select treatment-dependent survivors and create **immortal-time** or related selection bias. When individuals have multiple eligible times, nested target trials can use them, but variance estimation must account for repeated contributions.

Grace periods may require cloning people into strategies with which they are initially compatible, censoring upon deviation, and weighting that artificial censoring under the necessary assumptions. This is not the same as assigning future treatment retrospectively at baseline. When everyone is cloned into both strategies during a grace period, the comparison targets a form of per-protocol effect, not an intention-to-treat effect between distinct baseline assignments.

**Controlled direct effects** compare A interventions while setting a mediator B to a specified value; identification requires assumptions for both interventions. **Natural direct and indirect effects** involve cross-world counterfactuals and generally stronger assumptions. Hernán and Robins emphasize that a natural direct effect cannot be identified by randomization alone, even in principle; its observational identification therefore depends on assumptions beyond a realizable target-trial comparison. Neither a mediator-adjusted coefficient nor an identified total effect automatically establishes a biological mediation pathway.

## Worked Example — standardizing the smoking-cessation comparison
**Reconstruction:** Ch 13's expanded-dataset procedure, applied to the book's smoking-cessation/body-weight example. No new empirical estimate is supplied.

Define A as the specified cessation exposure, Y as weight change over follow-up, and L as measured baseline covariates. Establish the target population and intervention versions before modeling; retain the caveat that incomplete follow-up needs censoring analysis.

Make three conceptual copies of the covariate rows. The observed-data copy supplies A and Y for fitting the outcome model. In the second copy set A=0 and leave Y unobserved; in the third set A=1. Predict outcomes in both intervention copies using the model fitted only on observed outcomes. Average the A=1 predictions over the same baseline covariate distribution used for A=0, then subtract.

This estimates a standardized marginal mean contrast under the identifying and modeling assumptions. The copied rows are prediction inputs, not additional observed people. Interactions belong in the model when needed; the coefficient for A is not substituted for the average prediction contrast. If influential confounders were unmeasured or an intervention lacks support, duplicating rows and fitting a flexible model does not identify the missing counterfactual mean.

## Decision Rules & Judgment

- Before selecting an estimator, state population, interventions, outcome horizon, and causal contrast. Name mismatches between that target and the data.
- Separate identification assumptions from estimation uncertainty. Precision does not establish causal validity.
- Defend exchangeability, positivity, and consistency for the particular intervention and target; do not certify them through balance or fit alone.
- Choose adjustment variables from causal structure and timing. Avoid indiscriminate adjustment for colliders, mediators, or instrument-like variables.
- Analyze post-assignment retention and adherence explicitly; randomization does not automatically protect a selected comparison.
- For IPW, examine support, weights, and balance; report stabilization and truncation. No weighting method creates information where the required histories never occur.
- For a marginal effect from an outcome model, standardize predictions rather than interpreting a conditional coefficient by default.
- Under treatment-confounder feedback, use an appropriate g-method with sequential assumptions. Neither routine adjustment nor routine omission solves both sources of bias.
- For IV estimates, distinguish the three instrumental conditions from the additional condition determining the estimand; a complier effect is not automatically a population effect.
- Align time zero in the target trial and emulation; avoid defining treatment using future information.
- Preserve the distinction between an intervention effect, mediation, and a complete neural mechanism. These require different evidence.

## Key Takeaways
Causal conclusions require an explicit intervention question plus identifying assumptions. Models and data estimate an answer only after that logical step. Longitudinal feedback, selection, measurement, and intervention-version mismatches are substantive threats that no general “control for everything” rule resolves.

**Coverage note:** All 22 chapters are represented, grouped where their methods belong together. Long proofs, full worked datasets, software-specific programs, and most Fine/Technical Point derivations are omitted. The g-null paradox, SNM-logistic limitation, IV target restriction, and time-zero requirements are retained because they change decisions. The source does not supply current clinical effect sizes, a complete causal-discovery system, or a universal method for unmeasured confounding and mediation.
