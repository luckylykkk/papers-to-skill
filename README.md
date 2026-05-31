# Papers To Skill

`papers-to-skill` converts a folder of academic papers and related research knowledge into a reusable, citation-grounded domain expert skill.

- [English](#english)
- [中文](#中文)

## English

### What It Does

`papers-to-skill` helps users package their own frontier literature corpus into a domain research assistant skill.

The generated skill is intended for later consultation on research ideas, study design, parameter choices, statistical references, method selection, evidence lookup, and reviewer-risk checks.

It combines three patterns:

- book-style paper extraction into structured evidence
- multi-lane synthesis across claims, methods, concepts, contradictions, applications, and reading maps
- validation and scoring before treating the generated expert skill as usable

### Why This Matters

In many research workflows, the professional knowledge needed for a real project differs from broad general-domain knowledge. Model training data can also lag behind the latest literature, and this gap becomes larger in specialized vertical fields where methods, evidence, parameters, and reviewer expectations change quickly.

When we directly use a general-purpose AI model for academic discussion, the answer may fail to reflect the newest frontier research. This is usually not because the model lacks reasoning ability, but because it lacks the domain-specific prior knowledge needed for that scenario.

`papers-to-skill` is designed for that gap. It lets users package the newest papers from their own field into a reusable research assistant skill. Answers generated through that skill can then combine the model's reasoning ability with the user's own frontier literature corpus, producing responses that are more current, evidence-grounded, and closer to the actual research scenario.

### Three-Step Workflow

1. **Put the knowledge you want to include into one folder.**

   This folder can contain the papers or related research materials you want the generated skill to use as its evidence base.

   ```text
   my-research-corpus/
   +-- paper-01.pdf
   +-- paper-02.pdf
   +-- paper-03.pdf
   ```

2. **Use this tool to package that folder into a skill.**

   Start by extracting the paper corpus:

   ```bash
   python scripts/extract_papers.py <pdf-or-folder> --out <workdir>
   ```

   Then follow `SKILL.md` to synthesize the extracted evidence into a domain expert skill.

3. **Use the generated skill for frontier domain Q&A and research tasks.**

   After the skill is generated, use it as a specialized research assistant for questions that need the latest field-specific knowledge.

   Example prompts:

   ```text
   Use <generated-skill-name> to evaluate this research design and cite supporting papers.
   Use <generated-skill-name> to find statistical references for this parameter.
   Use <generated-skill-name> to identify reviewer risks in this study idea.
   ```

### Output Shape

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

### Citation Rule

Every substantive answer from a generated expert skill should include paper references from `references/papers.md`.

## 中文

### 这个工具做什么

`papers-to-skill` 可以把一个文件夹中的学术论文和相关研究知识，转换成一个可复用、带文献来源的垂直领域研究助手 skill。

生成后的 skill 可以用于后续咨询，例如研究想法评估、研究设计、参数选择、统计方法参考、方法学选择、证据查找、审稿风险检查等。

它结合了三类能力：

- 类似 `book-to-skill`：把论文提取成结构化证据，而不是简单堆叠原文
- 类似 `nuwa-skill`：从 claims、methods、concepts、contradictions、applications、reading map 等多个角度综合文献
- 类似 `darwin-skill`：在生成后进行验证、评分和修正，确保生成的 skill 可用

### 为什么需要它

在很多真实科研场景中，我们需要的专业知识往往和通用领域知识存在差距。模型训练获得的知识也可能与垂直领域最新文献之间存在时间差和专业差。

当我们直接使用通用型 AI 进行对话时，回答往往不能贴近最前沿的学术研究领域；这并不是模型的智力水平不够，而是它缺乏相关领域的前置知识。

因此，这个工具的目标是把用户自己相关领域的前沿文献打包成一个可复用的研究助手 skill。基于这个研究助手生成的回答，可以结合该领域最新证据、方法和参数参考，给出更真实、更贴近具体场景的建议。

### 三步使用流程

1. **把需要纳入的相关知识放在一个文件夹下。**

   这个文件夹可以放入你希望 skill 学习和引用的论文 PDF 或其他相关研究材料。

   ```text
   my-research-corpus/
   +-- paper-01.pdf
   +-- paper-02.pdf
   +-- paper-03.pdf
   ```

2. **使用这个工具把文件夹下的文件打包成 skill。**

   先运行提取脚本：

   ```bash
   python scripts/extract_papers.py <pdf-or-folder> --out <workdir>
   ```

   然后按照 `SKILL.md` 中的流程，把提取出来的文献证据综合成一个领域专家 skill。

3. **使用生成的 skill 进行专业前沿知识问答或其他研究需求。**

   生成 skill 后，就可以把它作为垂直领域研究助手来调用，用于需要前沿专业知识的问题。

   示例：

   ```text
   使用 <generated-skill-name>，帮我评估这个研究设计，并给出文献来源。
   使用 <generated-skill-name>，帮我查找某个参数或统计方法的参考。
   使用 <generated-skill-name>，帮我判断这个研究想法可能会被审稿人质疑的地方。
   ```

### 输出结构

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

### 引用规则

生成后的专家 skill 在回答实质性问题时，应该引用 `references/papers.md` 中的文献来源。
