# Papers To Skill

`papers-to-skill` converts a folder of academic PDFs into a reusable, citation-grounded domain expert skill.

It combines three patterns:

- book-style paper extraction into structured evidence
- multi-lane synthesis across claims, methods, concepts, contradictions, applications, and reading maps
- validation and scoring before treating the generated expert skill as usable

The generated expert skill is intended for later consultation on research ideas, study design, parameter choices, statistical references, method selection, evidence lookup, and reviewer-risk checks.

## Usage

```bash
python scripts/extract_papers.py <pdf-or-folder> --out <workdir>
```

After extraction, use `SKILL.md` as the operating workflow for synthesizing the paper corpus into a domain expert skill.

## Output Shape

```text
<skill-name>/
+-- SKILL.md
+-- references/
    +-- research/
        +-- 01-claims.md
        +-- 02-methods.md
        +-- 03-concepts.md
        +-- 04-contradictions.md
        +-- 05-applications.md
        +-- 06-reading-map.md
    +-- papers.md
    +-- evidence-table.md
    +-- concepts.md
    +-- methods.md
    +-- contradictions.md
    +-- reading-map.md
    +-- validation-report.md
```

## Citation Rule

Every substantive answer from a generated expert skill should include paper references from `references/papers.md`.

