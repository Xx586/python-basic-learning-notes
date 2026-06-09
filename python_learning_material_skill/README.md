
# python-learning-material Skill 使用说明

## 这是什么？

`python-learning-material` 是一个 Claude Code 可复用 Skill，用于**系统化整理和生成面向零基础学生的 Python 基础语法学习资料**。

它把从多次 Claude Code 对话中沉淀出的完整工作流程固化为一套可复用的规则、模板和 prompt。

## 适合什么任务？

- 有一套 Python 学习路线、思维导图、截图和零散的旧资料，需要整理成系统化学习材料。
- 已经有了章节框架，需要逐章补充知识点讲解。
- 需要验证一套 Python 学习资料的质量。
- 需要把"生成学习资料"这件事变成可重复执行的流程。

## 不适合什么任务？

- 写单个 Python 脚本（不需要完整资料体系）。
- 翻译或格式化现有文档（不需要生成新内容）。
- 制作高级/专家级 Python 教程（本 Skill 面向零基础）。

## 目录结构

```
python_learning_material_skill/
├── SKILL.md                              # Skill 入口文件
├── README.md                             # 本文件 — 使用说明
├── references/                           # 规则集（参考资料）
│   ├── workflow.md                       #   完整 8 步工作流定义
│   ├── knowledge_point_rules.md          #   知识点文档规则集
│   └── acceptance_rules.md              #   验收规则集
├── templates/                            # 模板（复制使用）
│   ├── knowledge_point_template.md       #   知识点文档模板
│   ├── chapter_completion_report_template.md  #   章节完成报告模板
│   ├── final_acceptance_report_template.md    #   最终验收报告模板
│   └── issue_fix_report_template.md     #   问题修复报告模板
└── prompts/                              # Prompt（直接使用）
    ├── 01_scan_materials.md              #   资料盘点
    ├── 02_generate_framework.md          #   生成总框架
    ├── 03_complete_single_chapter.md     #   完善单个章节
    ├── 04_complete_multiple_chapters.md  #   完善多个章节
    ├── 05_final_acceptance.md            #   最终验收
    └── 06_fix_acceptance_issues.md       #   修复验收问题
```

## 如何在 Claude Code 中使用？

### 推荐使用顺序

如果你要从零开始整理一套完整的 Python 基础语法学习资料，请按以下顺序使用：

```
第 1 步：资料盘点（prompts/01_scan_materials.md）
    ↓
第 2 步：生成总框架（prompts/02_generate_framework.md）
    ↓
第 3 步：分章节完善（prompts/03_complete_single_chapter.md 或 04）
    ↓ (每章自检)
第 4 步：最终验收（prompts/05_final_acceptance.md）
    ↓
第 5 步：问题修复（prompts/06_fix_acceptance_issues.md）
```

### 示例指令

#### 资料盘点
```
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/01_scan_materials.md 进行资料盘点，不要修改文件。
```

#### 生成总框架
```
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/02_generate_framework.md，基于盘点报告生成 10 章总框架。
```

#### 完善单个章节
```
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/03_complete_single_chapter.md，只完善第 3 章：流程控制。
```

#### 完善多个章节
```
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/04_complete_multiple_chapters.md，完善第 6-10 章。
```

#### 最终验收
```
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/05_final_acceptance.md，对 10 个章节做最终验收。
```

#### 修复问题
```
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/06_fix_acceptance_issues.md，修复验收报告中的 A 类问题。
```

## 注意事项

1. **不要一次性生成全部内容** — 分批处理，每次一个章节，质量优先。
2. **先框架、再分章节、再验收** — 三阶段顺序不可跳过。
3. **不要删除原始资料** — 原始文件是宝贵资产。
4. **每章完成后自检** — 13 项检查标准，通过后再进入下一章。
5. **验收只查不改** — 验收报告输出后，由用户决定是否修复、修复哪些。
6. **任务过长时暂停** — 不为了赶进度压缩内容质量。
7. **不确定的内容标注"不确定"** — 不要编造。

## 前置要求

在使用本 Skill 之前，目标文件夹中应至少包含：
- 一份 Python 学习路线文件
- 一份项目规则文件（定义基本约束）

强烈建议同时包含：
- 一份详细 prompt 文件（定义完整生成规范）
- 一张思维导图（知识点结构全景）
- 知识点结构截图（补充验证）

## 从何处获取更多帮助？

- 详细工作流程：参考 `references/workflow.md`
- 知识点文档规范：参考 `references/knowledge_point_rules.md`
- 验收详细标准：参考 `references/acceptance_rules.md`
- 报告格式模板：参考 `templates/` 目录
## Skill 生成背景

`python_learning_material_skill` 是在本项目 Python 基础语法学习资料整理完成后，进一步沉淀出来的一套可复用 Skill。

本项目最初的目标是：基于已有的 Python 基础资料、学习路线、思维导图和知识点截图，生成一套适合零基础学生系统学习的 Python 基础语法资料。整个资料生成过程并不是一次性完成的，而是通过 Claude Code 多轮对话逐步推进完成的。

在资料生成过程中，Claude Code 结合 DeepSeek V4 Pro 模型，按照以下流程逐步完成资料整理：

1. 先扫描并阅读当前 `python1` 文件夹中的所有资料；
2. 识别已有的 1-10 个章节目录；
3. 阅读学习路线、思维导图、截图、旧版知识点文档和项目规则；
4. 生成 10 个章节的知识点总框架；
5. 按章节分批完善知识点讲解内容；
6. 为每个知识点补充 Demo 样例、典型例题、易错点、课后练习和答题总结；
7. 对前五章和后五章分别进行完善；
8. 最后对 10 个章节进行整体验收；
9. 根据验收结果修复结构缺失、内容不完整、Demo 不规范等问题；
10. 在资料生成完成后，再结合最终生成的资料、核心提示词文件和 Claude Code 对话记录，总结出本 Skill。

---

## Skill 的生成依据

本 Skill 不是凭空编写出来的，而是从以下资料中提炼生成的：

| 资料                   | 作用                                          |
| -------------------- | ------------------------------------------- |
| `promopt.txt`        | 记录生成本套 Python 学习资料时使用的核心提示词，是 Skill 的主要规则来源 |
| `CLAUDE.md`          | 记录 Claude Code 在本项目中的执行规范，例如固定框架、分批处理、自检要求等 |
| `00_资料总框架.md`        | 记录 10 个章节和全部知识点结构，是 Skill 生成知识框架时的重要参考      |
| `Python基础学习路线(5).md` | 作为知识点主线，决定章节顺序和学习路径                         |
| `2.AI应用学习方式.md`      | 作为学习流程和文件组织规范的参考                            |
| `思维导图.png`           | 取自鱼皮编程导航，用于辅助确认 Python 基础语法整体结构             |
| 1-10 章知识点文档          | 作为最终生成效果的样本，用于反推 Skill 的输出标准                |
| Claude Code 多轮对话记录   | 用于提炼资料盘点、分章节生成、验收和修复流程                      |

---

## Skill 的核心作用

这个 Skill 的作用是把一次成功的学习资料生成流程，沉淀成以后可以重复使用的规则包。

以后如果需要整理新的学习资料，可以使用这个 Skill 指导 AI 按照固定流程工作，而不是每次重新写一大段提示词。

它主要支持以下任务：

1. 自动盘点项目资料；
2. 阅读学习路线、旧资料、思维导图、截图和提示词；
3. 生成完整章节框架；
4. 按章节逐步完善知识点讲解；
5. 为每个知识点生成统一格式的 `.md` 文档；
6. 为每个知识点生成 Demo 样例；
7. 补充典型例题、课后练习和答案；
8. 总结易错点；
9. 对章节进行自检；
10. 对整个项目进行最终验收；
11. 根据验收报告修复问题。

---

## Skill 使用的知识点文档标准

本 Skill 要求每个知识点文档都使用统一的 8 部分结构：

```markdown
# 知识点名称

## 1. 知识点定义

## 2. 语法格式

## 3. 重点说明

## 4. Demo 样例

## 5. 典型例题（附带答案）

## 6. 易错点

## 7. 课后练习（附带答案）

## 8. 答题总结
```

这种结构的目的，是让每个知识点都既有理论解释，也有代码示例、练习题、易错点和复习总结，适合 Python 零基础学生系统学习。

---

## 为什么要生成这个 Skill

在本项目中，生成 Python 基础语法资料的过程比较复杂，涉及：

* 多个原始资料来源；
* 多个章节目录；
* 多个知识点文件；
* 统一的文档结构；
* Demo 代码要求；
* 例题和练习要求；
* 分章节生成；
* 最终验收和修复。

如果每次都重新写提示词，容易出现遗漏、格式不统一、质量不稳定等问题。

因此，在完成本项目后，将整个流程总结成 `python_learning_material_skill`，可以让后续类似任务更加稳定、高效、可复用。

---

## 后续使用方式

以后使用该 Skill 时，可以先让 AI 读取：

```text
python_learning_material_skill/SKILL.md
```

然后根据任务选择对应 prompt，例如：

```text
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/01_scan_materials.md 进行资料盘点，不要修改文件。
```

或者：

```text
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/03_complete_single_chapter.md，只完善第 3 章：流程控制。
```

再或者：

```text
请读取 python_learning_material_skill/SKILL.md。
现在使用 prompts/05_final_acceptance.md，对 10 个章节做最终验收。
```

通过这种方式，后续就可以把本次 Python 基础语法资料的生成经验，迁移到新的学习资料整理任务中。
