# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository nature

This is a **documentation-only repository** (no code, no build system, no tests). It hosts Sida Peng's Chinese-language guide on doing research, intended for lab newcomers and the broader community. Everything tracked here is Markdown plus a `changelog` text file.

All authored content is in **Simplified Chinese** — match that language when editing or adding entries. Quoted English terms (e.g. "Roadmap", "Ph.D.", "Project") are kept as-is by convention; don't translate them.

## Content layout

The repo itself is shallow — three docs and a changelog — but most of the *actual* material lives on Notion and is only linked from here:

- `README.md` — landing page. Tracks "文档上次更新时间" (last-updated date) near the top; this date is bumped whenever content (here or on Notion) changes.
- `getting_started_in_research.md` — staged learning path for entering 3D-vision research (linked as item 1 from README).
- `getting_advanced_in_research.md` — how to build research ability once basics are in place (linked as item 2 from README, and from the end of `getting_started_in_research.md`).
- `changelog` — append-only log of edits, including edits to the external Notion pages. Each line is `- YYYY年M月D日，<动作> <文档名>:<Notion URL>，<简要说明>。` Newest entries go at the top.

Most "documents" referenced from the Markdown files (论文写作模板, 如何rebuttal, research project guide, etc.) are **Notion pages, not files in this repo**. Don't try to locate or edit them locally — link to the Notion URL the same way existing references do.

## Routine edit workflows

Two patterns cover the bulk of commits (see `git log` for examples — most commits are one of these):

1. **Recording a Notion update.** Prepend a dated bullet to `changelog`. If the change is meaningful enough that readers should notice, also bump "文档上次更新时间：YYYY年M月D日" in `README.md`. Use today's date from the environment context.
2. **Editing a tracked Markdown file.** Update the file, then add a corresponding `changelog` entry and bump the README date if appropriate.

When adding a new top-level topic to `README.md`, also link it from the relevant section in `getting_started_in_research.md` / `getting_advanced_in_research.md` if it fits the staged path those docs lay out.

## Style conventions to preserve

- The "如何努力成为一个Top Ph.D. Student" section in `README.md` uses an ordered list of resources (入门 → 培养能力 → research project → 写作 → rebuttal → slides). New high-level guidance generally slots into this list rather than being added as its own H2.
- External links pointing to Sida Peng's own materials use `https://pengsida.notion.site/...`, `https://pengsida.net/...`, or the GitHub repo URL. Match the existing host for the resource being referenced.
- The Notion notice in the README postscript ("更新可能会在Notion文档中进行，因此不一定会反映在Commit History中") is load-bearing — don't claim the repo's commit history is authoritative for content changes.

## What this repo is *not*

- Not a code project — there is nothing to build, lint, run, or test. Don't add tooling (package.json, CI configs, linters) unless the user explicitly asks.
- Not a place for original commentary — the docs reflect a specific author's research experience. When editing, preserve the first-person framing ("本人", "我") and don't insert generalizations or rewordings that change the voice.
