# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository nature

This is a **documentation-only repository** (no code, no build system, no tests). It hosts Sida Peng's Chinese-language guide on doing research — a **local snapshot** (as of 2026-05-21) of 18 Notion pages, reorganized into 8 chapters under `content/` for linear reading. Original source-of-truth still lives on Notion; this repo is a frozen point-in-time mirror.

All authored content is in **Simplified Chinese** — match that language when editing. Quoted English terms ("Roadmap", "Ph.D.", "Project", "Pipeline figure") are kept as-is by convention; don't translate them. Author voice is first-person ("我"/"本人") — preserve it; don't rewrite into third-person.

## Repository layout

```
content/                  Main material — 18 chapters across 8 sections (01..08)
  01-getting-started/     入门：tools, study plan
  02-research-skills/     培养能力：finding ideas, reading papers, discussing, debugging experiments...
  03-research-project/    做 project：overview, tech analysis template, finding papers
  04-paper-writing/       写论文：writing template, practicing, top-researchers advice
  05-rebuttal/            rebuttal 流程与语言风格
  06-presentation/        学术报告 slides
  07-collaboration/       (placeholder — content lives across other chapters for now)
  08-taste-and-mindset/   科研品味与心态：Sebastian Starke model, interview reflections
assets/<slug>/            Inline images for each page, downloaded from Notion
references/               Curated lists of NOT-mirrored resources (PDFs, videos, courses, Zhihu)
docs-legacy/              Pre-restructure README + getting_*.md (archived)
staging/                  Snapshot intermediates: raw HTML, meta.json, image_map.json
scripts/                  One-shot snapshot helpers (process_tool_result.py, download_images.py, restructure.py)
SUMMARY.md                Authoritative reading order (GitBook-style TOC)
SOURCES.md                Generated table: each content file → its Notion source URL + fetched_at
README.md                 Landing page with reading roadmap
changelog                 Append-only log (Chinese, dates in 年月日 format, newest on top)
```

Every `content/**/*.md` starts with YAML front matter (`title`, `source_url`, `source_author`, `fetched_at`). **Treat that front matter as authoritative provenance** — when in doubt about whether a document is fresh, check its `source_url` against Notion. Update `fetched_at` if you re-snapshot.

## Routine edit workflows

Two patterns cover most commits (see `git log` for examples):

1. **Recording a Notion update.** Prepend a dated bullet to `changelog`. If the change affects something that's also snapshotted under `content/`, re-snapshot that page (see "Re-snapshotting a page" below) rather than just editing the local copy — otherwise the local copy drifts from `source_url`.
2. **Editing the README / SUMMARY structure.** Adjust both — they need to stay consistent. `SUMMARY.md` is the canonical TOC; `README.md` is the entry page with the 8-stage roadmap table.

When adding a NEW page from Notion: snapshot it (see below), put the result in the appropriate `content/<chapter>/` directory with a numbered filename, add an entry to `SUMMARY.md`, add a row to the README roadmap if it's prominent, and regenerate `SOURCES.md` (one-liner in `scripts/`).

## Re-snapshotting a page

The snapshot pipeline lives in `scripts/`. To refresh one page:

1. `mcp__playwright__browser_navigate` → the Notion URL
2. `mcp__playwright__browser_evaluate` with the toggle-expansion + extract function (see `scripts/process_tool_result.py` for context, or just adapt the JS from a prior commit message). Pad the JSON with `_pad: 'x'.repeat(80000)` to guarantee tool-result file overflow → result lands at `.../tool-results/...txt`.
3. `python3 scripts/process_tool_result.py <result_file> notion <slug> <source_url>` → writes `staging/notion-raw/<slug>.{html,md,meta.json,images.txt,zhihu.txt}`.
4. `python3 scripts/download_images.py` (re-runs for all pages, idempotent on already-downloaded).
5. Manually move the new `.md` into `content/<chapter>/<file>.md` with front matter and snapshot notice — or extend `scripts/restructure.py` with the new mapping and re-run.

## Style conventions to preserve

- New `content/**/*.md` files: keep the YAML front matter exactly in the existing format, including the "本文是 [...] 在 YYYY-MM-DD 的快照" notice line right after.
- Image paths in `content/` always use `../../assets/<slug>/img-NN.<ext>`.
- The Notion-update notice in README's Postscript is load-bearing — don't claim the local commit history is the source of truth for content changes.

## What this repo is *not*

- Not a code project — there is nothing to build, lint, run, or test. Don't add tooling (package.json, CI configs, linters) unless the user explicitly asks.
- Not a place for original commentary — the docs reflect the original author's research experience. When editing, preserve the first-person framing and don't insert generalizations or rewordings that change voice.

## Resource awareness (VPS-specific)

This repo lives on a small shared VPS (~1.9 GB RAM). The user's global `CLAUDE.md` forbids running heavy operations here (`uv sync`, large model downloads, project main programs). Snapshot operations should run via the Playwright MCP (which proxies to the user's WSL), not via local Chromium. Light Python tooling (`markdownify` + `beautifulsoup4` via `pip install --user --break-system-packages`) is acceptable and already installed.
