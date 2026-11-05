# Data availability, privacy, ethics and permissions

## Original human recordings — restricted

The research uses primary recordings of consenting participants from Pabna University of Science and Technology. The [published article](https://doi.org/10.1002/eng2.70575) says:

> The data that support the findings of this study are available on request from the corresponding author. The data are not publicly available due to privacy or ethical restrictions.

The recorded speakers' voices, any raw/processed audio, synthetic *mixtures containing their speech*, separated outputs, and notebook results with embedded playback are subject to this restriction. The public repository does not contain or license those assets. Publication of the article or its waveform figures **does not authorize distribution of the underlying voice recordings**.

## How to request restricted data

Consult the Data Availability Statement and contact a corresponding author of the published article through the journal. Requests may require participant consent, institutional approval and appropriate privacy safeguards. The code maintainer's email is `razuahmed038@gmail.com` for code questions, but contacting the maintainer does not confer permission to obtain or distribute the recordings. No guarantee of data release is made.

## Use of custom audio

You may run the public code with **three distinct recordings** that you have the rights and, where needed, consent to use. The software license does not grant rights in third-party recordings. Never assume that separation, anonymization or frequency-domain processing makes voice recordings non-identifiable. Do not upload clips of other people or their derived outputs without appropriate permissions.

## Synthetic demo

`scripts/generate_demo_audio.py` creates three mathematical, non-human speech-like signal alternatives as **non-speech synthetic signals** for local functional demonstration. They are not sourced from participants, copyrighted music or third-party recordings. Generated `demo_audio/` files are ignored by Git and may be recreated by any user.

## Data processing behavior

The notebook processes recordings **locally** and does not include remote upload or data transmission. FFmpeg may write intermediate `.canonicalized.wav` files next to your local audio; the notebook may create local generated outputs and may embed audio in **Jupyter notebook output cells** when you execute playback. Clear all notebook outputs before uploading to a public repository. `.gitignore` helps prevent accidental commits but is not an authorization mechanism. Run `python scripts/check_public_release.py` before publishing.

## Material-specific licenses

- **Repository source code/scripts and author-written documentation:** MIT (see `LICENSE`).
- **Published paper:** governed by its own publisher/license terms, not MIT.
- **Restricted audio and derivatives:** **not distributed** or licensed by this repository.
- **Third-party dependencies:** remain under their respective licenses.
- **User-supplied custom recordings:** retain their owners' rights and applicable privacy restrictions.