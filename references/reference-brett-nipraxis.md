# Nipraxis: Introduction to Practical Neuroimaging in Python — Matthew Brett et al.
**Format**: md/Rmd (textbook.nipraxis.org) | **Pages**: ~245 | **Sections**: 67 chapters across 6 parts | **Depth**: study

## Mental Model (read first)
This is the library's **epistemics-of-practice** source, and it is the only one that argues that *how you organize your analysis determines whether you can think scientifically at all*. Its thesis: brain imaging requires working knowledge of eight disciplines, most people learn them at a **"makes-sense" level** where you cannot challenge your teacher, and the resulting **disorganized, encrusted practice** consumes the cognitive capacity you need for the questions that matter — "Do I believe this result?", "How would I know if my hypothesis was wrong?"

The remedy is to build every method from primitives — read the raw bytes of a NIfTI file, implement convolution and the GLM yourself — so that **you take no one's word for it**. The motto is literal: *Nullius in Verba*.

**Reach for this book when you need**: the mathematical guts of the GLM/convolution/t-statistic rather than a software wrapper; the exact logic of Bonferroni and Šidák correction; what an image actually *is* (array + affine); a worked check of whether normalization really aligns the anatomy you care about; or an argument for why reproducibility is a scientific rather than administrative obligation.

**Coverage note**: this distillation front-loads the epistemic argument, the image/affine representation, the GLM built from scratch, and the family-wise error mathematics. Compressed: Python/NumPy mechanics (`arange`, `allclose`, broadcasting, reshaping, indexing, dunders, list comprehensions, path manipulation), Jupyter and git workflow, module and package structure — general scientific-computing skills that are prerequisites here rather than neuroscience content. The practical linear algebra and image-processing chapters are represented by their conceptual payload rather than their code.

---

## Frameworks & Structure

### Part I: The neuroimaging problem — why process is epistemology
- **Core idea**: The book teaches two things in a deliberate order — (1) *working with* brain imaging data, then (2) principles of analysis methods. The ordering is the argument: without organized practice you cannot reach the principles.
- **The eight disciplines** a neuroimaging researcher needs working knowledge of: **neuroanatomy, neurophysiology, data analysis, physics, signal processing, image processing, linear algebra, statistics.** "You can do neuroimaging badly without knowing much about some of these, but to do it well, to ask intelligent fruitful questions, you will need a working knowledge of all of these, and deep knowledge in some of them."
- **The failure pattern, in three named stages** — this is the book's diagnostic framework and the most portable thing in it:
  1. **The "makes-sense" level** — "the level at which you are prepared to take the word of your teacher on facts and interpretation, but you can't challenge what your teacher is saying, because you don't understand it deeply enough." *Name this state when you are in it.*
  2. **Picking up the rest as you go**, accepting practice on faith — "It's what your mentor does, or what the lab does. You may not even ask yourself why your mentor or your lab does what it does. **They may not know themselves.**" Quoting Chekhov: "Medicine is the application of the laws of science; except there is a lot of law, and not much science."
  3. **Encrusted habit** — analysis has many steps and many defensible choices (the *plurality* of analysis pipelines), so it is easy to get confused, easy to err, hard to replicate your own work, "and all but impossible to replicate an analysis by someone else. **This confusion is a poison to clear thought.**"
- **The cost, stated as a capacity argument**: Robin Murray's 2001 talk "Should psychiatry take fMRI research seriously?" (answer: "not yet") wondered aloud "whether the frontal lobes of researchers in the field were so occupied by the difficulties of analysis, that they no longer had the capacity to think of a hypothesis." **The claim is not that disorganized researchers are lazy — it is that analysis overhead crowds out theory.**
- **Four consequences of disorganized analysis**, each distinct: (a) work "that is like science, but not science"; (b) **you make many mistakes and don't realize it, because your process makes checking hard**; (c) you stay inefficient — "this time will not reduce markedly, with more experience," because you never learn to automate; (d) collaboration fails, because you cannot explain the process to yourself, let alone others.
- **Feynman's criterion** (from "What is Science", 1969): *"Science alone of all the subjects contains within itself the lesson of the danger of belief in the infallibility of the greatest teachers in the preceding generation… Learn from science that you must doubt the experts… **Science is the belief in the ignorance of experts.**"* Paired with the Royal Society's motto **Nullius in Verba** — "Take no-one's word for it."
- **Donoho on the ubiquity of error**: *"The scientific method's central motivation is the ubiquity of error — the awareness that mistakes and self-delusion can creep in absolutely anywhere and that the scientist's effort is primarily expended in recognizing and rooting out error."* **The relevant point: the more experienced the computational scientist, the more they worry about error in their own work.**
- **The reproducibility argument in its strongest form** (Buckheit & Donoho, WaveLab): *"An article about computational science in a scientific publication is not the scholarship itself, it is merely **advertising** of the scholarship. The actual scholarship is the complete software development environment and the complete set of instructions which generated the figures."*
- **Cargo cult science** (Feynman, 1974): imitating the form of scientific investigation — runways, wooden headphones, bamboo antennas — while missing what makes planes land. **The distinguishing thing is named precisely: "a kind of scientific integrity… a kind of utter honesty — a kind of leaning over backwards… the idea is to give all of the information to help others to judge the value of your contribution; not just the information that leads to judgement in one particular direction."**
- **The practical corollary, and the reason the ordering matters: "rigor is hard to retrofit."** You *can* analyze without organized process, "but you will find it takes an enormous amount of work to go back and make your process reproducible. And you won't gain from that work, because you'll have to do it all again for your next paper." Organized working costs time up front and repays across every future project.
- **Why code, specifically**: code is written in a *language* that "expresses ideas and procedures," so it becomes a way to think about what you are doing — not merely to execute it.

### Part II: What an image actually is
- **Core idea and the book's signature pedagogical move**: do not accept "an image" as a primitive. Open the file, read the bytes, parse the header by hand.
- **The NIfTI-1 exercise**: read the file with `Path.read_bytes`; **the first 352 bytes are the header** describing the parameters of the image and the data that follow; slice out the `datatype` field at its documented byte offset (careful — there is also a distinct `data_type` field with an underscore); the value is stored **in binary, in the same format the computer holds the number in memory**, so decode it with `struct.unpack` using an explicit format string. **You can also read out which software wrote the image.**
- **Why this matters beyond the exercise**: it establishes that an image is **an array of numbers plus metadata that tells you how to interpret it in space** — and that every downstream operation (registration, masking, coordinate reporting) depends on that metadata being right. **Header and data can disagree; only reading them separately reveals it.**
- **The array progression the course builds through**: 1D → 2D (`reshape_and_2d`) → **arrays as images** → 3D volumes (`arrays_3d`, `images_3d`) → **4D time-series** (`intro_to_4d`) → the **voxels-by-time** reshape (`voxels_by_time`) that turns a 4D dataset into the time × voxels matrix the GLM operates on. **That single reshape is the pivot from "brain picture" to "design-matrix problem."**
- **Affines** (`nibabel_affines`, `nibabel_apply_affine`, `image_header_and_affine`, `images_and_affines`): the affine matrix maps **voxel indices → spatial coordinates**. This is what makes it meaningful to say "MNI 0, 20, 44," what makes two images comparable, and what any resampling must get right.
- **Boolean masking** (`boolean_arrays`, `boolean_indexing`, `boolean_indexing_nd`) as the mechanism for restricting analysis to in-brain voxels.

### Part III: Working reproducibly
- **Modules and the Python path** (`on_modules`, `sys_path`, `module_directories`): a module is a `.py` file on the path; a **module directory** lets one module span many files. *The point is to move analysis out of ad-hoc notebook cells into reusable, testable units.*
- **`assert`** — "raise an error unless the following expression is equivalent to True," using Python **truth value testing**, not `== True`.
  - **The authors' warning about this Python construct**, routinely violated in analysis code: `assert` is for development, testing and debugging — declaring that a condition is expected to be true — and not for raising errors at runtime. Their reason is decisive: when Python runs with optimization, `assert` statements are **stripped out for speed**, and the code's author does not control whether it is run that way. Runtime error conditions call for raised exceptions instead.
- **Coding style** — PEP8, with **Pylint** as a checker. The stated benefit is cognitive, not aesthetic: "Once you have learned the guidelines, you will spend less time thinking about formatting and more time thinking about **the algorithm and code structure**."
- **Docstrings** — the **numpy docstring standard**. Four reasons given, and the first is the important one: **"the process of writing the docstring forces you to explain the function to yourself, and therefore write clearer code with better design."** The others: others can read it; `help()` / `func?` retrieve it; Sphinx renders it. **Write the documentation *as* you write the code**, to help you find the cleanest design.
- **Testing** (`on_testing`) and **data validation** (`validating_data`) — verifying that the data you have is the data you think you have, before analyzing it.
- **Floating point** (`allclose`): computers cannot represent every float exactly, so **never test computed results for exact equality** — use `np.allclose`. *A small point with large consequences for anyone comparing pipeline outputs.*

### Part IV: Detecting activation — the model, built from primitives
- **Voxel time courses** (`voxel_time_courses`): the signal at one voxel across the run, the unit the whole model operates on.
- **Convolution** (`on_convolution`, `convolution_background`, `convolution_matrices`): implemented rather than invoked. The neural event sequence convolved with the hemodynamic response gives the **predicted BOLD time-course** — the regressor. Convolution is also expressible as a **matrix** operation, which is what connects it to the GLM.
- **Regression** (`on_regression`, `regress_one_voxel`, `regression_notation`) — fit one voxel first, with explicit notation, before generalizing.
- **The GLM in matrix form** — the notation the book insists you be able to read:
  $$\vec{y} = \boldsymbol{X}\vec{\beta} + \vec{\varepsilon}$$
  where $\vec{y}$ is the data (time-points), $\boldsymbol{X}$ the **design matrix**, $\vec{\beta}$ the parameters, $\vec{\varepsilon}$ the errors.
- **The t-statistic, written out** — because the point is to know what your software computes:
  $$\hat\sigma^2 = \frac{1}{n - \textrm{rank}(\boldsymbol{X})}\sum e_i^2 \qquad t = \frac{\vec{c}^T\hat{\vec\beta}}{\sqrt{\hat\sigma^2\,\vec{c}^T(\boldsymbol{X}^T\boldsymbol{X})^{+}\vec{c}}}$$
  - **The decomposition to remember**: the denominator is the square root of **two** components — (a) **the estimated variance**, from the squared residuals *in the data*, and (b) **the covariance of the design**, which depends *only on the contrast and the design matrix*. **Half of your t-statistic is determined before you collect any data. That is why design optimization is a statistical intervention, not a convenience.**
  - **Degrees of freedom** are $n - \textrm{rank}(\boldsymbol{X})$ — note it is the *rank*, not the column count, so collinear regressors do not buy you what they appear to.
  - **The contrast vector $\vec{c}$** selects the combination of parameters being tested (e.g. the second row of the parameter array to test a slope against zero).
- **Whole-image estimation** (`whole_image_statistics`, `multi_multiply`): reshape 4D data to **time × voxels** and fit every voxel in one matrix operation. *This is the mass-univariate analysis made mechanically explicit.*
- **`nan` handling as a diagnostic, not a nuisance**: white edges in a t-map are voxels where "all the scans have 0 at this voxel, so the numerator and denominator of the t statistic are both 0." **These out-of-brain voxels have p-value 0 and therefore *always survive* correction, appearing as spurious white.** The fix is a brain mask (e.g. **Otsu's method**), applied *before* the GLM so both estimation and correction operate on in-brain voxels only. **A concrete case where an artifact of the pipeline masquerades as a maximally significant result.**
- **Hypothesis testing** (`hypothesis_tests`, `mean_test_example`, `numpy_random`) — including simulation-based reasoning about null distributions.

### Part V: Multiple comparisons — the mathematics, derived
- **Family-wise error rate (FWER)**, defined: the Bonferroni threshold "treats a set of tests as one *family*, and the threshold is designed to control the probability of detecting **any** positive tests in the family, if the null hypothesis is true."
- **Šidák correction first, because it is derivable** — the book teaches this before Bonferroni precisely because the inequality behind Bonferroni is harder to explain:
  - Probability all $n$ tests are *above* threshold $\theta$, **assuming tests are independent**: $(1-\theta)^n$
  - Probability one or more is $\le \theta$: $1 - (1-\theta)^n$
  - Set equal to the desired FWE rate: $\alpha_{fwe} = 1 - (1-\theta)^n$
  - Solve: $\boxed{\theta = 1 - (1-\alpha_{fwe})^{1/n}}$
- **Bonferroni** rests on **Boole's inequality**: the probability of one or more events is no greater than the sum of their individual probabilities,
  $$\mathbb{P}\Bigl(\bigcup_i A_i\Bigr) \le \sum_i \mathbb{P}(A_i)$$
  from which the threshold is simply $\alpha_{fwe}/n$ — "the desired family-wise error rate divided by the number of voxels."
- **The independence assumption is stated at the point where it enters**, which is what makes this treatment useful: the Šidák derivation says *"assuming tests are independent"* in the same breath as the formula. **Voxels are spatially autocorrelated, so both corrections are conservative for imaging** — this is the mathematical basis for the cluster and permutation methods in [[reference-jahn-brain-book]].

### Part VI: Space, registration, and its limits
- **The anterior cingulate exercise** — the book's most instructive assignment, and a genuine test of a step everyone performs automatically (see the Worked Example below).
- **Anatomical variability as the premise** (Vogt 1995): **~65% of brain hemispheres have a single cingulate sulcus; the rest have two**, with an extra *superior cingulate sulcus* and *superior cingulate gyrus*. **And the cytoarchitectonic regions appear to correspond to the sulcal anatomy.** *So the variability is not cosmetic — it tracks the microstructural boundaries you are trying to compare across subjects.*
- **Nonlinear registration** (dipy) to the **MNI ICBM152** high-resolution template, followed by a direct visual and quantitative check of whether area 24 actually lands where it should.

---

## Worked Example — testing whether normalization does what you assume (the anterior cingulate exercise)
This is the single most transferable exercise in the book: it converts an unexamined pipeline step into a testable claim.

1. **Establish that the anatomy is variable and that the variability matters.** Read Vogt (1995): ~65% of hemispheres have one cingulate sulcus, the rest two — and cytoarchitectonic boundaries follow the sulcal pattern. **If registration smears across this, you are averaging different cytoarchitecture.**
2. **State your prediction before running anything.** Sketch, on paper, the sulcal anatomy of the medial surface of each hemisphere for *this subject*, then for the *template*, then **draw arrows from each subject structure to the part of the template it should map onto.** Determine whether your subject has single or double cingulate anatomy in each hemisphere (sagittal slices are best for this).
3. **Define the region by hand from anatomy, not from data.** In MRIcron, find a coronal slice just posterior to the genu of the corpus callosum and draw your estimate of left and right **area 24** (a, b, c combined) across five adjacent slices, using the Vogt cytoarchitectonic diagram. Scroll through slice by slice afterward to confirm you drew what you meant to. Save the VOI and convert it to NIfTI.
4. **Run the registration independently** (dipy nonlinear, subject high-res → template; 10–20 minutes) — started *before* step 2/3 so your drawing cannot be contaminated by seeing the result.
5. **Resample your hand-drawn region into template voxel space** using the same mapping.
6. **Compare against your prediction, three ways**: warped subject vs. template visually, as an overlay with varying blend; your resampled region on the template; your resampled region on the warped subject.
7. **Ask the actual question**: "Do you think the **cytoarchitecture** lines up with where you think it should be, given your drawing and the anatomy of the template and the individual subject image?"

**The generalizable method: to audit any automated preprocessing step, (a) write down what you expect it to do in terms of the anatomy or signal you care about, before running it; (b) construct an independent ground truth by hand; (c) run the step blind to your prediction; (d) compare.** The same shape works for skull stripping, motion correction, and coregistration. Notice this also inoculates against the "makes-sense" level: you cannot complete the exercise while taking anyone's word for it.

---

## Decision Rules & Judgment

- **When you notice you are at the "makes-sense" level, say so and stop treating your belief as knowledge.** The test: can you challenge what you were taught, or only repeat it?
- **"Nullius in verba" is operational, not decorative.** For any step you rely on, be able to derive it, implement it, or test it against a hand-built ground truth. If you can do none of the three, mark the claim as borrowed.
- **Organize for reproducibility from the first day of a project — rigor is hard to retrofit.** Retrofitted rigor costs more and does not transfer to the next paper; built-in rigor compounds.
- **Treat your paper as advertising and your code+data+instructions as the scholarship.** If a reader cannot regenerate the figures, you have not communicated the result.
- **Apply Feynman's leaning-over-backwards standard**: report the information that lets others judge your contribution, *including* what cuts against you — not only what points one way.
- **Expect error everywhere and design to catch it.** The relevant expertise signal is worrying more about your own mistakes as you get more experienced, not less.
- **Mask before you model.** Out-of-brain voxels produce `nan` t-statistics with p-value 0, so they survive *any* correction and appear maximally significant. Build a brain mask (e.g. Otsu) and run the GLM on in-mask voxels only.
- **Read the header separately from the data.** Datatype, dimensions, TR, orientation, and the affine live in metadata that can disagree with your assumptions; verify rather than trust.
- **Know the two halves of your t-denominator.** Estimated variance comes from the residuals; the design covariance $\vec{c}^T(\boldsymbol{X}^T\boldsymbol{X})^{+}\vec{c}$ depends only on the design and contrast. **You can improve half your statistic before scanning anyone — that is what design optimization buys.**
- **Use rank, not column count, for degrees of freedom.** Adding collinear regressors does not add information.
- **State the independence assumption whenever you use Bonferroni or Šidák.** Both derive from it; voxels violate it; that is why they are conservative here and why cluster/permutation methods exist.
- **Never `assert` for runtime error handling** — assertions are stripped under optimization and you do not control how your code is run. Raise exceptions for expected error conditions; reserve `assert` for development and tests.
- **Never test floating-point results for exact equality** — use tolerance-based comparison.
- **Write the docstring while writing the function**, because the act of explaining it to yourself improves the design. Documentation written afterward documents whatever you happened to build.
- **Move analysis out of ad-hoc cells into modules you can test.** If a step exists only as notebook state, it is neither reproducible nor checkable.
- **Before trusting a normalization, verify it against the anatomy your hypothesis depends on.** Population-level alignment does not guarantee alignment of the specific structure you will make a claim about — especially where sulcal patterns vary (cingulate: ~65% single, ~35% double) and cytoarchitecture follows the sulci.

## Key Takeaways
1. **Disorganized analysis is an epistemic problem, not a tidiness problem** — it consumes the capacity you need to ask whether you believe your own result.
2. **The "makes-sense" level is a nameable failure state**: you can repeat the reasoning but not challenge it. Recognizing you are in it is the first step out.
3. **Rigor is hard to retrofit.** Reproducibility built in from the start repays across projects; bolted on afterward it pays once.
4. **An image is an array plus an affine plus a header.** Every spatial claim you make depends on metadata you should verify rather than assume.
5. **Build the GLM from primitives once** — convolution, design matrix, contrast, t-statistic — so you know what your software is computing and where its assumptions live.
6. **Half the t-statistic is fixed by the design**, which is why experimental design is the highest-leverage statistical decision you make.
7. **Bonferroni and Šidák both assume independent tests**, and imaging violates that assumption — know the derivation so you know why cluster and permutation methods are the right response.
8. **Mask before modeling**: the most "significant" voxels in an uncorrected whole-image map may be outside the brain entirely.
