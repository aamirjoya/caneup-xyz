#!/bin/bash
# Cloudflare Pages build script for Hugo

# Hugo version
HUGO_VERSION="0.147.4"

# Download Hugo
wget -q "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" -O /tmp/hugo.tar.gz
tar -xzf /tmp/hugo.tar.gz -C /tmp/
chmod +x /tmp/hugo

# Build site
/tmp/hugo --minify

echo "Build complete!"
