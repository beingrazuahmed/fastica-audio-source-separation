# Scientific methodology and limitations

## Overview

This research provides a classical three-source **blind source separation** experiment and explicitly reported evaluation protocol. The study is documented in [Engineering Reports, DOI:10.1002/eng2.70575](https://doi.org/10.1002/eng2.70575). The public repository is the code implementation; the private participant data are not distributed.

## Main pipeline

1. **Three input recordings:** decode, convert to mono, trim silence (`top_db=25`), normalize RMS, align to the minimum duration. An explicit 48 kHz target is used for portable input resampling; this was a no-op on the original 48 kHz study material.
2. **Linear instantaneous mixture:** build a fixed-seed, three-channel matrix `A` (3×3), row-normalized from Gaussian draws, and mix clean source tracks `S` using `X = A @ S` without added noise by default.
3. **Primary separation:** FastICA with parallel algorithm, logcosh contrast, unit-variance whitening, `max_iter=1000`, tolerance `1e-4` and the experiment's seeds.
4. **Baseline comparisons:** PCA on multichannel mixture with full SVD; NMF on mono STFT magnitude with NNDSVDA initialization, Kullback–Leibler divergence, multiplicative update solver and soft masks followed by inverse STFT.
5. **Aligned evaluation:** align estimated sources to the known reference order through the `mir_eval.separation.bss_eval_sources` permutation and calculate SDR, SIR and SAR. Summarize source-averaged metrics as **mean ± population SD over 10 runs** for the original benchmark.
6. **Visualization and logging:** source statistics, optional local audio playback, evaluation CSV, mixing matrix, config and comparison plot. Private speech-derived outputs should not be shared without permission.

## What a new user can and cannot reproduce

- With three different, independent authorized sources, a user **can repeat the algorithmic workflow** and compute new separation metrics against those known reference sources, provided adequate sample length and software compatibility.
- With the deterministic synthetic demo, a user can test the pipeline without any original human voices. This is a **functional demonstration**, not a replacement for the published speech experiment.
- Without the restricted source recordings, a user **cannot reproduce the exact published scores** (53.51 dB SDR for FastICA, etc.). No notebook or license can substitute for source data.
- The method **does not** solve arbitrary blind extraction from one unknown mono mixed recording; the NMF mono pathway is a baseline with reference-based scoring.

## Limitations and responsible reporting

This work assumes three known, reasonably independent input tracks and creates a synthetic linear instantaneous mixture. It is not tested here on reverberant rooms, convolutive mixing, microphone arrays, unknown external mono mixtures, or large-scale out-of-distribution speech datasets. New recordings can fail to separate well; ICA has scaling/permutation ambiguity; PCA and NMF are baselines with different signal representations. Preprocessing, STFT resolution, audio duration, model settings and dependency versions affect the results. BSS Eval's legacy `mir_eval` implementation is deprecated but preserved for method comparability. Never report private-study performance as demo performance.

## Original figure correspondence (published)

- Figure 1: end-to-end research pipeline.
- Figures 2–4: waveform comparisons for male+male (reference 1 → displayed output 2), female+female (reference 2 → output 3), male+female (reference 3 → output 1).
- Figures 5–7: accompanying spectrogram comparisons of those same variants (printed caption of Figure 6 says "Waveform" but image is the spectrogram; the reference/output pairing remains correct).
- Figure 8: waveform and spectrogram of mixed audio.
- Figure 9: mean±SD BSS comparison over methods.

These are **published experiment visuals**, not promised output for arbitrary custom signals. For the definitive figures, see the journal article.