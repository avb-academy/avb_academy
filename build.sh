#!/bin/bash
# File: build.sh
# Purpose: Sophisticated partial automation of AVB Academy build process

set -e
set -o pipefail

# --- Default flags ---
REBUILD_IMAGES=false
FORCE_IMAGES=false

# --- Help message ---
show_help() {
    echo "Usage: ./build.sh [OPTIONS]"
    echo
    echo "Options:"
    echo "  --images        Recreate SVGs in static/images (only if drawio is newer)"
    echo "  --force         Force recreation of all images (use with --images)"
    echo "  --help          Show this help message and exit"
    echo
    echo "If no options are provided, the full build is executed."
    exit 0
}

# --- Argument parsing ---
for arg in "$@"; do
    case $arg in
        --images)
            REBUILD_IMAGES=true
            ;;
        --force)
            FORCE_IMAGES=true
            ;;
        --help)
            show_help
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Use --help to see available options."
            exit 1
            ;;
    esac
done

# --- Delete public folder for clean start ---
echo "Deleting public folder"
rm -rf public/

# --- Create/Activate virtual environment and install dependencies ---
VENV_DIR="venv"
# Check if the virtual environment directory already exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists. Skipping creation."
fi

echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing/updating dependencies from requirements.txt..."
pip install -r requirements.txt
echo "Installation complete!"

# --- Function to build images ---
build_images() {
    echo "Creating/rebuilding SVG images..."
    CMD="python3 build_scripts/create_svg.py"
    if [ "$FORCE_IMAGES" = true ]; then
        CMD="$CMD --force"
    fi
    $CMD
}

# --- Full build sequence ---
if [ "$REBUILD_IMAGES" = true ]; then
    # Only build images
    build_images
else
    # Complete build
    echo "Sorting termbase..."
    python3 build_scripts/sort_termbase.py data/termbase.yaml

    echo "Deleting old SVG files..."
    rm -f static/images/*.drawio.svg
    rm -f static/images/*.drawio.en.svg
    rm -f static/images/*.drawio.de.svg

    # Build images (optional force)
    build_images

    echo "Building Hugo site..."
    hugo

    # Copy english 404 to directory root
    cp public/en/404.html public/404.html
fi

echo "Build completed successfully."
