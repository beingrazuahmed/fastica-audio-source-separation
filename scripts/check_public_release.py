#!/usr/bin/env python3
"""Reject accidental release of participant/audio-derived content."""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "FastICA_Audio_Source_Separation.ipynb"
SKIP = {".git", ".venv", "venv", "__pycache__", ".ipynb_checkpoints"}
PROHIBITED_DIRS = {"Raw Data", "Data", "demo_audio", "outputs_bss"}
AUDIO_EXTS = {".mp3", ".wav", ".flac", ".ogg", ".aac", ".m4a", ".aiff", ".aif", ".wma", ".opus", ".mp4", ".webm"}
ISSUES = []

try:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4:
        ISSUES.append("Expected Jupyter notebook v4 format")
    for i, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            ISSUES.append(f"Notebook cell {i} has embedded saved outputs")
        if cell.get("execution_count") is not None:
            ISSUES.append(f"Notebook cell {i} has a saved execution count")
        try:
            compile(''.join(cell['source']), str(NOTEBOOK), 'exec')
        except SyntaxError as e:
            ISSUES.append(f"Notebook cell {i} syntax error: {e}")
except Exception as exc:
    ISSUES.append(f"Unable to verify notebook: {exc}")

for p in ROOT.rglob("*"):
    if not p.is_file():
        continue
    parts = p.relative_to(ROOT).parts
    if any(part in SKIP for part in parts):
        continue
    if any(part in PROHIBITED_DIRS for part in parts):
        ISSUES.append(f"Sensitive/generated directory: {p.relative_to(ROOT)}")
    if p.suffix.lower() in AUDIO_EXTS:
        ISSUES.append(f"Audio/media file in public release: {p.relative_to(ROOT)}")
    if p.suffix.lower() in {".html", ".htm"}:
        ISSUES.append(f"HTML may contain embedded audio: {p.relative_to(ROOT)}")
    if p.suffix.lower() in {".ipynb", ".py", ".json", ".md", ".txt", ".yaml", ".yml"}:
        try:
            payload = p.read_text(encoding="utf-8")
            if re.search(r"C:\\Users\\[^\\]+",payload,re.I):
                ISSUES.append(f"Real Windows user profile path: {p.relative_to(ROOT)}")
        except (UnicodeError, OSError):
            pass

if ISSUES:
    print("PUBLIC RELEASE CHECK FAILED:")
    for issue in sorted(set(ISSUES)):
        print("  -", issue)
    sys.exit(1)
print("PASS: notebook code compiles, no embedded outputs or participant media in public files")
