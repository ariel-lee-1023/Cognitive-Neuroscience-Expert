A smaller, later P3 peak establishes a waveform difference; it does not yet establish impaired cognition. First test whether recording, trial selection, averaging, or overlapping activity can produce the pattern.

### 1. Verify the experiment and recording

Compare physical stimuli, target probability, sequence history, interstimulus intervals, task instructions, and response requirements across groups. Check accuracy, omissions, reaction-time distributions, fatigue, sensory limitations, and relevant medication differences. Unequal task performance can change which events are averaged.

Verify event markers against actual stimulus onset and response timing, including equipment delays and jitter. Inspect raw EEG for clipping, bad channels, ocular/muscle activity, and reference contamination. Document acquisition and analysis references and channel interpolation. Inspect prestimulus activity before baseline correction: subtracting a different baseline shifts the whole waveform. Check preceding-event and response-related overlap, especially if patients respond later.

### 2. Audit rejection as both noise reduction and selection

Report presented and retained trials, artifact types, and participant exclusions by group and condition. Apply consistent, preferably group-blind rules and inspect raw versus corrected traces; correction can remove neural activity or leave contamination.

Compare retained with rejected trials by accuracy, reaction time, trial position, and stimulus history. If patients disproportionately lose difficult or inattentive trials, the retained samples represent different states. Matching trial counts does not repair this selection.

Estimate residual noise and measurement uncertainty. Repeat analyses using repeated random subsampling to comparable retained counts and relevant trial composition as a sensitivity check, retaining the full-data analysis. Fewer trials generally increase uncertainty; noise can inflate a selected positive maximum, so unequal counts alone do not predict a smaller patient peak.

### 3. Test filter distortion directly

Recover the full filter specification: cutoff definitions, order/roll-off, phase, padding, edge handling, and whether filtering preceded epoching. Compare minimally filtered data with defensible alternative settings applied consistently to both groups.

Inspect the impulse response and pass plausible P3 waveforms, neighboring components, and known timing shifts through the actual pipeline. Measure resulting amplitude and latency changes. High-pass filtering can create opposite-polarity lobes; low-pass filtering can smear peaks. Zero-phase filtering removes phase delay but can spread later activity backward in time. Identical filters can distort groups differently when their waveform shapes differ.

### 4. Separate component size, timing variability, and overlap

Inspect individual averages, scalp distributions, and trial-level ERP images. Greater latency variability can broaden and lower the average without reducing single-trial amplitude; asymmetric timing distributions or overlap can also move its maximum. Evaluate latency dispersion with a method whose recovery has been checked at these noise levels.

Distinguish P3a/P3b and neighboring slow or motor potentials using task manipulations and multiple electrodes. Matched difference waves can help, but subtraction can retain several differing processes.

### 5. Use measurements that answer the claim

Prespecify electrodes and windows independently of the observed group difference. Prefer broad-window mean amplitude over maximum amplitude when suitable, checking that delayed patient activity remains inside the window. Compare peak latency with an appropriate area-based latency measure; specify boundaries and polarity handling. Fifty-percent area latency is not onset. Neither measure solves overlap automatically.

Analyze participant-level estimates with uncertainty and multiplicity control, rather than treating grand-average maxima as observations. Specialized jackknife latency analyses require their corresponding statistical correction.

**Interpretation threshold:** If the effect survives these checks, report a reproducible difference in the task-evoked response. A particular cognitive impairment requires a discriminating task contrast and behavioral convergence; P3 size and peak timing are not universal measures of cognitive capacity or processing speed.

*Framework: Luck’s ERP Technique, supplied 2005 first edition, Chapters 2–6; Kappenman–Luck’s ERP Components, component-overlap framework. The ordered checks are my synthesis.*
