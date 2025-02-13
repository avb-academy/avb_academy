#!/bin/bash
# Convert all .drawio files in the current directory to .drawio.svg

for f in *.drawio; do
    /Applications/draw.io.app/Contents/MacOS/draw.io --export --format svg --output "${f}.svg" "$f"
done

echo "Conversion complete!"
