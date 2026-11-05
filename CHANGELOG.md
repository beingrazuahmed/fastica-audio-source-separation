# Changelog

## 1.0.0 — 2026-11-05 (initial GitHub release candidate)

- Reconstructed the author's original HTML-exported Jupyter research code as a clean notebook without media outputs.
- Preserved main published algorithms: FastICA, PCA, mono-STFT NMF, fixed-seed 3×3 mixture, legacy BSS Eval, 10-run defaults and original speaker-source mapping.
- Added `original`, `custom` and `demo` profiles; portable audio paths; generic labels for changed source files; explicit 48 kHz input resampling and input validity checks.
- Kept local inline audio playback enabled; disabled private WAV exports and private signal plots by default, with output-free commit rules.
- Added deterministic synthetic demo generator, programmatic safety checks, six tests, CI workflow, MIT code license, citation metadata, privacy/ethics/data permissions, author credits, contact, ORCID, contribution and reuse instructions.
- Added figure import instructions and nine-figure publication manifest (original TIFF ZIP and converted PNGs still pending).
- Documented exactly what was tested and what remains unverified (complete original 10-run numerical replication).

No new numerical research results are claimed by this release.