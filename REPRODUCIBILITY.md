# Reproducibility and execution guide

## Scope and prerequisites

Python **3.12**, JupyterLab, the packages in `requirements.txt`, FFmpeg for encoded audio formats, adequate RAM and sufficient storage for local outputs. Running all 10 repetitions on ~96.63 seconds of 48 kHz audio can be resource-intensive, especially the mono-STFT NMF step. The original article's precise results depend on the original private source waveforms.

**The code is reusable, but identical results are NOT guaranteed with changed input audio.** A synthetic example is included to demonstrate execution without distributing people’s speech.

## A. Public synthetic example (no speech)

```bash
python scripts/generate_demo_audio.py
```

Start Jupyter with `FASTICA_PROFILE=demo`, `FASTICA_RUNS=1`, then run notebook cells in order. Set optional `BASE_CFG.nmf_max_iter=50` only for a faster trial; this **changes the benchmark configuration**, so do not report demo results as paper replication. To reproduce the paper's method settings, leave the existing algorithm configurations unchanged.

The demo generator deterministically creates `demo_audio/source_1.wav`–`source_3.wav` (three different synthetic signals). They are generated **locally** and ignored by Git. They are NOT a speech dataset, and no one should infer speech-separation quality from them.

## B. Own/custom audio (three tracks)

1. Obtain three separately recorded tracks that you are allowed to process. They must not be silent, nearly constant, or duplicates. Source separation in this notebook requires *reference* sources to create a simulated multichannel mixture. It cannot recover an unknown individual voice from a single pre-existing mixed recording by itself.
2. Create private folder `Raw Data/` at the repository root, or set `FASTICA_PRIVATE_AUDIO_DIR` to an absolute local folder. **Do not upload this folder.**
3. Name the three files `source_1.wav`, `source_2.wav`, `source_3.wav`, or edit `CUSTOM_AUDIO_FILENAMES` in the notebook's configuration cell. MP3 and other FFmpeg-compatible formats may also be supplied. Alternatively set `FASTICA_AUDIO_FILES` to three paths separated by `os.pathsep`.
4. Select `FASTICA_PROFILE=custom`. For a quick validation use `FASTICA_RUNS=1`; default is **10**. Adjust source labels with `CUSTOM_SOURCE_LABELS` in the notebook to document your sources accurately.
5. Run all cells. Audio is converted (FFmpeg if needed) to WAV, loaded as mono, resampled to 48 kHz, silence-trimmed, RMS-normalized and cropped to the shortest source. The controlled mixing, separation and evaluation code is then run on those three tracks.
6. Results are saved to `outputs_bss/` locally. Playback is enabled; **clear notebook outputs before every public commit**.

**Recommended input:** three nonempty, distinct tracks with several seconds of usable signal, ordinary PCM audio, and sufficient sampling quality. Very short clips, identical tracks and low-rank signals will be rejected. All new files should have appropriate rights/consent; do not publicly share derived clips containing restricted voices.

## C. Original published study

1. Obtain access to the **original private recordings** under the paper's privacy and ethics restrictions; public GitHub releases do not contain them.
2. Set profile `original` (default), and place the three files, with exactly these names, in a local `Raw Data/` directory:
   - `Sample recording 1 (Male+Male).mp3`
   - `Sample recording 2 (Female+Female).mp3`
   - `Sample recording 3 (Male+Female).mp3`
3. Keep `MIX_CFG.mix_seed=0`, `PREP_CFG`'s original main preprocessing (no bandpass/denoising), FastICA/PCA/NMF parameters, default **10** runs, and BSS Eval implementation as coded. It now sets `target_sr=48000` explicitly; this is a no-op for the original 48 kHz inputs.
4. After preprocessing, expect three source arrays of **4,638,464 samples** each (**96.63 s at 48 kHz**). After execution, compare mean±SD SDR/SIR/SAR in the summary CSV against the article. Full 10-run reproduction was not completed independently during the release audit; do not represent it as independently confirmed.

### Important mapping in the paper

| Original reference | Original source variant | Aligned FastICA display (published) |
| --- | --- | --- |
| Recording 1 | Male + Male | Separated source 2 |
| Recording 2 | Female + Female | Separated source 3 |
| Recording 3 | Male + Female | Separated source 1 |

New custom/demo audio uses labels `Source 1`, `Source 2`, `Source 3` (or `Synthetic 1`–`3`), not the original speaker-variant labels. The mapping describes post-evaluation display order, not a claim that ICA naturally fixes output order.

## Results and interpretation

`outputs_bss/` contains `metrics_per_run_{fastica,pca,nmf}.csv`, `metrics_summary_runlevel_sd_table.csv`, `mixing_matrix_A.csv`, `config.json`, `dataset_overview.csv`, a plot and a text log. This folder is ignored in Git. `config.json` records input **basenames only**, not full private paths. Do not upload files created from private speech without clearance.

`SAVE_PRIVATE_AUDIO_FILES=False` prevents extra WAV exports; `SHOW_PRIVATE_SIGNAL_FIGURES=False` avoids user-specific signal plots. `ENABLE_INLINE_AUDIO_PLAYBACK=True` lets the local author listen, but **Jupyter may embed the audio in saved cell outputs**. Run `python scripts/check_public_release.py` before every commit and remove outputs as necessary.

## Checks and troubleshooting

- **`FileNotFoundError`:** selected profile cannot find the filenames. Set correct profile and folder, generate demo files for demo mode or change `CUSTOM_AUDIO_FILENAMES`.
- **`ffmpeg not found`:** install FFmpeg and add it to PATH for MP3/FLAC/OGG. WAV files do not require FFmpeg conversion.
- **Resampling:** all sources load at 48 kHz by default; changing this target changes the computation and possibly the results.
- **Silence, too short, duplicate:** supply three adequate, distinct non-silent tracks.
- **High runtime or memory:** start with `FASTICA_RUNS=1`; use shorter audio for demos. For published comparisons, keep all paper settings.
- **Numerical output differences:** source audio changes, changed dependencies, resampling or parameters can change metrics. See `METHODS_AND_LIMITATIONS.md`.
- **`mir_eval` warning:** `bss_eval_sources` is deprecated in 0.8.2. Retained intentionally; do not silently migrate to another scoring method.
- **Safety checker failure:** remove prohibited audio files, original embedded-output HTML, or saved notebook outputs. This also applies to generated audio from human participants.

## Validation status

This package includes an automatically generated public synthetic example, structural notebook/privacy tests and a local trial procedure. Previous audits validated three private MP3s at 48 kHz with a 96.63-second aligned window and exercised the algorithm chain on short synthetic audio. Re-testing the updated configurable-input release is documented in the delivery; do not claim original-paper full numerical replication.