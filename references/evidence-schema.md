# Evidence Schema

Use these structures when turning multiple papers into a skill.

## Paper Entry

```markdown
## <citation-key>

- **Title**:
- **Authors**:
- **Year**:
- **Venue/DOI**:
- **Source file**:
- **Research question**:
- **Method/data**:
- **Main findings**:
- **Reusable concepts**:
- **Operational methods**:
- **Limitations**:
- **Evidence strength**: high | medium | low
```

## Citation Key Rules

Use stable citation keys:

```text
<first-author-lastname>-<year>-<short-topic>
```

Examples:

- `smith-2024-muscle-ct`
- `lee-2023-fat-infiltration`

If two papers collide, append `-a`, `-b`, or a second author name. Use the same key in every generated file and answer.

## Evidence Table Row

```markdown
| Claim | Supporting papers | Confidence | Caveats | Skill implication |
|---|---|---|---|---|
| <specific claim> | <key1>; <key2> | high/medium/low | <limits> | <how the generated skill should act> |
```

## Contradiction Entry

```markdown
## <topic>

- **Position A**: <claim> - <paper keys>
- **Position B**: <claim> - <paper keys>
- **Likely reason**: dataset, method, population, metric, scope, or time period
- **Skill behavior**: how to handle this uncertainty when answering users
```

## Generated Skill Reference Pattern

In the generated `SKILL.md`, point to evidence instead of repeating it:

```markdown
For claims, confidence, and caveats, read `references/evidence-table.md`.
For method details, read `references/methods.md`.
```

The generated skill must instruct answers to include:

```markdown
## References
- `<paper-key>` - <short title>, <year>
```
