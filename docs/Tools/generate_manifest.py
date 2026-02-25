"""
Scans the tools folder for image files and generates manifest.json.
Run this script whenever you add or remove images in the tools folder.
Usage: python generate_manifest.py   (run from repo root or from docs/tools)
"""
import os
import json
import re

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
# Folder name for URLs (must match actual folder: Tools)
TOOLS_FOLDER = "Tools"
MANIFEST_PATH = os.path.join(TOOLS_DIR, "manifest.json")
TOOLS_DATA_JS_PATH = os.path.join(TOOLS_DIR, "tools-data.js")
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def filename_to_display_name(filename: str) -> str:
    """Convert filename (without path) to a display label."""
    name = os.path.splitext(filename)[0]
    # Remove trailing " 2" or " 1" (duplicate file suffix), not "MS 365"
    name = re.sub(r"\s+[12]$", "", name)
    # Replace hyphens/underscores with spaces and title-case
    name = name.replace("-", " ").replace("_", " ")
    return name.strip().title() if name.strip() else filename


def main():
    entries = []
    for f in sorted(os.listdir(TOOLS_DIR)):
        if f.startswith(".") or f == "manifest.json" or f == "generate_manifest.py":
            continue
        ext = os.path.splitext(f)[1].lower()
        if ext not in IMAGE_EXTENSIONS:
            continue
        entries.append({
            "src": f"{TOOLS_FOLDER}/{f}",
            "name": filename_to_display_name(f),
        })
    data = {"tools": entries}
    with open(MANIFEST_PATH, "w", encoding="utf-8") as out:
        json.dump(data, out, indent=2)
    with open(TOOLS_DATA_JS_PATH, "w", encoding="utf-8") as out:
        out.write("window.TOOLS_MANIFEST = " + json.dumps(data) + ";\n")
    print(f"Wrote {len(entries)} tools to {MANIFEST_PATH} and {TOOLS_DATA_JS_PATH}")


if __name__ == "__main__":
    main()
