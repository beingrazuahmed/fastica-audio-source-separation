# Published research figures — FastICA

Nine figure images from the open-access article:

Ahmed, M. R., Mauya, J., Reza, M. S., & Amin, R. (2026). *Sophisticated Audio Source Separation: A Statistical Exploration of Clarity and Precision With FastICA*. *Engineering Reports*, 8(1), e70575. https://doi.org/10.1002/eng2.70575

The original TIFF images were supplied by the author; the optimized PNG versions are intended for browser display, preserving the scientific graphics and publication numbering. All nine images are prepared for addition to this folder.

| Figure | File | Original-to-separated comparison |
| --- | --- | --- |
| 1 | `fig01-workflow.png` | Research workflow |
| 2 | `fig02-waveform-male-male.png` | Recording 1 → separated source 2 |
| 3 | `fig03-waveform-female-female.png` | Recording 2 → separated source 3 |
| 4 | `fig04-waveform-male-female.png` | Recording 3 → separated source 1 |
| 5 | `fig05-spectrogram-male-male.png` | Recording 1 → separated source 2 |
| 6 | `fig06-spectrogram-female-female.png` | Recording 2 → separated source 3 |
| 7 | `fig07-spectrogram-male-female.png` | Recording 3 → separated source 1 |
| 8 | `fig08-mixed-audio.png` | Mixed-audio waveform and spectrogram |
| 9 | `fig09-bss-comparison.png` | BSS metric comparison |

See [figure_manifest.csv](figure_manifest.csv) for the paper's printed captions. Figure 6's published caption says “Waveform”; the plotted figure is a spectrogram. Do not change the figure numbering or original/separated-source mapping.

**Copyright and attribution:** © The Author(s), published by Wiley in *Engineering Reports* under the article's Creative Commons Attribution licence. Reproduce with the required article credit. The repository MIT software licence does not replace the article's figure licence. The figure graphics do not grant permission to release underlying participant audio.

To regenerate PNGs locally using the TIFF ZIP, run:
```bash
python -m pip install 'Pillow>=10,<13'
python scripts/import_figures.py "Paper Figures.zip"
```
