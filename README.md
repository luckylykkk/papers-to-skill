# Papers To Skill

> Turn your frontier literature folder into a reusable, citation-grounded domain expert skill.<br>
> 把你的前沿文献文件夹，变成一个可复用、可引用的领域研究专家 Skill。

![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)
![Citation Grounded](https://img.shields.io/badge/answers-citation--grounded-green)
![Local Corpus](https://img.shields.io/badge/knowledge-user--supplied-orange)

`papers-to-skill` packages the papers and research materials in a user-provided folder into a reusable expert skill. The generated skill can then answer field-specific research questions with citations from the supplied corpus.

- [Quick Install](#quick-install)
- [Three-Step Use](#three-step-use)
- [Real Anonymized Case Study](#real-anonymized-case-study)
- [Not RAG, Not A One-Off Summary](#not-rag-not-a-one-off-summary)
- [Architecture](#architecture)
- [Usage Workflow](#usage-workflow)
- [中文说明](#中文说明)

## Quick Install

Tell your agent:

```text
Install this skill: git@github.com:luckylykkk/papers-to-skill.git
```

中文：

```text
安装这个 skill：git@github.com:luckylykkk/papers-to-skill.git
```

## Three-Step Use

1. **Put the knowledge you want to include into one folder.**

   ```text
   my-research-corpus/
   +-- paper-01.pdf
   +-- paper-02.pdf
   +-- paper-03.pdf
   ```

2. **Use `/papers-to-skill` to generate a domain expert skill from that folder.**

   ```text
   /papers-to-skill Turn <your-literature-folder> into a domain research expert skill.
   ```

3. **Use the generated expert skill for frontier domain Q&A and research tasks.**

   ```text
   /<generated-skill-name> What are the hottest research directions in this field, and what could be done next?
   /<generated-skill-name> Find statistical references for this parameter.
   /<generated-skill-name> Evaluate this study design and cite supporting papers.
   ```

Replace `<your-literature-folder>` with your own local folder. Do not put private local paths in public documentation. Replace `<generated-skill-name>` with the actual skill name generated from your corpus.

## Real Anonymized Case Study

This is an anonymized version of a real workflow. The original local path is intentionally replaced with a placeholder.

```text
/papers-to-skill Turn <diabetes-pcat-ccta-literature-folder> into a domain research expert skill.
```

Generated result:

```text
Generated skill: diabetes-pcat-ccta

Processed corpus:
- 1059 BibTeX records
- 861 PDFs
- about 810 unique papers after PMID / file-ID deduplication
- 51 duplicate PDF groups detected
- 52 highly relevant core papers fully extracted

Generated files:
- SKILL.md
- papers.md
- evidence-table.md
- methods.md
- concepts.md
- contradictions.md
- reading-map.md
- validation-report.md

Validation:
- quick_validate.py passed
- globally installed skill also passed validation
- citation key consistency check passed
```

Then the generated skill was used for domain-specific questions:

```text
/diabetes-pcat-ccta I want to run a regression analysis on coronary calcium score. Help me find references.

/diabetes-pcat-ccta Which papers used Kaplan-Meier curves and ROC prediction models?

/diabetes-pcat-ccta Give me clickable paper paths for the KM + ROC papers.
```

Example answer behavior:

```text
For coronary calcium score regression, use log(CACS + 1) for skewed continuous CACS,
consider CACS > 400 as a binary sensitivity analysis, and adjust for clinical risk factors,
CAD-RADS, plaque burden, and PCAT/FAI when aligned with the research endpoint.

The answer includes paper-key references from the generated corpus.
```

## Not RAG, Not A One-Off Summary

`papers-to-skill` is not just a RAG index and not just a one-time literature summary.

It generates a reusable skill: a compact operating layer that captures how the literature should guide future answers. The generated skill includes evidence tables, methods, concepts, contradictions, reading maps, validation notes, and citation rules. You can invoke it repeatedly for new research questions after the corpus has been distilled.

In other words:

- **RAG** retrieves relevant chunks.
- **A literature summary** describes papers once.
- **A generated skill** turns the corpus into a reusable domain assistant with rules, boundaries, and citations.

## Why This Exists

General AI is often strong at reasoning, but weak answers in frontier academic fields are frequently caused by missing domain-specific prior knowledge. The model may not know the newest papers, the latest parameter conventions, the most relevant negative results, or what reviewers in a narrow field currently care about.

`papers-to-skill` is designed to close that gap by letting users bring their own literature corpus. Instead of asking a general model to answer from broad training memory, you first package your field-specific papers into a skill, then use that skill for grounded consultation.

## What It Can Help With

- research idea evaluation
- study design
- parameter and statistical references
- method selection
- evidence lookup
- reviewer-risk checks
- domain-specific Q&A with citations

## Architecture

The architecture is shown with an Image2-generated diagram:

![papers-to-skill architecture](assets/papers-to-skill-architecture.png)

## Usage Workflow

The usage workflow is shown with an Image2-generated diagram:

![papers-to-skill usage workflow](assets/papers-to-skill-workflow.png)

## What Gets Distilled

The generated expert skill is built from six evidence lanes:

| Lane | What it extracts |
|---|---|
| Claims | Major findings, hypotheses, and evidence strength |
| Methods | Study design, datasets, metrics, statistical models, algorithms |
| Concepts | Definitions, taxonomies, assumptions, and relationships |
| Contradictions | Negative results, disagreements, boundary conditions |
| Applications | How the evidence changes research decisions or agent behavior |
| Reading map | Where to look when answering future questions |

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

## Honest Boundaries

Every generated skill should state what it cannot do:

- it is only as current as the supplied corpus
- it should not invent citations, thresholds, sample sizes, or effect sizes
- it should distinguish strong evidence from weak or single-paper evidence
- it should not treat model output as clinical, legal, or financial advice
- it should cite the source papers for substantive claims

## 中文说明

### 快速安装

告诉你的 agent：

```text
安装这个 skill：git@github.com:luckylykkk/papers-to-skill.git
```

### 三步使用

1. **把需要纳入的相关知识放在一个文件夹下。**

   ```text
   my-research-corpus/
   +-- paper-01.pdf
   +-- paper-02.pdf
   +-- paper-03.pdf
   ```

2. **使用 `/papers-to-skill` 把该目录生成相关领域专家 skill。**

   ```text
   /papers-to-skill 帮我把 <your-literature-folder> 目录生成相关领域专家skill
   ```

3. **使用生成的领域专家 skill 进行专业前沿知识问答。**

   ```text
   /<generated-skill-name> 告诉我目前该领域最热门的研究方向和接下来可以做的研究方向有哪些
   /<generated-skill-name> 帮我查找某个参数或统计方法的参考
   /<generated-skill-name> 帮我评估这个研究设计，并给出文献来源
   ```

其中 `<your-literature-folder>` 需要替换为你自己的本地文献目录；公开 README 中不要写入真实私人路径。`<generated-skill-name>` 需要替换为实际生成出来的 skill 名称。

### 真实匿名案例

下面是一次真实使用流程的匿名化版本。原始本地路径已被替换为占位目录，避免在公开 README 中暴露私人路径。

```text
/papers-to-skill 帮我把 <diabetes-pcat-ccta-literature-folder> 目录生成相关领域专家skill
```

生成结果：

```text
生成的 skill：diabetes-pcat-ccta

处理语料：
- 扫描到 1059 条 BibTeX 记录
- 扫描到 861 个 PDF
- 按 PMID / 文件 ID 去重后约 810 篇
- 发现 51 组重复 PDF
- 抽取 52 篇高相关核心文献全文，全部成功

生成文件：
- SKILL.md
- papers.md
- evidence-table.md
- methods.md
- concepts.md
- contradictions.md
- reading-map.md
- validation-report.md

验证结果：
- quick_validate.py 通过
- 全局安装版本通过验证
- 引用 key 一致性检查通过
```

随后可以直接使用生成的领域专家 skill 提问：

```text
/diabetes-pcat-ccta 比如说我要对钙化积分进行回归分析，帮我找到参考

/diabetes-pcat-ccta 有哪些文章使用了KM曲线和ROC预测模型

/diabetes-pcat-ccta 给出KM + ROC文章的可点击目录
```

示例回答效果：

```text
对于钙化积分回归分析，可以把 CACS 作为连续结局、分类结局或预测因子处理。
连续型 CACS 通常建议使用 log(CACS + 1)；
敏感性分析可考虑 CACS > 400；
模型中应结合年龄、性别、BMI、糖尿病相关指标、CAD-RADS、斑块负荷、PCAT/FAI 等变量。

回答会附带来自生成文献库的 paper-key 引用来源。
```

### 不是 RAG，也不是普通文献总结

`papers-to-skill` 不是简单建立一个 RAG 检索库，也不是生成一份一次性的文献综述。

它生成的是一个可复用的 skill：一个浓缩后的领域操作层。这个 skill 会保存证据表、方法、概念、矛盾与边界、阅读地图、验证结果和引用规则。之后你可以反复调用它，回答新的研究问题。

换句话说：

- **RAG** 主要检索相关片段。
- **普通文献总结** 主要一次性概括论文。
- **生成的 skill** 会把文献库变成一个可复用、有边界、有引用规则的领域研究助手。

### 它会提取什么

| 通道 | 提取内容 |
|---|---|
| 核心结论 | 主要发现、假设、证据强度 |
| 研究方法 | 研究设计、数据集、指标、统计模型、算法 |
| 关键概念 | 定义、分类、假设、概念关系 |
| 矛盾与边界 | 阴性结果、冲突发现、适用边界 |
| 应用场景 | 文献如何改变研究决策或 agent 行为 |
| 阅读地图 | 后续回答问题时应该查哪篇文献、哪个部分 |

### 引用规则

生成后的专家 skill 在回答实质性问题时，应该引用 `references/papers.md` 中的文献来源。
