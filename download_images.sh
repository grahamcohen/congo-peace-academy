#!/usr/bin/env bash
#
# download_images.sh — pull all Google-Sites-hosted images used on the site
# into ./assets/images/downloaded/, then rewrite the HTML to point at the
# local copies instead.
#
# Why this exists:
# The current site references images served from lh3.googleusercontent.com
# (where Bienfait's existing Google Sites stored them). Those URLs work right
# now, but Google can change or expire them at any time. Run this once after
# cloning the repo to self-host everything.
#
# Requirements: bash, curl, sed, grep, python3 (for url-safe filenames).
# Run from the repo root:
#     ./download_images.sh
#

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
IMG_DIR="$ROOT/assets/images/downloaded"
mkdir -p "$IMG_DIR"

echo "==> Collecting unique Google-hosted image URLs from HTML…"

# Pull every distinct lh3.googleusercontent.com URL out of every .html file
mapfile -t URLS < <(
  grep -hoE 'https://lh3\.googleusercontent\.com/[^"'"'"' ]+' \
    "$ROOT"/*.html "$ROOT"/about/*.html "$ROOT"/our-events/*.html \
    2>/dev/null | sort -u
)

echo "    Found ${#URLS[@]} unique URLs."

if [[ ${#URLS[@]} -eq 0 ]]; then
  echo "    Nothing to do."
  exit 0
fi

echo "==> Downloading…"

declare -A MAP   # remote URL → local relative path

for url in "${URLS[@]}"; do
  # Derive a stable, filesystem-safe filename from the URL hash
  fname=$(python3 -c "
import hashlib, sys
u = sys.argv[1]
h = hashlib.sha1(u.encode()).hexdigest()[:12]
print(f'cpa-img-{h}.jpg')
" "$url")
  out="$IMG_DIR/$fname"
  if [[ -f "$out" ]]; then
    echo "    [skip] $fname (already downloaded)"
  else
    echo "    [get]  $fname"
    curl -sSL -A "Mozilla/5.0" -o "$out" "$url" || {
      echo "       (failed — leaving original URL in place)"
      continue
    }
  fi
  MAP["$url"]="assets/images/downloaded/$fname"
done

echo "==> Rewriting HTML to use local images…"

# Build a sed script that replaces every remote URL with its local path.
# Files at /about/* and /our-events/* need ../ prefix; root files use ./.
tmp_sed=$(mktemp)
for url in "${!MAP[@]}"; do
  local_path="${MAP[$url]}"
  # Escape forward slashes and ampersands for sed
  esc_url=$(printf '%s' "$url" | sed 's/[\/&]/\\&/g')
  esc_root="${local_path//\//\\/}"
  esc_sub="..\/${local_path//\//\\/}"
  echo "s|$esc_url|__LOCAL_ROOT__$esc_root|g" >> "$tmp_sed"
done

# Apply for root-level HTML
for f in "$ROOT"/*.html; do
  sed -i.bak -E -f "$tmp_sed" "$f"
  sed -i.bak -E "s|__LOCAL_ROOT__|./|g" "$f"
  rm "$f.bak"
done

# Subdirectory HTML files need ../
for f in "$ROOT/about"/*.html "$ROOT/our-events"/*.html; do
  [[ -f "$f" ]] || continue
  sed -i.bak -E -f "$tmp_sed" "$f"
  sed -i.bak -E "s|__LOCAL_ROOT__|../|g" "$f"
  rm "$f.bak"
done

rm "$tmp_sed"

echo "==> Done. Images live in assets/images/downloaded/."
echo "    HTML has been rewritten to point at local copies."
echo "    Commit the new files and you're free from Google Sites image hosting."
