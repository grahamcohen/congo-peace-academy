#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
IMG_DIR="$ROOT/assets/images/downloaded"
mkdir -p "$IMG_DIR"
python3 <<PYEOF
import os, re, hashlib, subprocess, glob
ROOT = "$ROOT"; IMG_DIR = "$IMG_DIR"
url_re = re.compile(r'https://lh3\.googleusercontent\.com/[^"\'\s)]+')
all_html = (glob.glob(f"{ROOT}/*.html") + glob.glob(f"{ROOT}/about/*.html") + glob.glob(f"{ROOT}/our-events/*.html"))
urls = set()
for f in all_html:
    urls.update(url_re.findall(open(f).read()))
print(f"Found {len(urls)} unique image URLs")
mapping = {}
for i, url in enumerate(sorted(urls), 1):
    h = hashlib.sha1(url.encode()).hexdigest()[:12]
    fname = f"cpa-img-{h}.jpg"
    out = os.path.join(IMG_DIR, fname)
    if not os.path.exists(out) or os.path.getsize(out) < 1000:
        r = subprocess.run(["curl","-sSL","-o",out,
            "-A","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
            "-e","https://sites.google.com/",
            "-H","Accept: image/avif,image/webp,image/*,*/*;q=0.8",
            "--max-time","30", url])
        sz = os.path.getsize(out) if os.path.exists(out) else 0
        status = "OK" if sz > 1000 else "FAIL"
        print(f"  [{i}/{len(urls)}] {status} ({sz} bytes) {fname}")
        if sz <= 1000:
            try: os.remove(out)
            except: pass
            continue
    mapping[url] = f"assets/images/downloaded/{fname}"
for f in all_html:
    rel = os.path.relpath(f, ROOT)
    depth = rel.count("/")
    prefix = "../" * depth if depth else "./"
    content = open(f).read()
    for url, local in mapping.items():
        content = content.replace(url, prefix + local)
    open(f, "w").write(content)
print(f"Mapped {len(mapping)}/{len(urls)} successfully. Rewrote {len(all_html)} HTML files.")
PYEOF
