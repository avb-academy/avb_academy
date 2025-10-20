import os
import re
import yaml
import subprocess
import argparse
from pathlib import Path
import sys
from html import unescape
from bs4 import BeautifulSoup, NavigableString


# --- Configuration ---
DRAWIO_APP = "/Applications/draw.io.app/Contents/MacOS/draw.io"
TERMS_PATH = Path("data/termbase.yaml")
LANGUAGES = ["en", "de"]
OUTPUT_SUFFIX = ".svg"

# --- Argument parsing (Jupyter-safe) ---
parser = argparse.ArgumentParser(description="Convert .drawio to .svg and translate using termbase.yaml")
parser.add_argument(
    "-f", "--force", action="store_true",
    help="Force regeneration of all .drawio files even if up to date"
)
args, unknown = parser.parse_known_args()
FORCE = args.force  # Default is False

# --- Load the termbase ---
print(f"[INFO] Loading termbase from: {TERMS_PATH}")
with open(TERMS_PATH, "r", encoding="utf-8") as f:
    termbase = yaml.safe_load(f)
print(f"[INFO] Loaded {len(termbase)} terms from termbase.\n")

# --- Summary tracking ---
summary = {"converted": 0, "translated": 0, "warnings": 0, "errors": 0, "skipped": 0}

def translate_svg(content: str, lang: str, file_name: str) -> str:
    print(f"[INFO] Translating file: {file_name} → language: {lang}")

    translations_lower = {key.lower(): value.get(lang, None) for key, value in termbase.items()}
    missing_terms = set()

    # Parse SVG preserving XML
    soup = BeautifulSoup(content, "lxml-xml")

    # Process all divs containing @@ placeholders
    for div in soup.find_all("div"):
        # find all text nodes with @@...@@ inside this div
        text_nodes = [node for node in div.descendants if isinstance(node, NavigableString) and "@@" in node]
        for tn in text_nodes:
            raw_text = tn.string

            def replace_placeholder(match):
                term = match.group(1)
                term_clean = unescape(term).strip()
                translation = translations_lower.get(term_clean.lower())
                if translation is None:
                    print(f"[ERROR] Term '{term_clean}' not found or missing '{lang}' entry. Fallback to '{term_clean}'")
                    missing_terms.add(term_clean)
                    summary["errors"] += 1
                    return term_clean
                # preserve capitalization
                if term_clean.istitle():
                    translation = translation.title()
                elif term_clean.isupper():
                    translation = translation.upper()
                elif term_clean.islower():
                    translation = translation.lower()
                return translation

            new_text = re.sub(r"@@(.*?)@@", replace_placeholder, raw_text)
            tn.replace_with(NavigableString(new_text))

    if missing_terms:
        print(f"[INFO] Missing terms ({len(missing_terms)}): {', '.join(sorted(missing_terms))}")
    else:
        print("[INFO] All terms successfully translated.")

    print(f"[INFO] Completed translation for language: {lang}\n" + "-" * 60)
    return str(soup)

# --- Function to export .drawio → .svg ---
def export_drawio(drawio_path: Path, force: bool = False):
    svg_path = drawio_path.with_suffix(drawio_path.suffix + ".svg")

    if not svg_path.exists():
        reason = "SVG missing"
    elif force:
        reason = "Force enabled"
    elif drawio_path.stat().st_mtime > svg_path.stat().st_mtime:
        reason = "Drawio newer"
    else:
        print(f"[SKIP] {svg_path.name} is up to date.")
        summary["skipped"] += 1
        return svg_path, False

    print(f"[INFO] {reason}: regenerating {svg_path.name}")
    subprocess.run(
        [DRAWIO_APP, "--export", "--format", "svg", "--output", str(svg_path), str(drawio_path)],
        check=True
    )
    summary["converted"] += 1
    return svg_path, True

# --- Main loop (recursive over static/images) ---
IMAGES_DIR = Path("static/images")

for drawio_file in IMAGES_DIR.rglob("*.drawio"):
    svg_path, converted = export_drawio(drawio_file, FORCE)

    # Read the SVG content
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()

    # Translate for each language
    for lang in LANGUAGES:
        translated_svg = translate_svg(svg_content, lang, svg_path.name)
        output_svg_path = svg_path.with_name(f"{svg_path.stem}.{lang}.svg")
        with open(output_svg_path, "w", encoding="utf-8") as f:
            f.write(translated_svg)
        summary["translated"] += 1
        print(f"[INFO] Created: {output_svg_path.name}\n")

# --- Summary ---
print("\nProcessing completed!")
print(f"Files converted:   {summary['converted']}")
print(f"Files translated:  {summary['translated']}")
print(f"Warnings:          {summary['warnings']}")
print(f"Errors:            {summary['errors']}")
print(f"Skipped:           {summary['skipped']}")
print("--------------------------------------------------")

if summary["errors"] > 0:
    print(f"[ERROR] {summary['errors']} translation errors occurred.", file=sys.stderr)
    sys.exit(1)
else:
    sys.exit(0)