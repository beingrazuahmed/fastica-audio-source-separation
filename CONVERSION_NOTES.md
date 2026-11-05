# Conversion and repository preparation notes

**Input:** The user's original HTML-exported Jupyter notebook inside `FastICA by Razu.zip` and the subsequent Version 3 playback-enabled notebook. Original recordings remain restricted and are **not** copied here.

- Extracted the original Python research code into 13 organized executable code cells; stripped all saved HTML/Jupyter media outputs.
- Preserved the main scientific algorithms: FastICA, PCA and mono-STFT NMF, 3×3 fixed-seed mixing, BSS Eval with permutation alignment, SD/SDR/SIR/SAR aggregation, ten-run defaults and original speaker-variant mapping.
- Added three run profiles: `original`, `custom`, `demo`. New custom and synthetic files are labeled by source rather than incorrectly called the published male/female variants.
- Converted local path handling to a portable private-data folder, with optional custom file paths. The study's original 48 kHz data are unchanged by explicit common-rate resampling, while custom recordings are aligned at 48 kHz.
- Added validation for missing/silent/too-short/duplicate or linearly dependent tracks, and prevented same-name WAV collision during FFmpeg canonicalization.
- Kept local audio playback enabled on the author's request but cleared saved notebook output and disabled private WAV export and signal-specific plots by default.
- Improved private result metadata by recording **file basenames**, not absolute local paths. All outputs and generated audio are `.gitignore`-excluded.
- Bundled a deterministic, generated non-human signal example, a release checker, standard-library tests, GitHub Actions, MIT software license, citation records, ethics/data policy, contact/ORCID, usage and contribution guidance.
- Added no new published experimental results. The paper's full original ten-run computation has **not** been independently re-executed. New audio produces new metrics, not the published article's metrics.
- Before public use, confirm that Md. Razu Ahmed or other relevant rights holders have authority to release all authored source code under MIT. Repository code licensing **does not override participant audio restrictions**.

## Previous checks

Prior release audits confirmed that the original 3 private MP3 inputs load at 48 kHz and align to 4,638,464 samples (96.63 s). Short synthetic smoke tests exercised mixing, FastICA, PCA, NMF and evaluation. Current-release tests are described in the delivery report.