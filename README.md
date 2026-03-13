# Make Medical AI Writing Better for Everyone

## 为什么做这个项目

当你第三次重写同一个 structured abstract，或者还在纠结 JAMA 的 Key Points 到底该怎么写时，审稿人真正关心的问题通常早就不是措辞本身，而是研究设计是否说清楚、统计是否站得住、伦理与披露是否完整。

医学顶刊写作的难点，从来不只是英文表达，而是整套投稿逻辑：文章类型是否选对，研究设计与报告规范是否匹配，摘要是否准确承载核心发现，结论是否超过证据边界，cover letter 和 disclosure 是否足够稳。这个项目就是把这些高频、隐性的写作规则整理成一个开箱即用的 AI skill。

## 我们做了什么

这个仓库参考了 [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) 的风格和组织方式，但将应用场景从工科论文写作转到医学顶刊投稿，重点面向：

- JAMA 风格的原始研究、随机试验、观察性研究、系统综述与 Meta 分析
- ICMJE 作者署名、AI 使用披露、试验注册等投稿底线
- EQUATOR 系列报告规范，例如 CONSORT、STROBE、PRISMA、STARD、TRIPOD、SQUIRE、CARE
- cover letter、revision response、投稿前 preflight 审核

## 特点

- 医学审稿逻辑优先：先研究设计和合规，再语言润色
- JAMA 取向：对没有指定目标期刊的请求，默认用 JAMA 作为高标准模板
- 可安装可复用：既有可直接调用的 skill，也保留了适合开源分享的 README 结构
- 适合真实投稿流程：从提纲、摘要、正文，到 cover letter、response letter、最终核查

不要把时间浪费在重复调 prompt 上，把精力留给真正重要的医学研究问题。

---

## 目录

### Part I: 推荐使用场景
- 临床研究英文写作
- JAMA structured abstract
- JAMA Key Points
- Reviewer 视角审稿
- Cover letter / Response letter

### Part II: Skill 结构
- 仓库结构
- Skill 安装
- 核心 references
- 辅助脚本

---

# Part I: 推荐使用场景

> 使用方式：把 skill 安装到 Codex / Cursor 后，直接用自然语言描述你的研究类型、目标期刊、已有材料和你想产出的内容。

## 临床研究英文写作

示例 prompt：

```markdown
Use $medical-top-journal-writing to turn my cohort study notes, baseline table, and main regression results into a JAMA-style Original Investigation draft. Keep causal language conservative, follow STROBE logic, and list anything still missing before submission.
```

## JAMA structured abstract

示例 prompt：

```markdown
Use $medical-top-journal-writing to rewrite my abstract into JAMA headings. My study is a multicenter diagnostic accuracy study. Preserve all numbers exactly and flag any abstract claims not supported by the results table.
```

## JAMA Key Points

示例 prompt：

```markdown
Use $medical-top-journal-writing to write JAMA Key Points for this manuscript. Keep it within 75-100 words total and structure it as Question, Findings, Meaning.
```

## Reviewer 视角审稿

示例 prompt：

```markdown
Use $medical-top-journal-writing to audit this near-final draft as if you were a top medical journal reviewer. Prioritize study design clarity, statistical reporting, ethics, registration, overclaiming, and abstract/main-text inconsistencies.
```

## Cover letter / Response letter

示例 prompt：

```markdown
Use $medical-top-journal-writing to draft a submission cover letter for JAMA based on this abstract, clinical importance statement, and novelty bullets. Mention trial registration, ethics approval, and why the manuscript fits JAMA readers.
```

```markdown
Use $medical-top-journal-writing to draft a point-by-point response to reviewers. For each comment, summarize the change made in the manuscript and keep the tone respectful and evidence-based.
```

---

# Part II: Skill 结构

## 仓库结构

```text
awesome-ai-medical-writing/
├── README.md
└── skills/
    └── medical-top-journal-writing/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── journal-playbook.md
        │   ├── medical-writing-checklist.md
        │   └── reporting-guidelines.md
        └── scripts/
            └── manuscript_preflight.py
```

## Skill 安装

如果你的环境支持本地 skills，直接把 `skills/medical-top-journal-writing/` 复制或链接到对应的 skills 目录即可。

如果你使用支持 GitHub 仓库安装的 skills 工具，也可以直接安装这个仓库中的 skill 目录。

## 核心 references

- `journal-playbook.md`
  - JAMA 取向的文章类型、摘要结构、Key Points 和写作取向
- `reporting-guidelines.md`
  - 把常见医学研究设计映射到对应报告规范
- `medical-writing-checklist.md`
  - 投稿前需要核查的伦理、统计、披露、AI 使用与 submission package

## 辅助脚本

`manuscript_preflight.py` 可以快速给出某一研究类型的预检清单，例如：

```bash
python3 skills/medical-top-journal-writing/scripts/manuscript_preflight.py --study-type rct --target-journal jama
```

它适合在起草前或投稿前做 checklist，不替代最终的期刊官网核对。

---

## 参考依据

这个 skill 的默认规则主要锚定在以下官方来源：

- [JAMA Instructions for Authors](https://jamanetwork.com/journals/jama/pages/instructions-for-authors)
- [ICMJE Recommendations](https://www.icmje.org/recommendations/)
- [ICMJE Clinical Trials Registration FAQ](https://www.icmje.org/about-icmje/faqs/clinical-trials-registration/)
- [EQUATOR Network](https://www.equator-network.org/)

如果你后续想继续扩展，我建议下一步加上：

- NEJM / Lancet / BMJ 的期刊特定 references
- 医学图表与 figure legend prompt 集
- reply-to-reviewers 模板库
- 临床研究不同稿型的 cover letter 模板
