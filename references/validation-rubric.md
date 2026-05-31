# Validation Rubric

Use this Darwin-style rubric after generating a literature-backed skill.

| Dimension | Weight | Check |
|---|---:|---|
| Trigger clarity | 10 | Frontmatter says what the skill does and when to use it. |
| Workflow executability | 15 | Steps are ordered, concrete, and have clear inputs and outputs. |
| Evidence grounding | 20 | Non-obvious claims trace to `references/evidence-table.md` and answer examples include paper-key citations. |
| Cross-paper synthesis | 15 | The skill extracts consensus, contradictions, methods, and boundary conditions instead of summarizing papers one by one. |
| Failure handling | 10 | The skill says what to do when evidence is weak, PDFs fail, or papers disagree. |
| Actionable specificity | 15 | Instructions avoid vague phrases and include concrete decision rules. |
| Reference design | 10 | Dense evidence lives in references; `SKILL.md` stays compact. |
| Test performance | 5 | The skill handles 2-3 realistic prompts without overclaiming. |

Score each dimension 1-10, multiply by weight, then divide total by 10.

## Required Test Prompts

Create at least:

1. A normal use prompt that asks the generated skill to solve its core task.
2. A disagreement prompt that asks about a contested claim or boundary condition.
3. A method prompt that asks for a reproducible procedure, metric, or evaluation recipe.

Each test output must include a `References` section with paper keys unless the correct answer is "the corpus has no evidence"; in that case it must cite nearest related papers or state no relevant paper exists.

## Keep Or Revise

- Keep the generated skill when score is at least 80 and no evidence-grounding failure is found.
- Treat missing references in substantive answers as an evidence-grounding failure.
- Revise once when score is below 80 or the weakest dimension is below 7.
- Do not make broad rewrites during validation. Fix the single weakest dimension first.
- Record failed tests and residual risks in `references/validation-report.md`.
