#!/usr/bin/env python3
"""下载所有 staging 中引用的图片到 assets/<slug>/。

对每个 staging/notion-raw/*.meta.json，读取它的 .images.txt 列表，
逐个 curl 下载，文件名 img-NN.<ext>。最后输出 staging/image_map.json
(URL → 本地相对路径)，供阶段 E 重写 Markdown 用。

跳过：
  - data:image/...  (Notion 的占位 callout 图标，无实际内容)

URL 形式处理：
  - /image/...        → 前缀 https://pengsida.notion.site
  - http(s)://...     → 原样
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO = Path(__file__).resolve().parent.parent
NOTION_BASE = "https://pengsida.notion.site"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"


def absolutize(url: str) -> str | None:
    if url.startswith("data:"):
        return None
    if url.startswith("http"):
        return url
    if url.startswith("/"):
        return NOTION_BASE + url
    return None


def guess_ext_from_url(url: str) -> str:
    # URL 里的 image.png / image.jpg
    m = re.search(r"\.(png|jpg|jpeg|gif|webp|svg)(?:[?&]|$)", url, re.IGNORECASE)
    if m:
        return "." + m.group(1).lower()
    # URL-encoded 后的 .png
    m = re.search(r"%2E(png|jpg|jpeg|gif|webp)", url, re.IGNORECASE)
    if m:
        return "." + m.group(1).lower()
    return ".png"


def ext_from_content_type(ct: str) -> str:
    ct = ct.split(";")[0].strip().lower()
    return {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
    }.get(ct, ".png")


def curl_download(url: str, out_path: Path) -> tuple[bool, str]:
    """返回 (success, content_type)"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "curl", "-sSL", "-A", UA,
        "--max-time", "30",
        "-w", "%{http_code}\t%{content_type}",
        "-o", str(out_path),
        url,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=40)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    if r.returncode != 0:
        return False, f"curl-rc={r.returncode}"
    parts = (r.stdout or "").split("\t", 1)
    code = parts[0].strip()
    ct = parts[1].strip() if len(parts) > 1 else ""
    if code != "200":
        return False, f"http-{code}"
    if out_path.stat().st_size < 100:
        return False, f"too-small-{out_path.stat().st_size}"
    return True, ct


def main() -> None:
    all_meta = sorted(Path("staging/notion-raw").glob("*.meta.json"))
    image_map: dict[str, str] = {}        # absolute URL → local path relative to repo root
    failures: list[dict] = []

    for meta_path in all_meta:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        slug = meta["slug"]
        imgs_path = meta_path.with_suffix("").with_suffix(".images.txt")
        if not imgs_path.exists():
            continue
        urls = [u.strip() for u in imgs_path.read_text(encoding="utf-8").splitlines() if u.strip()]
        # 去重保序
        seen = set()
        urls = [u for u in urls if not (u in seen or seen.add(u))]
        if not urls:
            continue

        target_dir = REPO / "assets" / slug
        idx = 0
        for url in urls:
            absurl = absolutize(url)
            if absurl is None:
                continue  # data: URLs etc.
            if absurl in image_map:
                # 已下过（其他页也引用），但当前 slug 的 Markdown 里仍引用原 URL，
                # 在 image_map 里它的本地路径属于"首次出现的 slug"。Markdown 重写时统一指向首次路径即可。
                continue
            idx += 1
            ext = guess_ext_from_url(absurl)
            out_name = f"img-{idx:02d}{ext}"
            out_path = target_dir / out_name
            ok, info = curl_download(absurl, out_path)
            if not ok:
                failures.append({"slug": slug, "url": absurl, "reason": info})
                if out_path.exists():
                    out_path.unlink()
                print(f"  [FAIL] {slug}/{out_name}: {info}")
                continue
            # 按实际 Content-Type 修正扩展名（首选 URL，但服务器声明的更权威）
            if info and info.startswith("image/"):
                correct_ext = ext_from_content_type(info)
                if correct_ext != ext:
                    new_path = out_path.with_suffix(correct_ext)
                    out_path.rename(new_path)
                    out_path = new_path
                    out_name = out_path.name
            relpath = out_path.relative_to(REPO).as_posix()
            image_map[absurl] = relpath
            print(f"  [OK] {slug}/{out_name} ({info}, {out_path.stat().st_size//1024}KB)")

    # 写出结果
    (REPO / "staging" / "image_map.json").write_text(
        json.dumps(image_map, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if failures:
        (REPO / "staging" / "image_failures.json").write_text(
            json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    print(f"\n✓ Downloaded {len(image_map)} images, {len(failures)} failures")
    print(f"  image_map.json -> staging/image_map.json")


if __name__ == "__main__":
    os.chdir(REPO)
    main()
