#! /usr/bin/env bash

# Install pixi
curl -fsSL https://pixi.sh/install.sh | bash
export PATH="$HOME/.pixi/bin:$PATH"
echo 'export PATH="$HOME/.pixi/bin:$PATH"' >> "$HOME/.bashrc"

# Install dependencies
pixi install
