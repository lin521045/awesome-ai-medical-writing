#!/usr/bin/env python3
"""Generate a compact medical-journal preflight checklist."""

from __future__ import annotations

import argparse
import sys


GUIDELINES = {
    "rct": ("CONSORT", "randomized clinical trial"),
    "randomized-clinical-trial": ("CONSORT", "randomized clinical trial"),
    "cluster-rct": ("CONSORT extension", "cluster randomized clinical trial"),
    "noninferiority-rct": ("CONSORT extension", "noninferiority randomized clinical trial"),
    "nonrandomized-trial": ("TREND", "nonrandomized clinical trial"),
    "cohort": ("STROBE", "cohort study"),
    "case-control": ("STROBE", "case-control study"),
    "cross-sectional": ("STROBE", "cross-sectional study"),
    "meta-analysis": ("PRISMA", "meta-analysis"),
    "systematic-review": ("PRISMA", "systematic review"),
    "diagnostic": ("STARD", "diagnostic accuracy study"),
    "prediction-model": ("TRIPOD", "prediction model study"),
    "quality-improvement": ("SQUIRE", "quality improvement study"),
    "economic-evaluation": ("CHEERS", "economic evaluation"),
    "qualitative": ("SRQR/COREQ", "qualitative study"),
    "case-report": ("CARE", "case report"),
    "survey": ("AAPOR best practices", "survey study"),
    "genetic-association": ("STREGA", "genetic association study"),
}


JAMA_RULES = {
    "rct": {
        "article_type": "Original Investigation",
        "subtitle": "A Randomized Clinical Trial",
        "abstract": "Importance; Objective; Design; Setting; Participants; Intervention(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": [
            "3 Key Points",
            "trial registration and ID",
            "trial protocol",
            "CONSORT checklist",
            "flow diagram",
            "data sharing statement",
        ],
    },
    "randomized-clinical-trial": {
        "article_type": "Original Investigation",
        "subtitle": "A Randomized Clinical Trial",
        "abstract": "Importance; Objective; Design; Setting; Participants; Intervention(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": [
            "3 Key Points",
            "trial registration and ID",
            "trial protocol",
            "CONSORT checklist",
            "flow diagram",
            "data sharing statement",
        ],
    },
    "cluster-rct": {
        "article_type": "Original Investigation",
        "subtitle": "A Randomized Clinical Trial",
        "abstract": "Importance; Objective; Design; Setting; Participants; Intervention(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": [
            "3 Key Points",
            "trial registration and ID",
            "trial protocol",
            "CONSORT extension checklist",
            "cluster flow diagram",
            "data sharing statement",
        ],
    },
    "noninferiority-rct": {
        "article_type": "Original Investigation",
        "subtitle": "A Randomized Clinical Trial",
        "abstract": "Importance; Objective; Design; Setting; Participants; Intervention(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": [
            "3 Key Points",
            "trial registration and ID",
            "trial protocol",
            "CONSORT extension checklist",
            "flow diagram",
            "data sharing statement",
        ],
    },
    "nonrandomized-trial": {
        "article_type": "Original Investigation",
        "subtitle": "A Nonrandomized Clinical Trial",
        "abstract": "Importance; Objective; Design; Setting; Participants; Intervention(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": [
            "3 Key Points",
            "registration and ID if applicable",
            "protocol",
            "flow diagram",
            "data sharing statement",
        ],
    },
    "cohort": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
    "case-control": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
    "cross-sectional": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
    "meta-analysis": {
        "article_type": "Original Investigation",
        "subtitle": "Title should include 'A Meta-analysis'",
        "abstract": "Importance; Objective; Evidence Review; Findings; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement", "PRISMA flow", "review checklist"],
    },
    "systematic-review": {
        "article_type": "Systematic Review",
        "subtitle": "A Systematic Review",
        "abstract": "Importance; Objective; Evidence Review; Findings; Conclusions and Relevance",
        "requires": ["3 Key Points", "PRISMA-style flow diagram", "evidence-quality table"],
    },
    "diagnostic": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
    "prediction-model": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
    "quality-improvement": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
    "economic-evaluation": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
    "qualitative": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
    "case-report": {
        "article_type": "Brief report or case report outside JAMA main journal",
        "subtitle": "Journal-specific",
        "abstract": "Verify live target-journal format",
        "requires": ["CARE checklist", "explicit chronology", "patient consent if identifiable"],
    },
    "survey": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement", "response-rate reporting"],
    },
    "genetic-association": {
        "article_type": "Original Investigation",
        "subtitle": "None",
        "abstract": "Importance; Objective; Design; Setting; Participants; Exposure(s); Main Outcomes and Measures; Results; Conclusions and Relevance",
        "requires": ["3 Key Points", "data sharing statement"],
    },
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a compact medical-journal preflight checklist.")
    parser.add_argument("--study-type", required=True, help="e.g. rct, cohort, meta-analysis, qualitative")
    parser.add_argument("--target-journal", default="jama", help="e.g. jama, nejm, lancet")
    return parser


def normalize(value: str) -> str:
    return value.strip().lower().replace("_", "-").replace(" ", "-")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    study_type = normalize(args.study_type)
    target_journal = normalize(args.target_journal)

    if study_type not in GUIDELINES:
        valid = ", ".join(sorted(GUIDELINES))
        print(f"Unknown study type: {args.study_type}", file=sys.stderr)
        print(f"Supported values: {valid}", file=sys.stderr)
        return 2

    guideline, label = GUIDELINES[study_type]
    journal_rules = JAMA_RULES.get(study_type, JAMA_RULES["cohort"])

    print(f"# Preflight: {label}")
    print()
    print(f"- Target journal: {target_journal}")
    print(f"- Recommended reporting standard: {guideline}")
    print(f"- JAMA-oriented article type: {journal_rules['article_type']}")
    print(f"- Subtitle convention: {journal_rules['subtitle']}")
    print(f"- Abstract pattern: {journal_rules['abstract']}")
    print("- Core checks:")
    for item in journal_rules["requires"]:
        print(f"  - {item}")
    print("  - ethics approval and consent language if applicable")
    print("  - funding, conflicts, acknowledgments, and author contributions")
    print("  - AI-use disclosure if AI materially assisted writing, analysis, or figures")

    if target_journal != "jama":
        print()
        print("Note: non-JAMA targets should use this as a starting checklist only; verify the live journal instructions before final formatting.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
