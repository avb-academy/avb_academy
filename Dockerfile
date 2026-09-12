ARG PYTHON_VERSION=3.13.1

FROM python:${PYTHON_VERSION}-slim-bookworm

ARG HUGO_VERSION=0.148.1
ARG DRAWIO_VERSION=25.0.2

ENV DRAWIO_APP=/usr/bin/drawio PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl && curl -fsSL -o /tmp/hugo.deb "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb" && curl -fsSL -o /tmp/drawio.deb "https://github.com/jgraph/drawio-desktop/releases/download/v${DRAWIO_VERSION}/drawio-amd64-${DRAWIO_VERSION}.deb" && apt-get install -y --no-install-recommends /tmp/hugo.deb /tmp/drawio.deb && rm -f /tmp/hugo.deb /tmp/drawio.deb && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

WORKDIR /site

CMD ["bash", "build.sh"]