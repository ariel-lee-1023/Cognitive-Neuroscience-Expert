# How We Learn: Why Brains Learn Better Than Any Machine … for Now — Stanislas Dehaene
**Format**: md | **Pages**: ~407 (extractor estimate, not printed pagination) | **Sections**: 10 chapters | **Depth**: study | **Type**: text

**Source edition:** Viking, first American edition, 2020, based in part on the French book published in 2018. The supplied Markdown has ten chapters in three parts, plus an introduction and conclusion; the extractor's 13 detected headings are not 13 chapters. The English title's machine comparison concerns its period, not the capabilities of current AI. Locators use chapter/subsection names or a named experiment in the supplied text.

## Mental Model (read first)
Learning changes an internal model through structured experience. The learner brings prior organization, explores hypotheses, uses error information, and consolidates what has been acquired. Dehaene's **four pillars of learning — attention, active engagement, error feedback, consolidation** connect these mechanisms to teaching. They are a framework for choosing and examining learning conditions, not a guarantee that a particular lesson works or a substitute for measuring retention and transfer.

**Use for:** planning study, interpreting failed retention, assessing educational claims, designing practice and feedback, and comparing biological and artificial learning. Combine [O'Reilly](reference-oreilly-comp-cog-neuro.md) for complementary learning systems and implemented mechanisms, [Dayan & Abbott](reference-dayan-abbott-theoretical-neuroscience.md) for formal learning rules, [Reading in the Brain](reference-dehaene-reading-brain.md) or [The Number Sense](reference-dehaene-number-sense.md) for domain-specific representations, and [Hernán & Robins](reference-hernan-robins-causal-inference.md) for a claimed intervention effect.

## Frameworks & Structure

### Chapters 7–10 — The four pillars as a design framework
**Locator:** Part Three, “The Four Pillars of Learning”; Chapters 7–10 and “Reconciling Education with Neuroscience.”

| Pillar | What changes in the learner | Design implication | What can mislead |
|---|---|---|---|
| **Attention** | Relevant information is selected and amplified | Make the target discrimination clear, manage competing demands, and check what the learner attends to | Looking at the screen or being entertained does not establish processing of the target |
| **Active engagement** | The learner generates, predicts, explains, or tests a representation | Elicit an answer or explanation before revealing one, at a manageable difficulty | Physical movement, clicking, or unguided discovery is not automatically cognitive engagement |
| **Error feedback** | The discrepancy between expectation and outcome informs a revision | Give specific corrective information and another chance to use it | A score or punishment alone may reveal little about what to change |
| **Consolidation** | Acquired representations become more stable, accessible, or efficient | Revisit material over time, retrieve it, and provide conditions for sleep and practice | Smooth performance immediately after rereading can conceal poor delayed retention |

**Editorial application:** choose the desired later behavior first. Diagnose whether failure arose from target selection, shallow engagement, uninformative correction, insufficient retrieval, or a mismatch between practice and transfer. Several constraints can coexist. The pillars do not license assigning every failure to motivation or adding all four as decorative lesson labels.

### Chapter 1 — Seven definitions of learning
**Locator:** “Seven Definitions of Learning,” seven bold subsection headings.

The definitions emphasize complementary aspects of learning, rather than seven mutually exclusive brain modules:

1. **Learning is adjusting the parameters of a mental model.** Experience changes a mapping or representation used for prediction/action. Specify the parameter and the prediction it changes; fitting data does not establish the brain's implementation.
2. **Learning is exploiting a combinatorial explosion.** A limited set of components or parameters can yield many configurations. Combinatorial capacity makes rich representation possible but creates a search problem; it is not a measure of actual knowledge.
3. **Learning is minimizing errors.** A discrepancy between prediction and outcome can guide adjustment. Gradient descent illustrates one way to reduce a loss; it neither guarantees a global optimum nor proves that the brain performs standard backpropagation.
4. **Learning is exploring the space of possibilities.** Local improvements can become trapped. Exploration, variable examples, and changing hypotheses can reveal alternatives; indiscriminate randomness is not a complete teaching method.
5. **Learning is optimizing a reward function.** Reinforcement can select actions without specifying each desired output. Separate reward from a detailed teaching signal and consider how credit is assigned to earlier actions.
6. **Learning is restricting search space.** Structural assumptions and reuse of computations reduce the possibilities that must be learned. Invariance or shared parameters can help if the assumptions fit the task; excessive or wrong constraints can obstruct learning.
7. **Learning is projecting a priori hypotheses.** Prior structure and expectations make induction possible. A Bayesian description combines a prior with evidence, but it does not identify a unique neural algorithm or show that a child explicitly calculates probabilities.

**Formal bridge, editorial notation:** a simple delta rule has V_(t+1)=V_t+α(r_t−V_t), where V is an expectation, r an observed outcome, and α an update rate. In a compound-cue Rescorla–Wagner model, the discrepancy depends on the sum of predictions by the present cues, not merely one cue's value. These are specified models of learning, not universal equations for every synaptic change or every classroom error. Use the formal references for assumptions, competing algorithms, and recovery.

### Chapter 2 — Why our brain learns better than current machines
**Locator:** Chapter 2, list beginning “Learning abstract concepts,” discussions of hypotheses, social learning, and Sherlock Holmes.

The book emphasizes abstraction, compositional representations, efficient learning from limited examples, uncertainty, exploration, and the use of communicative information. These are comparison dimensions, not a single brain-versus-machine leaderboard. Translate an assertion such as “learns faster” into data efficiency, interaction cost, compute/energy, prior experience, generalization, or robustness under distribution shift.

**Abstraction and recombination:** successful recognition of familiar examples need not show that the learner has extracted the rule needed for a new combination. Test novel cases that preserve the relevant relation while changing superficial features. Conversely, success on one transfer task does not establish domain-general reasoning.

**Negative evidence:** an event that should have occurred under a hypothesis but did not occur can be informative. The inference depends on what the learner could reasonably expect and observe. An absent signal is not evidence of absence if the detection procedure was weak.

**Historical boundary:** claims about what “current machines” lack refer to the 2018–2020 setting. Do not infer a present-day ranking, impossibility theorem, or absence of a capability from the title. Comparing to a named current model requires current primary evidence and a specified task/budget. Human prior development and a machine's pretraining both count when defining the comparison.

### Chapter 3 — Babies' invisible knowledge
**Locator:** “Babies' Invisible Knowledge,” examples involving objects, number, probability, people, and language.

Infants can bring structured expectations to learning before being able to explain them or act fluently. Dehaene argues against an unrestricted blank-slate account. Discrimination, anticipatory looking, habituation, and surprise paradigms reveal different aspects of that competence; they do not show an explicit adult theory in the infant's head.

**Prior knowledge versus prenatal and postnatal experience:** early emergence can constrain how much learning an account requires, but an early response is not by itself a direct genetic assay. Distinguish inherited biases, self-organization, sensory history, and test-specific learning. Likewise, an ability being learnable does not show that the starting architecture is unconstrained.

**Social learning:** the learner interprets what another person intends to communicate, rather than simply pairing every heard word with every visible object. Teaching can guide attention and hypothesis selection. It can also narrow exploration if learners reasonably assume the demonstration exhausted what matters; the instructional context changes what they infer from the same evidence.

### Chapter 4 — The birth of a brain
**Locator:** “The Birth of a Brain,” cortical organization, connectivity, and developmental variation.

The book treats brain development as organized construction influenced by genetic programs, local interactions, and developmental conditions. Large-scale architecture and connection patterns constrain subsequent learning. Genes do not contain a verbatim list of learned words, and experience does not redesign every long-distance pathway without constraint.

**Self-organization:** local interaction rules can produce organized patterns without a detailed blueprint for every element. This is a mechanistic idea to specify, not a replacement for identifying the relevant developmental processes. **Variation** in anatomy and developmental trajectory need not map one-to-one onto a learner's observable performance.

**Boundary for disability claims:** early candidate-gene/neural-migration accounts in the book do not justify deterministic diagnosis. Brain-based variation and trainability can coexist. For current reading-disability genetics, use the explicitly later evidence and limits in [Reading in the Brain](reference-dehaene-reading-brain.md); do not repeat historical family-risk figures as an individual prediction.

### Chapter 5 — Nurture's share: plasticity has conditions
**Locator:** “Nurture's Share,” synaptic plasticity, perceptual learning, sensitive periods, and deprivation examples.

**Synaptic plasticity** includes changes in connection efficacy and structure; learning-related changes can also involve dendrites, axons, and myelination. A task improvement alone does not identify which biological change occurred. **Hebbian learning** links activity relationships to changed connections in a family of rules; it is not equivalent to the entire error-feedback account.

**Sensitive periods** are intervals of heightened plasticity that differ by system and kind of experience. The book contrasts strong early malleability with continued, more constrained learning later. Do not turn its developmental sketches into a universal age cutoff after which learning is impossible. Critical/sensitive periods for a specific function need evidence for that function and exposure history.

**Enrichment and deprivation:** effects depend on what input or practice was absent, the developmental stage, and the task. An animal deprivation experiment does not establish the dosage or efficacy of a human educational intervention. A broad “more stimulation is better” rule ignores attention, stress, sleep, and the content of the activity.

### Chapter 6 — Recycle your brain
**Locator:** “Recycle Your Brain,” literacy and mathematical education examples.

**Neuronal niche:** a cultural invention is learned through circuits whose prior operations and connections can support the new demand. Learning changes the system while retaining constraints from its history. The account predicts neither arbitrary rewiring nor fixed inability to acquire a new practice.

Reading and exact mathematics connect acquired symbols with preexisting visual, linguistic, spatial, and quantity processes. Shared regional recruitment does not imply that their representations and algorithms are identical. For a learning difficulty, identify the specific mapping that must change rather than prescribing generic “brain training.”

**Causal boundary:** differences between schooled and unschooled groups can motivate hypotheses about education, but schooling co-varies with many experiences. Claims that literacy caused a particular change need longitudinal/intervention evidence or a defensible causal design, not an appealing recycling explanation alone.

### Chapter 7 — Attention: select the information that should be learned
**Locator:** “Attention,” Posner's three systems, selective amplification, executive attention, multitasking, and pedagogical cues.

The book distinguishes **alerting** (readiness/when to attend), **orienting** (selection of relevant information), and **executive attention** (control of operations and competing demands). Asking a tired learner to “focus harder” does not identify which function is limiting. Nor does a gaze trace establish what distinction was encoded.

**Selection changes learning:** the same display can teach different things depending on the feature attended. State the relevant distinction, use cues that direct processing toward it, and test whether learners can apply it without those cues. A striking but irrelevant animation may absorb attention while leaving the intended rule poorly learned.

**Central bottlenecks:** unfamiliar controlled operations compete more than well-practiced routines. Task switching can feel fluent while imposing waiting time or omissions. Reduce concurrent demands during acquisition, while avoiding a universal claim that no two processes can run together. Automatization can change interference, but it must be demonstrated in the relevant tasks.

### Chapter 8 — Active engagement: generate a model, not just a movement
**Locator:** “Active Engagement,” Held–Hein carousel experiment, critique of pure discovery, curiosity, metacognitive monitoring.

**Active inference in learning, in the ordinary sense used here:** make a prediction, choose a response, explain a relation, or test a hypothesis and compare it with the result. This wording does not identify the book with a specific contemporary Active Inference formalism. Physical activity can accompany engagement, but movement or clicking alone does not establish learning of the intended concept.

**Guided activity versus pure discovery:** Dehaene explicitly rejects equating active engagement with leaving novices to rediscover a domain without help. Clear explanation and worked demonstrations can coexist with learner prediction and application. Choose guidance according to prior knowledge, error patterns, and task complexity; do not classify an entire teaching tradition by a single label.

**Curiosity / expected learning progress:** learners seek information they expect to make sense of. Material can be uninteresting because it is already mastered or because it seems impenetrable. Break an excessive challenge into a tractable question; let a knowledgeable learner progress. This is a mechanism-oriented hypothesis for adapting difficulty, not a calibrated formula prescribing a universal success rate.

**Metacognition:** confidence in knowing something can diverge from the ability to retrieve or explain it. Require an attempt before showing the solution and compare confidence with actual performance. Familiarity from repeated exposure is weak evidence of transferable mastery.

### Chapter 9 — Error feedback: make the discrepancy informative
**Locator:** “Error Feedback,” Rescorla–Wagner/classical conditioning, grades, retrieval practice, and distributed practice.

**Prediction error** concerns a gap between expectation and observed outcome, not just an overt mistake. In the Rescorla–Wagner account, a fully predicted outcome produces little update; this explains why merely repeating paired events is not always sufficient. A learner who gets a problem correct by guessing can still need corrective explanation, while an informative failed attempt can improve subsequent performance.

**Feedback content:** identify the relevant discrepancy and how to correct it. A grade collapses many possible errors into one number and may arrive too late to reconnect with the original reasoning. An answer explanation, a contrastive example, and a new attempt can reveal whether the learner revised the right representation. Non-punitive feedback aims to sustain willingness to attempt and update; humiliation is not an instructional mechanism.

**Retrieval practice / testing effect:** retrieving an answer can strengthen later access and reveal gaps. It differs from using tests only for ranking. Provide appropriate correction when attempts are wrong and adjust the task if the learner lacks prerequisites. A quiz made of familiar options may measure recognition more than the later target behavior.

**Spacing / distributed practice:** spreading encounters across time can improve durable learning relative to massing under suitable conditions. The interval should relate to the desired retention horizon and current success; the book does not supply a universally optimal schedule. Compare delayed retrieval and transfer, not just how easy a review session felt. Interleaving task types and spacing repetitions are related design choices but not identical manipulations.

### Chapter 10 — Consolidation: stabilize and free capacity
**Locator:** “Consolidation,” reading automatization, sleep/replay, and hidden-rule experiments.

**Automatization** can make a formerly slow, controlled operation efficient enough to support a larger task. In reading, improved access to word forms reduces the burden of serial decoding. Practice effects are task- and item-dependent; a flatter word-length function in a studied range is not a universal absence of length effects.

**Sleep and reactivation:** the book discusses offline reactivation and changes in memory organization as mechanisms supporting consolidation. Pair this with the existing complementary-learning-systems account for fast episodic encoding and slower integration. Sleep provides conditions for learning-related change; it does not replace initial encoding or prove that complex new material can be mastered by playing it to a sleeping person.

**Test alternative explanations:** time of day, elapsed time, interference, initial learning, and sleep opportunity must be considered in interpreting a sleep/wake comparison. An observed retention benefit does not uniquely identify replay or hippocampal transfer. Discovering a hidden rule after sleep in one task is evidence about that paradigm, not a guarantee of overnight creativity or improvement for every kind of memory.

## Worked Example
**Reconstruction from Chapter 1, prism adaptation.** A visual displacement makes a reach miss its target. Repeated reaching with information about the error produces compensatory adjustment. After the displacement is removed, an error in the opposite direction reveals that the mapping has changed: the learner was not merely succeeding by the original mapping.

This connects an internal parameter, a perturbation, feedback, and an aftereffect. The book uses it to illustrate model adjustment. The editorial caution is that an aftereffect constrains the explanation but does not identify the exact synapses changed, prove a single learning rate for all tasks, or rule out every explicit strategy. Ask what should generalize to another target or effector before claiming a general learning mechanism.

## Decision Rules & Judgment

- Specify what the learner should do after a delay and in a new case before selecting an activity.
- If immediate fluency and delayed performance diverge, test retrieval and transfer, then examine spacing, feedback, and consolidation conditions.
- If learners are busy but cannot explain or apply the rule, redesign the cognitive action rather than adding motion or clicks.
- If novice exploration repeatedly fails, supply structure or an example, then ask for a prediction and application; engagement is compatible with guidance.
- If errors persist, make feedback diagnostic and verify a changed strategy; a repeated score alone cannot tell the learner what to repair.
- If a biological explanation is used to sell instruction, separate mechanistic plausibility from evidence that this intervention improves a defined outcome in this population.
- If a developmental constraint is invoked, identify the function and exposure history; avoid universal age ceilings or biological fatalism.
- If comparing brains and AI, state the learning criterion, resources, and source vintage, and verify the contemporary system rather than relying on the book's title.

## Key Takeaways

1. Learning requires a model, structured evidence, and conditions for useful change; exposure alone is an incomplete explanation.
2. Attention, engagement, feedback, and consolidation identify practical questions, not a guaranteed recipe.
3. Guided explanation and active learner effort can reinforce one another.
4. Durable retention and transfer are stronger targets than immediate familiarity.
5. Brain mechanisms motivate hypotheses about instruction; causal outcome evidence evaluates an intervention.

**Coverage note:** All ten chapters and the concluding educational synthesis are represented. The seven definitions and four pillars retain their source formulations. Extensive anecdotes, historical AI rankings, exact sensitive-period ages, unsupported universal classroom effect sizes, and book-era genetic predictions are omitted or bounded. The delta-rule notation and instructional decision procedure are editorial connections to the existing library, not copied equations or a validated intervention package.
