#!/usr/bin/env python3
"""把 Playwright MCP browser_evaluate 的工具输出文件转成 staging/ 下的 html/md/meta。

工具输出文件结构（来自 Claude Code）:
    ### Result\n
    "<escaped JSON of {title, html, images, zhihu, subpages, allLinks}>"\n
    ### Ran Playwright code\n
    ...

用法:
    python3 scripts/process_tool_result.py <tool_result_file> <kind> <slug> <source_url>
    # kind: notion | zhihu
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

from markdownify import markdownify as html_to_md  # type: ignore

REPO = Path(__file__).resolve().parent.parent


def extract_payload(result_text: str) -> dict:
    # 抓 ### Result 后第一个被双引号包起来的字符串
    m = re.search(r"### Result\s*\n\"(.*?)\"\s*\n###", result_text, re.DOTALL)
    if not m:
        raise SystemExit("could not locate ### Result block")
    escaped = m.group(1)
    # 这是 JSON.stringify 的输出再被工具结果包一层 JSON 字符串，所以要 json.loads 两次
    inner_json = json.loads('"' + escaped + '"')  # 解开外层字符串转义
    payload = json.loads(inner_json)              # 解开真正的 JSON
    return payload


def main() -> None:
    if len(sys.argv) != 5:
        sys.exit("usage: process_tool_result.py <tool_result_file> <notion|zhihu> <slug> <source_url>")
    result_file = Path(sys.argv[1])
    kind = sys.argv[2]
    slug = sys.argv[3]
    source_url = sys.argv[4]

    out_dir = REPO / "staging" / f"{kind}-raw"
    out_dir.mkdir(parents=True, exist_ok=True)

    payload = extract_payload(result_file.read_text(encoding="utf-8"))
    if "error" in payload:
        sys.exit(f"playwright reported error: {payload['error']}")

    html = payload["html"]
    title = payload.get("title", "untitled")
    images = payload.get("images", [])
    zhihu = payload.get("zhihu", [])
    subpages = payload.get("subpages", [])
    partial = payload.get("partial", False)

    (out_dir / f"{slug}.html").write_text(html, encoding="utf-8")
    md = html_to_md(html, heading_style="ATX", strip=["script", "style"]).strip()
    (out_dir / f"{slug}.md").write_text(md, encoding="utf-8")

    meta = {
        "slug": slug,
        "title": title,
        "source_url": source_url,
        "kind": kind,
        "fetched_at": str(date.today()),
        "partial": partial,
        "image_count": len(images),
        "zhihu_count": len(zhihu),
        "subpage_count": len(subpages),
    }
    (out_dir / f"{slug}.meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out_dir / f"{slug}.images.txt").write_text("\n".join(images), encoding="utf-8")
    (out_dir / f"{slug}.zhihu.txt").write_text("\n".join(zhihu), encoding="utf-8")
    if subpages:
        sub_log = REPO / "staging" / "discovered-subpages.txt"
        with sub_log.open("a", encoding="utf-8") as f:
            for u in subpages:
                f.write(f"{u}\t# from {slug}\n")

    md_lines = md.count("\n") + 1
    print(f"[{slug}] title={title!r} html={len(html)//1024}KB md_lines={md_lines} "
          f"images={len(images)} zhihu={len(zhihu)} subpages={len(subpages)} "
          f"partial={partial}")


if __name__ == "__main__":
    main()
