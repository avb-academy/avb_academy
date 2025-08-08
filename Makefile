# Makefile for AVB Academy build process

.PHONY: all images site clean

all: site

images:
	echo "Creating images"
	cd static/images && ./convert_drawio.sh -f

site: images
	hugo

clean:
	rm -rf public
