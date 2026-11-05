#!/usr/bin/env python3
"""Generate deterministic mathematical example signals; no speech or third-party audio.

Requires only NumPy and SoundFile from requirements.txt. Outputs are ignored by Git.
These distinct tracks exercise a known-reference synthetic 3x3 mixture and BSS
pipeline, but are NOT the original article's human recordings or validated results.
"""
from pathlib import Path
import argparse
import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]


def generate(destination: Path, seconds: float = 2.0, sr: int = 48000) -> list[Path]:
    if seconds < 0.5 or seconds > 30:
        raise ValueError("seconds must be between 0.5 and 30")
    if sr < 8000 or sr > 96000:
        raise ValueError("sample rate must be between 8000 and 96000")
    destination.mkdir(parents=True, exist_ok=True)
    n = int(round(seconds * sr))
    t = np.arange(n, dtype=np.float64) / sr
    rng = np.random.default_rng(20261105)
    frequencies = (190, 330, 510)
    paths = []
    for k, f0 in enumerate(frequencies):
        envelope = (0.6 + 0.25*np.sin(2*np.pi*(1.3+0.7*k)*t + 0.5*k))
        carrier = np.sin(2*np.pi*f0*t + 0.13*k) + 0.35*np.sin(2*np.pi*(f0*2.1)*t)
        noise = 0.015*rng.standard_normal(n)
        y = 0.25 * (envelope*carrier + noise)
        path = destination / f"source_{k+1}.wav"
        sf.write(path, y.astype(np.float32), sr, subtype="PCM_16")
        paths.append(path)
    return paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=float, default=2.0)
    parser.add_argument('--sr', type=int, default=48000)
    args = parser.parse_args()
    for p in generate(ROOT/'demo_audio',args.seconds,args.sr):
        print(f"Created local synthetic, non-speech track: {p.relative_to(ROOT)}")
    print("Set FASTICA_PROFILE=demo and FASTICA_RUNS=1, then run the notebook.")


if __name__ == '__main__':
    main()
