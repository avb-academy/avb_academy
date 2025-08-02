#!/bin/bash
# Convert .drawio files to .svg only if needed

DRAWIO_APP="/Applications/draw.io.app/Contents/MacOS/draw.io"

for f in *.drawio; do
    svg="${f}.svg"

    if [ ! -f "$svg" ]; then
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
