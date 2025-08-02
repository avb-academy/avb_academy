#!/bin/bash
# Convert .drawio files to .svg only if needed, unless forced

DRAWIO_APP="/Applications/draw.io.app/Contents/MacOS/draw.io"
FORCE=0

usage() {
    echo "Usage: $(basename "$0") [-f] [-h]"
    echo
    echo "  -f    Force conversion of all .drawio files to .svg, even if up to date"
    echo "  -h    Show this help message and exit"
}

while getopts "fh" opt; do
    case "$opt" in
        f) FORCE=1 ;;
        h) usage; exit 0 ;;
        *) usage; exit 1 ;;
    esac
done

for f in *.drawio; do
    svg="${f}.svg"

    if [ "$FORCE" -eq 1 ]; then
        echo "Forcing regeneration of $svg from $f"
        "$DRAWIO_APP" --export --format svg --output "$svg" "$f"
    elif [ ! -f "$svg" ]; then
        echo "SVG not found for $f. Creating..."
        "$DRAWIO_APP" --export --format svg --output "$svg" "$f"
    elif [ "$f" -nt "$svg" ]; then
        echo "$f is newer than $svg. Recreating..."
        "$DRAWIO_APP" --export --format svg --output "$svg" "$f"
    else
        echo "$svg is up to date. Skipping."
    fi
done

echo "Conversion check complete!"
