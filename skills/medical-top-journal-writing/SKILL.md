---
name: medical-top-journal-writing
description: Draft, revise, and preflight manuscripts for high-impact medical journals with JAMA-oriented defaults and ICMJE/EQUATOR compliance. Use when Codex needs to turn study notes, tables, protocols, abstracts, cover letters, reviewer responses, or near-final drafts into submission-ready medical-journal materials for original investigations, trials, observational studies, systematic reviews, diagnostic or prognostic studies, qualitative studies, case reports, or related clinical research writing.
---

# Medical Top Journal Writing

Treat this skill as a medical-journal copilot, not a generic polishing tool. Prioritize article-type fit, reporting-guideline compliance, statistical clarity, ethics and disclosure language, and reviewer-proof structure before stylistic refinement.

Default to a JAMA-style clinical writing standard when the user asks for a "top medical journal" draft without naming a target. If the user names another journal, keep the same rigor but verify the live journal instructions before final formatting.

## Workflow

### 1. Triage the request

Identify these variables first:

- target journal or fallback journal family
- article type
- study design
- writing stage: outline, section draft, full manuscript, revision, cover letter, response letter, or pre-submission audit
- available source material: protocol, SAP, tables, figures, registry ID, ethics language, disclosures, and prior reviewer comments

If one missing item will materially change the output, ask only for that item. Otherwise make a clear assumption and proceed.

### 2. Lock the compliance frame

Before drafting, determine:

- article type and default length or structure from [references/journal-playbook.md](references/journal-playbook.md)
- reporting checklist from [references/reporting-guidelines.md](references/reporting-guidelines.md)
- required disclosure and submission items from [references/medical-writing-checklist.md](references/medical-writing-checklist.md)

If useful, run:

```bash
python3 scripts/manuscript_preflight.py --study-type <type> --target-journal <journal>
```

Use the script output as a drafting checklist, not as a substitute for reading the references.

### 3. Draft in medical-journal order

Prefer this sequence:

1. title and subtitle
2. structured abstract
3. JAMA Key Points if applicable
4. introduction
5. methods
6. results
7. discussion
8. references, tables, figures, supplements
9. cover letter and disclosure package

Keep the manuscript aligned to the actual evidence. Never invent sample sizes, effect estimates, confidence intervals, P values, subgroup results, registration numbers, ethics approvals, or follow-up durations.

### 4. Write with reviewer logic

Apply these rules throughout:

- lead with the clinical or public-health importance
- keep claims proportional to the design
- distinguish prespecified analyses from exploratory analyses
- report absolute numbers and denominators whenever possible
- foreground primary outcomes before secondary or subgroup findings
- present harms and null findings with the same discipline as positive results
- describe limitations in plain, non-defensive language
- translate findings into clinical relevance without hype

### 5. Preflight before handing off

Always do a last pass for:

- study design accurately named everywhere
- abstract consistent with main text, tables, and figures
- outcomes and time points used consistently
- ethics, consent, registration, funding, conflicts, data sharing, and AI-use language present where needed
- causal language toned down if the design is observational
- statistical terms, effect sizes, confidence intervals, and denominators reported cleanly
- journal-specific extras present, especially Key Points, subtitle style, or protocol/checklist supplements

## Drafting Rules

### Original investigations and trials

Open with why the clinical question matters now. In Methods, specify design, setting, participant selection, dates, intervention or exposure, outcomes, statistical methods, ethics approval, consent, and registration when applicable. In Results, keep the primary analysis first and anchor every claim to data. In Discussion, move in this order: principal findings, comparison with prior literature, strengths and limitations, and implications for practice or policy.

For JAMA-style abstracts, use the article-appropriate headings from [references/journal-playbook.md](references/journal-playbook.md). For research and review manuscripts that require Key Points, produce three lines only: Question, Findings, Meaning.

### Reviews and meta-analyses

State the clinical question precisely. Make the search strategy and eligibility logic auditable. Quantify the included evidence base, risk of bias or quality, and the main pooled or narrative findings. Keep conclusions bounded to the evidence reviewed. For systematic reviews and meta-analyses, make sure the PRISMA flow and evidence-quality table are addressed when relevant.

### Observational, diagnostic, prognostic, and qualitative studies

Guard carefully against overclaiming. Use association language for observational work unless causal inference is explicitly justified. For diagnostic or prognostic studies, separate model development, validation, and performance reporting. For qualitative work, make the sampling logic, analytic framework, reflexivity, and trustworthiness procedures explicit.

### Cover letters and revision responses

For cover letters, summarize the clinical importance, manuscript type, novelty, and why the paper fits the journal's readership. Mention registration, ethics, and related manuscripts when relevant.

For reviewer responses, quote or summarize each reviewer point, answer directly, specify the manuscript change, and point to the revised section. If you disagree, do so respectfully and with evidence.

## Non-Negotiables

- Do not list AI as an author.
- Do not hide AI assistance if it materially contributed to writing, analysis, or figure generation; disclose it according to the target journal and ICMJE-oriented guidance.
- Do not convert observational results into causal claims without justification.
- Do not report significance without the corresponding estimate context.
- Do not omit harms, missing data handling, exclusions, or protocol deviations when they matter to interpretation.
- Do not give a "submission ready" verdict if core metadata such as ethics approval, registration, or primary outcome definitions are missing.

## Output Packages

Adapt the deliverable to the user's stage.

For a draft request, prefer:

1. manuscript text
2. unresolved factual gaps list
3. journal-compliance checklist

For a revision request, prefer:

1. revised text
2. major changes summary
3. remaining red flags

For a pre-submission audit, prefer:

1. pass or fail checklist
2. highest-risk issues first
3. exact missing items to obtain before submission

## Resources

### scripts/

Use `scripts/manuscript_preflight.py` to generate a compact article-type and submission checklist from the selected study design.

### references/

Read only the file you need:

- [references/journal-playbook.md](references/journal-playbook.md): JAMA-oriented article structures, abstract rules, Key Points, and submission defaults
- [references/reporting-guidelines.md](references/reporting-guidelines.md): map study type to CONSORT, STROBE, PRISMA, STARD, TRIPOD, SQUIRE, CARE, and related standards
- [references/medical-writing-checklist.md](references/medical-writing-checklist.md): ethics, statistics, disclosure, AI-use, and pre-submission red flags

### assets/

This skill does not currently require assets.
