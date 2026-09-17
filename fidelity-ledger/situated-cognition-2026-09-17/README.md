# Situated-cognition extension — 2026-09-17

Three supplied books extend the existing cognitive-neuroscience expert from 18 to 21 sources. The repository's established architecture is preserved: root SKILL.md, one canonical reference per source, and the discovery symlink. Earlier source references, demonstrations, and historical evaluations remain unchanged.

- [Source editions and hashes](source-provenance.json)
- [Coverage, selection, and sampled exceptions](coverage-audit.md)
- [Selected research checks](research-checks.md)
- [Reading ledger](reading-ledger.json) and [computed report](reading-report.json)
- [Frozen scenario suite](acceptance-suite.json) and [editorial evaluation](evaluation.md)
- [Validation summary](validation.md), [generic validator](validation.json), and [existing-architecture checks](existing-architecture-check.json)
- [Runtime hashes](runtime-manifest.json)

The generic validator rejects the repository's pre-existing demos, maintenance, scripts, and tests directories; these are preserved under the existing-architecture override. This is not reported as a clean generic-validator pass. Reading coverage is sampled and includes upper-bound counts for truncated emissions, not a verified full read. Research checks are bounded supplements. Fresh-context behavioral comparisons and behavioral regression runs are unrun, so no measured model-performance improvement is claimed.
