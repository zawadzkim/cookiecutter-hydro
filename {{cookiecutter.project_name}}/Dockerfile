# syntax=docker/dockerfile:1

FROM python:3.11-slim

ENV PATH="/root/.pixi/bin:${PATH}"

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install pixi
RUN curl -fsSL https://pixi.sh/install.sh | bash

# Install dependencies into a runner manifest baked in the image.
WORKDIR /opt/runner
COPY pixi.toml /opt/runner/

# Project initialization:
RUN pixi install

# Project files are mounted at runtime via a host volume.
WORKDIR /workspace
VOLUME ["/workspace"]

CMD ["pixi", "run", "--manifest-path", "/opt/runner/pixi.toml", "python", "src/foo.py"]
