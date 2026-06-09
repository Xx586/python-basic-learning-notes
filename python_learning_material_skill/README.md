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
