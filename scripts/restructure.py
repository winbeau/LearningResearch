#!/usr/bin/env python3
"""把 staging/notion-raw/ 下的 .md 搬到 content/<chapter>/<file>.md，
加 front matter + "本快照来自 ..." 提示行。

映射表写死在 MAPPING 里。
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STAGING = REPO / "staging" / "notion-raw"

# slug → (目标路径相对 content/, 章节短标题)
MAPPING = {
    # 01-getting-started
    "59569d7b-设备配置":            ("01-getting-started/03-tools-and-configs.md", "常用工具与配置"),
    "8911dcc5-学习计划例子":         ("01-getting-started/04-study-plan-example.md", "学习计划参考例子"),

    # 02-research-skills
    "da6ce171-培养想idea能力":       ("02-research-skills/01-finding-ideas.md", "如何培养想 idea 的能力"),
    "d192db87-有效地读论文":         ("02-research-skills/02-reading-papers.md", "如何有效地读论文"),
    "d697ef57-如何高效讨论":         ("02-research-skills/03-effective-discussion.md", "如何高效地讨论"),
    "1aee6e71-实验不work原因":       ("02-research-skills/04-debugging-experiments.md", "如何找到实验不 work 的原因"),
    "caf34717-怎么做实验记录":       ("02-research-skills/05-experiment-notes.md", "怎么做实验记录"),
    "a3fe9f17-科研与课程不同":       ("02-research-skills/06-research-vs-coursework.md", "科研学习与课程学习的不同之处"),

    # 03-research-project
    "b43507ef-research-project":   ("03-research-project/00-overview.md", "如何做 Research Project（PhD 应具备的意识与能力）"),
    "1753fe29-Project技术分析模板":  ("03-research-project/01-tech-problem-template.md", "Project 核心技术问题分析模板"),
    "c278dab7-怎么找论文":           ("03-research-project/02-finding-papers.md", "怎么找论文"),

    # 04-paper-writing
    "c1a22465-论文写作模板":         ("04-paper-writing/00-writing-template.md", "论文写作模板"),
    "c13c7e52-怎么练习写论文":       ("04-paper-writing/01-practicing-writing.md", "怎么练习写论文"),
    "74aef88b-高水平科研工作者写作经验": ("04-paper-writing/02-top-researchers-writing-advice.md", "高水平科研工作者的写作经验"),

    # 05-rebuttal
    "af99ce47-怎么rebuttal":         ("05-rebuttal/00-rebuttal-guide.md", "怎么 Rebuttal"),

    # 06-presentation
    "810f0267-学术报告slides":       ("06-presentation/00-academic-talk-slides.md", "如何做学术报告 slides"),

    # 08-taste-and-mindset (07-collaboration 本轮没有相关页)
    "1713fe29-Sebastian-Starke":   ("08-taste-and-mindset/00-sebastian-starke-model.md", "博士生的楷模：Sebastian Starke"),
    "1d13fe29-面试反思科研品质":     ("08-taste-and-mindset/01-interview-reflections.md", "从面试问题反思科研的宝贵品质"),
}


def yaml_escape(s: str) -> str:
    return s.replace('"', '\\"')


def render(meta: dict, body: str, chapter_title: str) -> str:
    fm_lines = [
        "---",
        f'title: "{yaml_escape(meta["title"])}"',
        f'source_url: {meta["source_url"]}',
        "source_author: 彭思达 (Sida Peng)",
        f'fetched_at: {meta["fetched_at"]}',
    ]
    if meta.get("partial"):
        fm_lines.append("partial: true")
    fm_lines.append("---")
    fm = "\n".join(fm_lines)
    notice = (
        f"\n> 本文是 [{meta['title']}]({meta['source_url']}) 在 "
        f"{meta['fetched_at']} 的快照，原文档可能在 Notion 上有更新。\n"
    )
    return f"{fm}\n{notice}\n{body.strip()}\n"


def main() -> None:
    mapped, missing, unmapped = [], [], []

    slugs_on_disk = {p.stem for p in STAGING.glob("*.md") if not p.name.endswith(".images.txt")}
    for slug, (dest_rel, chapter_title) in MAPPING.items():
        meta_path = STAGING / f"{slug}.meta.json"
        md_path = STAGING / f"{slug}.md"
        if not (meta_path.exists() and md_path.exists()):
            missing.append(slug)
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        body = md_path.read_text(encoding="utf-8")
        out_path = REPO / "content" / dest_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        # 删除当前章节目录下的 .gitkeep（如果还在）
        gk = out_path.parent / ".gitkeep"
        if gk.exists():
            gk.unlink()
        out_path.write_text(render(meta, body, chapter_title), encoding="utf-8")
        mapped.append((slug, str(out_path.relative_to(REPO))))

    for slug in slugs_on_disk - set(MAPPING):
        unmapped.append(slug)

    print(f"✓ Moved {len(mapped)} files to content/")
    for slug, path in mapped:
        print(f"  {slug:35s} → {path}")
    if missing:
        print(f"\n! Missing (in mapping but no staging file): {missing}")
    if unmapped:
        print(f"\n! Unmapped (staging file but no mapping): {unmapped}")


if __name__ == "__main__":
    main()
