# Research Synthesis Framework

Use this framework to turn a paper corpus into domain expert behavior.

## Three Tests For Expert Operating Principles

An extracted idea qualifies as a domain operating principle only if it passes all three tests.

### 1. Cross-paper support

The idea appears in at least two papers, or one strong paper plus one independent supporting source inside the corpus.

If it appears in only one paper, keep it as a paper-specific finding, not a general rule.

### 2. Generative use

The idea helps answer a new research question, design a study, choose a method, pick a parameter/statistic, or predict reviewer concerns.

If it cannot guide a new decision, put it in `concepts.md` or `papers.md`, not the generated `SKILL.md` core workflow.

### 3. Field specificity

The idea is specific to this field or corpus. Avoid generic rules such as "use appropriate statistics" or "validate on external data" unless the papers define exactly how and when.

If the idea is generic but important, write it as a checklist item with paper-specific details.

## Evidence Classes

Use these labels consistently:

- **consensus**: supported by multiple papers with compatible methods and findings.
- **promising**: supported by limited evidence but useful for hypothesis generation.
- **contested**: papers disagree or results depend on dataset, population, metric, or protocol.
- **negative**: papers show failure, no effect, or an important limitation.
- **unknown**: the corpus does not answer the question.

## Research Expert Skill Sections

Map synthesis outputs into the generated skill:

| Synthesis output | Generated skill destination |
|---|---|
| consensus principles | Core operating principles |
| methods and protocols | Method selection workflow |
| parameters/statistics | Parameter and statistics reference workflow |
| contradictions | Uncertainty and boundary handling |
| negative findings | Failure modes and "do not do" rules |
| open questions | Scope limits and research opportunity finder |

## Contradiction Handling

Do not merge disagreements into a bland average. For each contradiction, record:

- what each side claims
- which papers support each side
- likely reason for disagreement
- how the expert skill should behave when asked about it

When answering later, the generated skill should say "the corpus is contested here" and route the user to the specific evidence.

## Output Standard

A good generated expert skill can do all of these:

- evaluate a new idea against the corpus
- propose a study design with evidence-backed choices
- identify parameters, statistics, baselines, and metrics used in the literature
- warn about known failure modes and reviewer objections
- cite the paper-derived evidence files without overclaiming
