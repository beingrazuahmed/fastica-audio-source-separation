#!/usr/bin/env python3
"""Convert the authors' nine named TIFF figures from Paper Figures.zip to web PNG.

Never changes the scientific content; uses Pillow lossless PNG. Original TIFF files
are not copied to the repository. Requires Pillow (optional docs-only dependency).
"""
from __future__ import annotations
import argparse
from pathlib import Path
import io
import re
import sys
import zipfile

NAMES={
1:'fig01-workflow.png',2:'fig02-waveform-male-male.png',
3:'fig03-waveform-female-female.png',4:'fig04-waveform-male-female.png',
5:'fig05-spectrogram-male-male.png',6:'fig06-spectrogram-female-female.png',
7:'fig07-spectrogram-male-female.png',8:'fig08-mixed-audio.png',
9:'fig09-bss-comparison.png'}
MAX_FILE_BYTES=250*1024*1024
MAX_TOTAL_BYTES=900*1024*1024

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('zip_path',type=Path,help='ZIP containing Figure 1.tif ... Figure 9.tif')
    ap.add_argument('--dest',type=Path,default=Path(__file__).resolve().parents[1]/'figures')
    args=ap.parse_args()
    try:
        from PIL import Image, ImageOps
    except ImportError:
        ap.error("Pillow is required; install via: python -m pip install 'Pillow>=10,<13'")
    if not args.zip_path.is_file():
        ap.error(f'ZIP file not found: {args.zip_path}')
    with zipfile.ZipFile(args.zip_path) as archive:
        found={};total=0
        for entry in archive.infolist():
            if entry.is_dir(): continue
            name=Path(entry.filename).name
            match=re.fullmatch(r'Figure\s*([1-9])\.(?:tif|tiff)',name,flags=re.I)
            if not match: continue
            number=int(match.group(1))
            if number in found:raise ValueError(f'Duplicate Figure {number} TIFFs in archive')
            if entry.file_size>MAX_FILE_BYTES:raise ValueError(f'Figure {number} exceeds 250 MiB limit')
            total+=entry.file_size
            if total>MAX_TOTAL_BYTES:raise ValueError('Input TIFF total exceeds safety limit')
            found[number]=entry
        missing=set(NAMES)-set(found)
        if missing:raise ValueError(f'Missing original TIFF(s): {sorted(missing)}')
        args.dest.mkdir(parents=True,exist_ok=True)
        for number in sorted(NAMES):
            with archive.open(found[number]) as handle:
                payload=handle.read()
            with Image.open(io.BytesIO(payload)) as raw:
                if raw.width*raw.height>100_000_000:
                    raise ValueError(f'Figure {number} exceeds 100-megapixel safety threshold')
                raster=ImageOps.exif_transpose(raw)
                raster.load()
                if raster.mode not in {'RGB','RGBA','L'}:
                    raster=raster.convert('RGBA' if 'A' in raster.getbands() else 'RGB')
                dest=args.dest/NAMES[number]
                raster.save(dest,format='PNG',optimize=True)
                print(f'Figure {number}: {raster.width} x {raster.height} -> {dest}')
    print('All nine PNG figures generated; visually inspect them before publication.')
    return 0

if __name__=='__main__':
    sys.exit(main())
