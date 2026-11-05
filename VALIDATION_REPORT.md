# Verification report — 5 November 2026

## Validation evidence for this public code release

| Test | Result | What was actually checked |
| --- | --- | --- |
| Jupyter notebook JSON and schema | **Passed** | Notebook v4 validates with `nbformat`; 27 cells including 13 compiled executable code cells; all saved code-cell outputs and counters cleared |
| Public-release privacy checker | **Passed** | No original participant audio, no MP3/WAV derivatives, no HTML-exported embedded media and no stored notebook outputs in packaged repository |
| Standard-library test suite | **6/6 passed** | Notebook code parsing; run profiles and method symbols; privacy switches; documentation files; release checker |
| Citation metadata | **Parsed** | `CITATION.cff` YAML parser accepted metadata, publication DOI, four paper authors, ORCID and software author |
| End-to-end generated demo | **Passed** | Three generated non-human 48 kHz WAVs, one run, local playback call, FastICA, PCA, NMF, BSS alignment, summary CSV, comparison PNG and config |
| End-to-end changed audio | **Passed** | Three differently named WAV files, **22.05 / 32 / 44.1 kHz**; one stereo source; different source durations. Each resampled and aligned at **48 kHz**, with CSV/PNG outputs |
| Playback on, private WAV export off | **Passed** | `ENABLE_INLINE_AUDIO_PLAYBACK=True`, `SAVE_PRIVATE_AUDIO_FILES=False`; no output WAVs created by the notebook. Test suppressed actual user-visible player rendering while exercising playback calls. |
| Original study input preprocessing (previous audit) | **Passed previously** | Three authorized original MP3s loaded at 48 kHz; aligned to **4,638,464 samples, 96.63 seconds**. Input files are not distributed. |
| Original complete 10-run published evaluation | **Not independently rerun** | Published SDR, SIR, SAR table comes from the peer-reviewed article, not the synthetic test. |
| Full dependency matrix / Windows playback UI | **Not independently certified** | Functional tests ran using the available Linux environment and installed packages; local Windows/Jupyter UI must be tested on the author's desktop. |

| Nine figure PNG assets | **Pending author upload** | `figures/` is prepared with a nine-file manifest and optional TIFF ZIP importer; no image files have been invented or extracted from the publisher PDF. |

## Interpretation

**The same computational procedure is reusable on three different known reference tracks**, subject to adequate signal quality, input permissions and compatible dependencies. That does not mean the output or published metrics are identical for different audio, nor that arbitrary unknown acoustic mixtures can be separated. Because the original restricted data are not included, the paper's complete exact-number reproducibility is conditional upon authorized access.

Recheck all public files and `git diff --cached` before a first GitHub push; the notebook may contain embedded speech if a collaborator commits executed outputs after playing local recordings.