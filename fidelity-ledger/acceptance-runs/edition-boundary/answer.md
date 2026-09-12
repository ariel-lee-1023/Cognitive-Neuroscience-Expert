I cannot establish what Luck added in the second edition from the supplied material. The ERP reference explicitly covers the **2005 first edition**, with eight chapters, and says the second edition was neither supplied nor verified. A reliable comparison needs the second edition itself or an authoritative edition comparison.

Likewise, this source does not establish numerical acquisition settings for a current amplifier. Its equipment specifications and impedance preferences are historical, and no amplifier model or current manual is supplied. I would not turn them into a present-day sampling rate, filter cutoff, gain, or impedance threshold.

What the first-edition framework does support is how to choose and check those settings:

- Define the ERP time scale and bandwidth you need to preserve, then consult the specific amplifier's current documentation for compatible acquisition settings.
- Choose sampling and acquisition anti-alias filtering together. The retained signal must be adequately band-limited below half the sampling rate; a nominal cutoff alone does not establish sufficient attenuation above that limit.
- Check input range, resolution, noise, and clipping. Assess electrode impedance and imbalance against the particular amplifier's input properties and electrode system.
- Document the acquisition reference, montage, and actual filter characteristics. Assess temporal distortion as well as frequency attenuation, particularly for onset measurements.
- Verify physical stimulus onset against recorded event codes over realistic session durations, distinguishing constant delay, jitter, and drift.

These are source-supported selection and validation principles, not a verified current device preset. The missing sources are the second-edition text and the current manual for the amplifier and electrode configuration in use. Internet verification was outside the permitted scope.

Source: supplied `references/reference-luck-erp-technique.md`, “Edition boundary,” Chapters 3, 5, and 8, and “Decision Rules & Judgment.”
