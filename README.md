# Papers To Skill

`papers-to-skill` converts a folder of academic PDFs into a reusable, citation-grounded domain expert skill.

It combines three patterns:

- book-style paper extraction into structured evidence
- multi-lane synthesis across claims, methods, concepts, contradictions, applications, and reading maps
- validation and scoring before treating the generated expert skill as usable

The generated expert skill is intended for later consultation on research ideas, study design, parameter choices, statistical references, method selection, evidence lookup, and reviewer-risk checks.

## Scenario

In many research workflows, the professional knowledge needed for a real project differs from broad general-domain knowledge. Model training data can also lag behind the latest literature, and this gap becomes larger in specialized vertical fields where methods, evidence, parameters, and reviewer expectations change quickly.

`papers-to-skill` is designed for that gap. It lets users package the newest papers from their own field into a reusable research assistant skill. Answers generated through that skill can then combine the model's reasoning ability with the user's own frontier literature corpus, producing responses that are more current, evidence-grounded, and closer to the actual research scenario.

在很多真实科研场景中，我们需要的专业知识往往和通用领域知识存在差距。模型训练获得的知识也可能与垂直领域最新文献之间存在时间差和专业差。因此，这个脚本的目标是把用户自己相关领域的前沿文献打包成一个可复用的研究助手 skill。基于这个研究助手生成的回答，可以结合该领域最新证据、方法和参数参考，给出更真实、更贴近具体场景的建议。

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
