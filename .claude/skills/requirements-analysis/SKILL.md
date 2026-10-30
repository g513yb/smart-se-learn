---
name: requirements-analysis
description: Use when creating, modifying, confirming, or handing off requirements — 新建需求、修改需求、确认需求、编写验收标准、讨论 backlog、处理需求来源或变更时使用。
---

# 需求分析

## 概述

把原始信息变成可开发、可验收、可追溯的需求条目。核心原则：**只记录有来源的内容；没有来源的，变成问题，不变成需求。**

## 边界

- 在内：采集、故事卡、验收标准、优先级、建模、确认、变更记录
- 在外：设计、实现、测试执行、用户签收；设计只移交，不执行

## 硬规则

1. **来源与问题标签**：最终写入的需求必须有明确依据：`S-`/`D-`、已写入文件，或 AI 提议经人确认。`Q-` 不是来源；`P-` 不是最终来源，引用 P 的最终需求必须另有 S/D、已写入文件或人确认；推断不得进入“已确认”。S/D/Q/P 的定义与收录标准见 `references/dialogue-log.md`。依据写入记录；对话层按 `references/conversation-style.md` 说明依据；文件内容不标来源。
2. **先提问后动笔**：成形前先在内部列缺口；对话层的提问节奏见 `references/conversation-style.md`。缺口未确认，可以写候选草稿，但不得写成已确认需求。
3. **未知入清单**：不确定项写入 `docs/requirements/dialogue.md` 的 Q 表，编号并写清依据，不留在正文里当假设。
4. **示例保护**：出现“比如 / 例如 / 类似”时，先确认是举例还是真实需求；举例不得直接升级为需求。
5. **禁止越界**：AI 可以提出角色、字段、业务规则、非功能指标的候选，但必须标为“AI 提议”，经人确认后才能写入。
6. **生成与确认**：AI 可以生成、起草、归纳和提议内容；有 `S/D` 或项目文件依据的内容优先使用。需求内容、backlog、基线（`vision.md`、`personas.md`）写入前，必须把最终内容交人确认；有依据不等于可以写入。记录层（S/Q/D 的记录、Q 回答回写、`STATUS.md` 维护）由 AI 自动完成，不需要逐条确认，不在对话中说明。S/Q 的收录、角色/团队/状态输入的落点见 `references/dialogue-log.md`。不记录确认人/日期；无评审环节。
7. **设计隔离**：需求只写“做什么、为什么”；技术方案、算法、架构、库选型写入 `docs/design-notes.md`（`DSN-`），不进入需求文档。
8. **主动发现**：AI 可以主动提出需求候选；基于 `P` 的候选必须关联 Q；AI 生成的候选必须标为“AI 提议”，写入前经人确认。AI 准备提出遗漏内容但不确定时，可先做快速调研：查 1～2 个已批准来源，输出 P 观察 + Q + 可选 AI 草案；草案标“AI 提议”，人确认后写入；不写正式 brief。没有依据的可以作为开放问题或候选，但不得写成已确认需求。
9. **整理不等于补全**：把用户原话整理成故事卡时，只重述、拆分、归一化用语；原话中没有的角色、字段、规则、指标不得直接写成已确认内容。AI 可以提出补充建议，标为“AI 提议”，写入前由人确认；无法确认的写 Q。
10. **知识回填**：Q 被回答后，把回答写入 Q 的回答列；回答补充新内容时才另记 S；稳定业务事实写入 `context.md`，术语写入 `glossary.md`；回答不得只停留在问答记录里。
11. **冲突检查必做**：新增需求、变更需求、转为“已确认”前，按 `references/conflict-check.md` 检查并记录结论：确定冲突记 `D`，可能冲突或无法判断写入 `Q` 的依据，无冲突只在对话中说明；不得把“未发现”写成“没有冲突”。
12. **基线变更由人确认**：项目基线（愿景、范围、非目标、角色）的修改，由人确认；具体记录方式见 `references/vision-guide.md` 和 `references/persona-guide.md`；AI 不得自行修改。`CLAUDE.md` 和 skill 的管理/流程规则变更记录在文件本身，不写项目 D。
13. **文档边界**：需求文档只放标题、指针、表头和项目内容；流程、管理、确认规则只放 `CLAUDE.md` 和 skill references。需求文档里出现规则文字，视为缺陷：移到 skill，不在原处新增。
14. **管理文件边界**：管理文件只写结构、字段、含义、规则和通用示例；项目概念、事实、需求和具体角色只写项目文件。示例必须通用，或明确标注“非本项目”。
15. **S 与 Q**：S/Q 的边界、关联列回填、同一需求多条 S/Q 的处理、S 矛盾处理见 `references/dialogue-log.md`；写入前检查关联 Q 是否全部“已确认/已废弃”。

本文件中所有要求“标明依据”“标为 AI 提议”“输出能确认的/需要问的/不能写的”的地方，对话层按 `references/conversation-style.md` 执行；记录层保留原有来源和编号规则。对话层不展示记录动作或记录位置（记 S、不记 S、写入某文件、补进某节等）；用户问起时再说明。

违反字面规则即违反规则本意。

## 红旗：出现即停止

- “为了完整，先合理补全”
- “这是行业常见做法”
- “用户应该会需要”
- “先假设，后面再确认”
- “写细一点更专业”
- “两句话就能推出这些需求”
- “把推断写进‘以便’从句”
- “在验收标准的前置条件里补假设”
- “系统采用 / 通过算法 / 使用某框架”
- “对标平台这么做，所以我们也这么做”
- “我觉得应该有，但说不出依据”

处理方式：把内容标为“AI 提议”或改写成 Q；写入前必须由人确认，不得写成已确认需求。

## 会话开始

读 `STATUS.md`、`dialogue.md` 的待答 Q 索引和相关 Q、`vision.md` 的范围/模块顺序；`coverage-scan.md` 只读模块覆盖总览。按当前 Q 再读相关 `REQ`/`NFR`、对应模块的 `coverage-scan.md` 节、相关模型和模块 brief。`team.md` 只在分配负责人时读；`context.md`、`glossary.md`、`personas.md`、`decisions.md` 按需读。用 3～5 行自然语言复述当前理解，不播报流程步骤。

- 必读基础文件（`STATUS.md`、`vision.md`、`personas.md`、`dialogue.md`）缺失时：按 `references/file-lifecycle.md` 的“初始化顺序”建立，不凭记忆补，不跳到模块选择。`context.md`、`glossary.md` 和模块 brief 缺失是正常状态，不触发初始化。
- 核对：`dialogue.md` 中状态为“待回答/部分回答”的 Q 与 `STATUS.md` 的待决事项不一致时，以 `dialogue.md` 为准并更新 `STATUS.md`。
- 有多个待答 Q 时，按 `references/dialogue-log.md` 的处理顺序；对话层按 `references/conversation-style.md` 一次只问一个。
- 未指定模块：列出 `vision.md` 范围节中明确列出的模块/能力；没有明确列出则先补范围 Q，不自行归纳。参考 `STATUS.md` 的下一步，请用户选择；不得自行开始。
- 已指定模块：把模块选择写入 `STATUS.md` 和 `glossary.md`，不记 `S`，进入边界确认。
- 多模块待决或模块已有分析记录：不重选模块、不重做边界确认或模块首访；按 `references/dialogue-log.md` 的 Q 顺序逐条处理，当前模块写当前 Q 所属模块，其余模块留在待决事项。

## 信息充足性判断

不做整体“信息够了”的判断，按关卡逐项判断：

| 关卡 | 判断什么 | 不充足时 |
|---|---|---|
| 会话开始 | 是否指定模块 | 列清单，请用户选择 |
| 边界确认 | 模块边界是否明确 | 记 S，引用或生成范围 Q，停止 |
| 对标调研 | 本模块 brief 或快速调研是否存在 | 不做 P 驱动的主动候选 |
| 模块首访 | 27 个子提问是否各有显式引用 | 无引用即未覆盖，生成 Q |
| 缺口提问 | 四问和故事卡字段是否各有显式引用 | 无引用即缺口，生成 Q |
| 成形 | DoR 是否通过 | 留在候选 |
| 确认 | 人是否确认最终内容 | 保持候选 |

每一关只认显式引用；没有引用就是缺口。模板只规定结构和可写内容，不预填答案；“待确认”是合法状态。

各文件的定位、结构、AI 填充步骤、判定规则和阶段读写见 `references/file-lifecycle.md`。

## 会话结束

如阶段、下一步、模块状态或待决事项发生变化，AI 按阶段判定表直接更新 `STATUS.md`；不需要人确认，不在对话中说明；不写项目 D；不记录确认人/日期；不改需求。

## 六步流程

1. **采集**：
   - **边界确认**：从 `vision.md`、`context.md`、`glossary.md`、`backlog.md` 确认模块边界。边界明确 = 范围明确列出本期包含的模块/能力，且明确不包含什么；只有模块名不算明确。不明确时，记 S（用户选择的模块），先查 `dialogue.md` 是否已有范围 Q；有则引用原 Q，没有则生成一个范围 Q。无论哪种都停止；不做 brief、不做 27 项扫描、不生成功能问题。明确后进入对标调研。如果 `vision.md` 尚未建立，先按 `references/vision-guide.md` 初次建立，再判断模块边界。模块缩写由用户在边界确认时指定，记入 `glossary.md`；未指定则问，不自行缩写。
   - **对标调研**（边界明确后）：按 `references/research-guide.md` 选 1～2 个平台，产出 brief；brief 是主动提问的依据，只提取用户可见行为，设计细节进 `docs/design-notes.md`
   - **模块首访**：按 `references/coverage-scan.md` 的 27 个子提问逐项判断，产出 `docs/requirements/coverage-scan.md` 记录并更新其中的模块覆盖总览；扫描只产出问题，不产出需求
   - **缺口提问**：按 `references/gap-check.md` 对当前单位逐项检查；原话先记 S，只对“未覆盖 / 部分覆盖 / 无法判断 / 缺依据”生成 Q，进 `dialogue.md`；已有待答 Q 不重复；生成 Q 后同步更新 `coverage-scan.md` 对应模块的维度聚合和总览。角色相关分析前，如果 `personas.md` 尚未建立，先按 `references/persona-guide.md` 初次建立
   - **NFR**：与 backlog 并行；模块边界明确后，模块首访的质量维度或用户提出质量要求时即可进入 NFR；不等待 backlog 完成；写 NFR 前检查相关 backlog 故事
   - 文档缺失或为空时先报告，不凭记忆补全
2. **成形**：按 `references/extraction-guide.md` 提取（含诊断三栏、两个来源）；缺口用 `references/elicitation-playbook.md` 的成形四问；用故事卡（`references/story-card.md`）；先过冲突检查（`references/conflict-check.md`）并记录结论；过 DoR；写 Given-When-Then；写入故事卡后，回填相关 Q 的关联需求（`REQ-xxx`）和 S 的关联列，未回填不算成形完成；对话层按 `references/conversation-style.md` 说明依据，文件内容不标来源。
3. **排序**：MoSCoW 或价值-成本；AI 可给建议，建议必须标“建议”；优先级由人决定；backlog 不记录依据或 D。
4. **建模**：只在文字说不清流程、状态、规则、交互或边界时画；查 `references/modeling-guide.md` 选最小图型。每个图元素必须有 `S/D/REQ` 来源；未回答的 Q、P、推断不作来源；设计进 `DSN-`。源保存到 `models/src/<模块>-<主题>.mmd`（表格为 `.md`），导出到 `models/img/`，更新 `models/README.md`；文件头写问题、来源；人确认后写入。格式与拆页规则见 `references/diagram-delivery.md`。
5. **确认**：AI 提交最终内容、验收标准和依据（有/无来源、哪些是 AI 生成）；人确认后写入；无评审环节；标准可执行、无歧义后，按 `references/handoff.md` 做移交检查并输出移交包；人确认后更新 `STATUS.md`，需求阶段结束。
6. **变更**：冲突检查 → 影响分析 → 更新目标文件；冲突处理见 `references/conflict-check.md`。

## 移交设计

需求确认完成后，不直接开始设计。按 `references/handoff.md` 检查前置条件并输出移交包：REQ、NFR、需求模型、DSN、开放问题、设计入口。移交包经人确认后，`STATUS.md` 改为“已移交设计”。设计由独立的 `design-analysis` skill 承担；本 skill 只移交，不执行设计。

## 对话循环

1. 用户用自然语言描述需求，允许不符合故事卡格式。
1.5. AI 做写入前变更检查：新陈述与已确认条目不一致时，先展示两边原文并请用户选择，不直接写文件；细则见 `vision-guide.md` 第 6 节和 `file-lifecycle.md` 的写入规则。
1.6. **持续检查**：每次用户实质性陈述后，AI 在后台做两项检查：冲突检查；事实候选提取。事实候选先记为对应的 `S` 原句，分类并标“AI 提议”；不打断当前问题，除非候选直接影响当前结论。同一需求的多条 S/Q 按关联列汇总；写入前检查关联 Q 状态。发现 S 前后矛盾时暂停并先处理；矛盾未解决前不依赖该 S。到话题结束或写文件前，汇总候选请人确认；确认后的稳定事实写入 `context.md`，其他送对应文件。
2. AI 按 `gap-check.md` 在内部诊断缺口；对话层只输出当前必要的确认、问题或未定项，不逐栏展示；提问节奏见 `conversation-style.md`。
3. AI 基于本模块 brief 主动补充遗漏，必须带 `P` 依据。
4. 用户用自己的话回答 Q → 记入 Q 的回答列；回答本身补充了新内容时才另记 S-xxx；人采用 AI 草案 → 不记 S，直接写入目标文件。人不回答时，AI 按规则提出草案和依据，人确认后写入；未确认不写入。
5. AI 把用户原话整理成故事卡：只重述、拆分、归一化用语，不新增内容。
6. 人确认最终内容；AI 写入，并回填相关 Q/S 的关联列。
7. 按 `references/dialogue-log.md` 的处理顺序进入下一个问题；提问节奏见 `conversation-style.md`。

一次只处理一个模块或一个问题，不一次性生成整份需求文档。

## 写入与更新

AI 只写人确认后的需求内容；`docs/STATUS.md` 例外：AI 按阶段判定表自行维护。更新故事前先确认。需求文件不设状态字段，不记录评审/确认/D；决策记录用 `decisions.md` 的状态列（已决定/已废弃）。

## 门禁

**DoR / DoD**：见 `references/file-lifecycle.md` 的 `backlog.md` 节。
**模块门禁**：六维无“未问”；覆盖扫描 27 项完整；S/Q 关联列无“待建”；该模块 `dialogue.md` 中无“待回答/部分回答”的 Q。可用 `tools/requirements/reqtool.py check gate module <模块>` 机械检查。

## 工具

仓库提供只读检查工具 `tools/requirements/reqtool.py`。会话开始可运行 `check all`（q/dor/models/refs/coverage）；写入前运行 `check q`；写故事卡前运行 `check dor [REQ]`；建模后运行 `check models`；推送前运行 `check refs`；模块首访后运行 `check coverage`；模块确认前运行 `check gate module <模块>`；移交前运行 `check gate handoff`；需要选下一条 Q 时运行 `q next`。`FAIL` 项按输出处理，不得绕过；`INFO` 是当前阶段状态。工具不可用时按本 skill 手工检查。命令与退出码见 `tools/requirements/README.md`。

## 参考文件与阅读时机

每次会话先读 `SKILL.md`。其余文件按当前动作读，不必全读。

| 时机 | 必读 | 用途 |
|---|---|---|
| 初始化前 | `file-lifecycle.md` 的“初始化顺序” | 从零建立的结构、团队、状态和角色 |
| 第一次回复前 | `conversation-style.md` | 对话层：一次一问、不展示编号和流程 |
| 记录 S/Q 前 | `dialogue-log.md` | S/Q 表结构、收录标准、关联列 |
| 处理待答 Q 前 | `dialogue.md` 的待答 Q 索引与 Q、相关 `REQ`/`NFR`、对应模块的 `coverage-scan.md` 节、相关模型与模块 brief；必要时 `nfr-checklist.md`、`elicitation-playbook.md` | 判断答案、影响和缺口 |
| 处理 Q 涉及模型时 | `models/README.md` + 对应 `models/src/` 文件 | 确认待定点、图元素来源 |
| 写愿景或角色基线前 | `vision-guide.md`、`persona-guide.md` | 六节/五节结构、初次建立与变更 |
| 写决策前 | `decision-log.md` | D 的字段和记录规则 |
| 模块边界确认后、对标调研前 | `research-guide.md` | brief 六段、来源等级、停止条件 |
| 模块首访前 | `coverage-scan.md`、`elicitation-playbook.md` | 27 项扫描、六维提问 |
| 缺口提问前 | `gap-check.md` | 缺口定义、检查项、Q 模板 |
| 写故事卡前 | `story-card.md`、`extraction-guide.md`、`conflict-check.md` | 字段、提取规则、冲突检查 |
| 写 NFR 前 | `nfr-checklist.md` | 八类问题和指标写法 |
| 建模前 | `modeling-guide.md`、`diagram-delivery.md` | 选图、图源与导出规则 |
| 新建或更新文件前 | `file-templates.md`、`file-lifecycle.md` | 文件结构、建立时机、读写规则 |
| 移交设计前 | `handoff.md` | 前置检查、移交包 |
| 运行机械检查前 | `tools/requirements/README.md` | 命令、输出、退出码 |
| 拿不准当前阶段 | `file-lifecycle.md` 的“阶段判定表”和“backlog.md 的 DoR 可执行检查” | 阶段、下一步、待决事项、DoR |

最小必读集：`SKILL.md` + `conversation-style.md` + `file-lifecycle.md` 的“阶段判定表”和 `backlog.md` 的 DoR + 当前阶段对应的文件。当前阶段为“待决事项处理中”时，至少读 `STATUS.md`、`dialogue.md` 的待答 Q 索引和相关 Q、`vision.md` 的范围/模块顺序、对应模块的 `coverage-scan.md` 节。其余按需。
