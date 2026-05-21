# Learning Research

> 关于做科研的心得体会与方法论。本仓库是 [@pengsida](https://pengsida.net/) 的 Notion 文档的 **本地化快照**，按博士成长阶段重新编排，可线性阅读。

## Motivation of This Repository

1. 面向实验室研究生、本科生的科研教学。希望将科研经验进行书面总结，而不是以口口相传的方式传承，帮助实验室新人学习科研。
2. 开源这样的科研经验，希望对实验室以外的同学有所帮助。
3. 开源的形式可以接受大家的审阅，得到大家的建议，从而可以改进科研经验。

**Postscript:**
1. 本文档内容可能无法完全反映本人想表达的意思，内容可能也不够完整。如果想深入学习科研，推荐在参考文档的情况下在实践与交流中学习。
2. 本文档适用于[本人](https://pengsida.net/)在[本实验室](https://xzhou.me/)的科研经历，但不一定适用于其他情况。
3. 本文档原始内容持续更新于 Notion。本仓库是其中 18 篇核心文档在 **2026-05-21** 的快照——之后 Notion 上的修改不会自动反映到这里（每篇本地文件顶部均标注 `fetched_at` 与原文链接）。

## 📖 阅读路线图

如果你是科研新人，建议按下面的顺序读一遍。每一节都链到本仓库的本地文件，离线可读、含图。完整目录见 [SUMMARY.md](SUMMARY.md)。

| 阶段 | 内容 | 入口 |
|---|---|---|
| 🟢 **入门** | 配环境、定学习计划、跟着学长姐做项目 | [01 · 入门](content/01-getting-started/) — [常用工具与配置](content/01-getting-started/03-tools-and-configs.md)、[学习计划参考例子](content/01-getting-started/04-study-plan-example.md) |
| 🔵 **培养能力** | 想 idea、读论文、做实验、写实验记录、和导师/学长讨论 | [02 · 培养科研能力](content/02-research-skills/) — 6 篇 |
| 🟣 **做一个 Project** | 从问题到论文的完整流程 + 技术问题分析模板 + 怎么找论文 | [03 · Research Project](content/03-research-project/) — 3 篇 |
| 🟡 **写论文** | 写作模板、Method/Abstract/Introduction、练习写作、高水平科研工作者的写作经验 | [04 · 论文写作](content/04-paper-writing/) — 3 篇 |
| 🟠 **Rebuttal** | 流程图、语言风格、回应 Reviewer 的策略 | [05 · Rebuttal](content/05-rebuttal/00-rebuttal-guide.md) |
| 🔴 **Presentation** | 怎么做学术报告 Slides | [06 · Presentation](content/06-presentation/00-academic-talk-slides.md) |
| ⚪ **协作沟通** | 师生交流、和实验室同学相处 *(本轮暂未独立成章)* | [07 · 师生协作](content/07-collaboration/README.md) |
| ⚫ **品味与心态** | 学习高水平博士的科研模式、从面试反思科研 | [08 · 品味与心态](content/08-taste-and-mindset/) — 2 篇 |

> **TL;DR**：如果只想读一篇，推荐 [03 · 如何做 Research Project](content/03-research-project/00-overview.md)；如果只想读两篇，再加 [04 · 论文写作模板](content/04-paper-writing/00-writing-template.md)。

## 如何努力成为一个 Top Ph.D. Student

核心的能力：个人认为，Top Ph.D. Student 懂得设定一个长远的科研目标。这个科研目标具有重要的科学价值和实际价值（在实际应用中寻找真正有价值的科学问题）。然后根据这个科研目标细化科研的 Roadmap。博士期间做的几篇论文都是围绕着解决这个科研目标，并且做的论文能够清晰地展示出自己沿 Roadmap 的科研进展，论文 Demo 要尽量很酷（例子：[博士生的楷模：Sebastian Starke](content/08-taste-and-mindset/00-sebastian-starke-model.md)）。

在实际做科研过程中，Ph.D. Student 需要有五方面的能力：寻找重要的科研问题、提出解决方案、做实验、写论文、做 Presentation。

### 配套 Slides 与视频

- 《GAMES003：科研基本素养》版本（推荐）：
  - 《科研流程概述与领域视野建立》[Slides](https://pengsida.net/games003/GAMES003_files/week_1.pdf) · [课程视频](https://www.bilibili.com/video/BV1RitTezEa9?p=1)
  - 《技术方案的设计方法》[Slides](https://pengsida.net/games003/GAMES003_files/week_3.pdf) · [课程视频](https://www.bilibili.com/video/BV1RitTezEa9?p=3)
  - 《面向实验结果的方案优化》[Slides](https://pengsida.net/games003/GAMES003_files/week_5.pdf) · [课程视频](https://www.bilibili.com/video/BV1RitTezEa9?p=5)
- 《learning research》版本：[Slides](https://pengsida.net/files/learning_research_v4.pdf) · [Talk Video](https://www.bilibili.com/video/BV1DA4m1V7D3/)
- 着重讨论如何建立领域视野和选择科研课题：[Slides (2025-08-12)](https://pengsida.net/files/research_topic_selection.pdf)
- 《CCF 优博是怎么炼成的》：[Slides](https://pengsida.net/files/CCF_Talk.pdf)

本人与另外三位研究人员（[高俊](https://www.cs.toronto.edu/~jungao/)、[彭崧猷](https://pengsongyou.github.io/)、[王倩倩](https://qianqianwang68.github.io/)）在 GAMES 平台上开设了课程：[《GAMES003：图形视觉科研基本素养》](https://pengsida.net/games003/)。

## 仓库结构

```
content/        # 主体内容（按 8 个章节编排），每篇都是 Notion 的本地快照
references/    # 外部资源清单（PDF / 视频 / 课程 / Zhihu 链接），不本地化
assets/        # 各篇内文图片（按 slug 分目录）
docs-legacy/   # 重组前的 README + getting_*_in_research.md，备查
staging/       # 抓取中转产物（HTML / meta / 图片映射），开发参考
scripts/       # 一次性抓取脚本
SUMMARY.md     # 完整目录与阅读顺序
SOURCES.md     # 每篇本地文件的原 Notion URL + 抓取时间汇总
CLAUDE.md      # 给 Claude Code 工作的指引
```

## Citation

若该文档对您有所帮助，请在页面右上角点个 Star ⭐ 支持一下，谢谢！

如果转载该文档的内容，请注明原始出处：[https://github.com/pengsida/learning_research](https://github.com/pengsida/learning_research)（这是原作者的仓库；本地化快照仓库可补充本仓库地址）。

## Acknowledgements

本文档内容主要是原作者与导师、朋友、实验室同学日常交流讨论的总结。在此非常感谢以下人员对这份文档的启发：[周晓巍老师](https://xzhou.me/)、[孙佳明](https://jiamingsun.ml/)、[沈宇军](https://shenyujun.github.io/)、[帅青](https://chingswy.github.io/)、[沈泽弘](https://zehongs.github.io/)、[郭浩宇](https://github.com/ghy0324)、[贺星毅](https://github.com/hxy-123)、[林浩通](https://haotongl.github.io/)、[徐震](https://github.com/dendenxu)、[张上展](https://zhanghe3z.github.io/)、[皮怀瑾](https://github.com/phj128)。
