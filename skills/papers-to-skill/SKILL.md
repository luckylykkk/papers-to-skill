---
name: papers-to-skill
description: Converts multiple research paper PDFs into a grounded domain research expert skill by combining book-to-skill style document extraction, nuwa-skill style multi-source distillation, and darwin-skill style validation and optimization. Use when the user provides a folder, glob, or list of academic PDFs and wants a literature-backed expert skill for research ideas, study design, parameter/statistical references, method selection, evidence lookup, domain knowledge, paper collection distillation, multi-paper framework extraction, citation-grounded consultation, or comparison across papers.
allowed-tools: [Read, Write, Edit, MultiEdit, Glob, Grep, Bash, LS]
---

# Papers To Skill

Transform a literature corpus into a reusable domain research expert skill. The generated skill should answer later research questions as a field-specific consultant that can cite the paper-derived evidence base.

Example: a folder of muscle imaging quantification papers should generate a skill such as `muscle-imaging-quantification`, usable later for study design, segmentation/measurement choices, quantitative imaging metrics, cohort and parameter references, statistical analysis choices, baselines, and reviewer-risk checks.

Combine three patterns:

- **book-to-skill pattern**: extract each PDF into structured, on-demand knowledge instead of raw text dumps.
- **nuwa-skill pattern**: run multi-lane distillation across evidence types, then synthesize the corpus into an operating viewpoint.
- **darwin-skill pattern**: validate the generated skill with tests, score it, and revise only when quality improves.

Optimize for grounded synthesis across papers, not paper-by-paper summaries. The output is an expert operating layer over the corpus.

## Core Output

Generate a domain expert skill folder containing:

```
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

Use extra reference files only when they reduce context load. Do not paste raw paper text into the generated skill.

Use `references/domain-expert-template.md` as the target skill skeleton and `references/research-synthesis-framework.md` as the extraction method.

The generated expert skill must support later consultation prompts such as:

- "Evaluate this research idea against the literature."
- "Find design references for this study."
- "Which parameter range or statistical method is supported by these papers?"
- "What baselines, metrics, ablations, or failure modes should I consider?"
- "What would a reviewer challenge?"

Every substantive answer from the generated expert skill must include paper references. Use stable citation keys from `references/papers.md`, and include a short `References` section unless the user explicitly asks for brainstorming without citations.

## Modes

Route by user intent:

- **Full conversion**: PDF path(s) or folder provided with no qualifier. Extract, synthesize, and generate the skill.
- **Analyze only**: User asks to inspect, compare, summarize, map, or review before generation. Produce the synthesis report and stop.
- **Generate from notes**: User provides existing paper notes or extracted text. Skip extraction and generate from those notes.
- **Update existing skill**: User asks to add new papers to an existing skill. Read existing `references/papers.md` and append only new evidence.

## Pipeline

Use this order:

1. **Book phase**: extract and structure each paper.
2. **Nuwa phase**: distill the corpus through six evidence lanes and preserve lane outputs.
3. **Synthesis checkpoint**: inspect evidence quality before writing the expert skill.
4. **Skill phase**: generate a compact domain expert skill plus references.
5. **Darwin phase**: test, score, improve, or record limits.

## Step 1: Resolve Inputs

Accept any of:

- A directory containing PDFs
- One or more PDF paths
- A glob pattern such as `papers/*.pdf`
- A manifest or notes file that points to PDFs

Reject non-PDF primary inputs unless the user is in "generate from notes" mode.

Ask at most one clarification only if the target skill domain is impossible to infer from filenames, abstracts, or user wording. Otherwise infer a concise skill name from the corpus topic.

## Step 2: Extract Paper Text

Run the bundled extractor:

```bash
python scripts/extract_papers.py <pdf-or-folder> --out <workdir>
```

Use `--install-missing no` by default in non-interactive contexts. Use `--install-missing yes` only when the user explicitly wants package installation.

The script writes:

- `manifest.json`: per-paper metadata and extraction status
- `texts/<paper-id>.txt`: extracted text

If extraction fails for a paper, keep it in `manifest.json` with `status=failed`, continue with the rest, and report the failed filenames.

## Step 3: Book Phase - Structure Each Paper

For each extracted paper, read title, abstract, introduction, method, results, limitations, and conclusion sections when present. For long papers, use targeted section reads instead of loading entire files.

Create a book-to-skill style inventory for each paper:

- citation key
- title
- year
- research question
- core framework or hypothesis
- method or dataset
- main claims
- evidence strength
- limitations
- reusable concepts
- operational procedures
- anti-patterns or warnings

Use the schema in `references/evidence-schema.md` when generating final reference files.

## Step 4: Nuwa Phase - Distill The Corpus

Analyze the same corpus through six lanes. Run lanes in parallel when subagents are available; otherwise process them sequentially and keep the lane outputs separate until synthesis.

| Lane | Purpose | Output target |
|---|---|---|
| 1. Claims | Extract major claims, hypotheses, and findings | `references/research/01-claims.md` |
| 2. Methods | Extract procedures, datasets, metrics, prompts, algorithms, and evaluation recipes | `references/research/02-methods.md` |
| 3. Concepts | Extract definitions, taxonomies, assumptions, and relationships | `references/research/03-concepts.md` |
| 4. Contradictions | Extract disagreements, negative results, boundary conditions, and replication issues | `references/research/04-contradictions.md` |
| 5. Applications | Extract when the literature changes an agent workflow or user decision | `references/research/05-applications.md` |
| 6. Reading map | Map topics to papers and sections for on-demand lookup | `references/research/06-reading-map.md` |

Each lane must distinguish:

- what the paper explicitly says
- what multiple papers jointly support
- what is inferred by the agent
- what remains unknown

## Step 5: Evidence Review Checkpoint

Before generating the expert skill, produce a short evidence review:

```markdown
| Lane | Paper coverage | Strongest finding | Weakest area |
|---|---:|---|---|
| Claims | <N papers> | <finding> | <gap> |
| Methods | <N papers> | <finding> | <gap> |
| Concepts | <N papers> | <finding> | <gap> |
| Contradictions | <N papers> | <finding> | <gap> |
| Applications | <N papers> | <finding> | <gap> |
| Reading map | <N papers> | <finding> | <gap> |
```

If a lane has weak coverage, keep going but write the weakness into the generated skill's scope limits. Do not compensate by inventing authority.

## Step 6: Synthesize Across Papers

Extract cross-paper structure:

- **Consensus**: claims supported by multiple papers.
- **Contradictions**: incompatible findings, boundary conditions, or measurement differences.
- **Method patterns**: repeatable procedures, evaluation setups, data processing steps, prompts, metrics, or algorithms.
- **Concept map**: terms, definitions, assumptions, and relationships.
- **Decision rules**: when to use a method, when not to use it, and what evidence justifies that rule.
- **Open questions**: unresolved gaps that the generated skill must not overclaim.

Do not flatten disagreement into a single answer. Preserve minority findings when they change how the skill should behave.

Use `references/research-synthesis-framework.md` to decide which extracted ideas qualify as expert operating principles.

## Step 7: Generate The Skill

`SKILL.md` for the generated skill must include:

- frontmatter with precise trigger description
- domain identity card: what expert role this skill plays
- step-by-step operating workflow
- question router for research ideas, study design, methods, parameters/statistics, evidence lookup, and reviewer risk
- answer format that includes recommendation, evidence basis, caveats, next step, and references
- evidence-grounded decision rules
- domain operating principles that passed synthesis validation
- failure modes and fallback paths
- explicit "do not do" rules
- scope limits and non-goals
- pointers to reference files

Use `references/domain-expert-template.md` as the skeleton.
Keep `SKILL.md` under 500 lines. Put dense paper evidence in `references/`.

## Step 8: Generate References

Create these files:

- `references/papers.md`: citation inventory, one section per paper.
- `references/evidence-table.md`: claim -> supporting papers -> confidence -> caveats.
- `references/concepts.md`: definitions and concept relationships.
- `references/methods.md`: reusable procedures and evaluation recipes.
- `references/contradictions.md`: disagreements, boundary conditions, and unresolved questions.
- `references/reading-map.md`: which paper/section to read for each topic.
- `references/validation-report.md`: test prompts, scores, changes made, residual risks.

Every non-obvious claim in the generated skill must trace back to at least one paper in `evidence-table.md`.
Every generated answer protocol must require paper-key citations for substantive claims.

## Step 9: Darwin Phase - Validate And Improve

Score the generated skill before reporting completion. Use `references/validation-rubric.md` as the scoring guide.

1. Create 2-3 realistic user prompts for the generated skill.
2. Dry-run the skill against those prompts, or spawn independent evaluators when available.
3. Check every generated reference file exists.
4. Check `SKILL.md` does not cite claims absent from `evidence-table.md`.
5. Check the generated answer format includes a `References` section with paper keys.
6. Check failed or weak extractions are listed in the final report.
7. Identify the lowest scoring dimension and make one focused revision.
8. Keep the revision only if the skill becomes more specific, more grounded, or easier to execute.
9. Run quick validation on the generated skill if the validator is available:

```bash
python <skill-creator>/scripts/quick_validate.py <generated-skill-folder>
```

Write results to `references/validation-report.md`.

## Quality Rules

- Prefer synthesis over summaries.
- Separate "paper claims" from "agent instructions."
- Use book-to-skill extraction discipline, nuwa-style multi-lane synthesis, and darwin-style validation.
- Mark confidence as `high`, `medium`, or `low`; do not use numeric precision unless the papers provide it.
- Keep citations stable with keys like `smith-2024-transformers`.
- Require paper references in the generated expert skill's answers. The default answer should end with `References`.
- Never invent paper metadata, results, benchmarks, or publication venues.
- Do not quote long passages from papers. Summarize and cite the source paper key.
- Do not hide failed extractions; partial corpora create partial skills.

## Failure Handling

- If fewer than two papers extract successfully, switch to single-paper behavior and state that cross-paper synthesis is not possible.
- If papers are unrelated, generate a taxonomy first and ask for no more than one routing decision before skill generation.
- If abstracts and conclusions contradict extracted body text, prefer the body text and record the discrepancy in `contradictions.md`.
- If PDF extraction loses tables or equations needed for the task, recommend rerunning extraction with a layout-aware tool and mark affected claims as low confidence.
