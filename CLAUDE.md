# CLAUDE.md

本仓库是「智能软件工程学习平台」的项目仓库，当前处于需求阶段，包含需求文档、模型图和需求分析 skill；后续加入设计与实现。

开发方式：敏捷开发，按周迭代。需求何时算准备好、何时算完成，以及确认与变更的具体做法，见 `requirements-analysis` skill。

## 1. 开工顺序

1. 读 `docs/STATUS.md`：当前阶段、当前模块、下一步、待决事项。可运行 `python tools/requirements/reqtool.py check all` 做机械检查。
2. 判断任务类型：
   - 需求（新建、修改、确认、建模、backlog、变更、移交）→ 先加载 `requirements-analysis` skill，按 skill 的流程走；本文件不替代 skill。skill 的 `SKILL.md` 末尾有“参考文件与阅读时机”表，按表读，不必一次读全部 reference。
   - 设计 → 由 `design-analysis` skill 承担（待建）；尚未建立时，按 `requirements-analysis` 的 `handoff.md` 输出移交包后停下，不自行开始设计。
   - 实现、测试 → 当前尚未纳入仓库；后续加入时在 CLAUDE.md 中更新入口。
3. 负责人和负责范围见 `docs/team.md`。
4. 不确定从哪继续、或看到的状态与 skill 给的下一步不一致：停下来问，不自行开始。

## 2. 文档地图

| 路径 | 用途 | 何时读 |
|---|---|---|
| `docs/STATUS.md` | 当前阶段、当前模块、下一步、待决事项 | 会话开始、不确定进度时 |
| `docs/team.md` | 成员与负责范围 | 分配负责人时 |
| `docs/requirements/vision.md` | 愿景、范围、目标与非目标 | 需求讨论前 |
| `docs/requirements/context.md` | 已确认的稳定业务事实 | 按需；缺失正常 |
| `docs/requirements/personas.md` | 角色、目标、场景 | 讨论用户相关需求前 |
| `docs/requirements/backlog.md` | 需求故事池 | 新增、修改或领取需求前 |
| `docs/requirements/nfr.md` | 非功能需求 | 涉及性能、安全、可用性时 |
| `docs/requirements/dialogue.md` | 用户原话 S 与缺口问题 Q | 写需求前、遇到缺口时 |
| `docs/requirements/decisions.md` | 决策 D | 冲突、基线变更、需要决策时 |
| `docs/requirements/glossary.md` | 术语表 | 需求讨论、命名前 |
| `docs/requirements/coverage-scan.md` | 模块覆盖扫描 | 模块首访、状态变化时 |
| `docs/requirements/models/` | 建模源与导出图，目录见其中的 `README.md` | 出图或引用模型前 |
| `docs/requirements/research/` | 对标调研 brief 与来源 | 进入新模块、需要参考时 |
| `docs/design-notes.md` | 设计线索 `DSN-`，不进入需求 | 记录或查阅设计参考时 |
| `.claude/skills/requirements-analysis/` | 需求分析流程 | 执行需求流程时 |
| `tools/requirements/` | 需求一致性检查工具（只读） | 会话开始、写入前、移交前 |

文档尚未建立时，按 skill 的“初始化”顺序创建；不预建空文件，不预填内容。

## 3. 编号与命名

- 需求 `REQ-<模块缩写>-<三位序号>`；原话 `S-`；缺口问题 `Q-`；决策 `D-`；参考来源 `P-`；非功能需求 `NFR-<三位序号>`；设计线索 `DSN-`。
- 文件和目录用小写 kebab-case；正文用中文。
- 图源用 Mermaid（表格用 Markdown），源在 `models/src/`，导出在 `models/img/`；一图一源、一图一格式，文件名与图题一致。
- 文档和讨论中引用需求一律用编号。

## 4. 写入与协作

- 每条需求设一名负责人，负责人见 `docs/team.md`。
- 每条需求可溯源到明确来源（`S`/`D`、已写入文件或人确认）；没有来源的内容标待确认或写入 Q，不写成需求。
- 需求内容、backlog、基线（`vision.md`、`personas.md`）的写入由人确认；记录层（S/Q/D 记录、Q 回答回写、`STATUS.md` 维护）由 AI 自动完成。
- 修改已确认的需求或基线前先确认；基线变更由人确认；管理/流程规则变更记录在文件本身，不写项目 D。
- 技术方案、算法、架构、库选型只写 `docs/design-notes.md`；需求 skill 不做设计，只移交。
- 需求文档只放标题、指针、表头和项目内容；流程、管理、确认规则只写本文件和 skill references。需求文档出现规则文字视为缺陷。
- 管理文件只写结构、字段、含义、规则和通用示例；项目概念、事实、需求和具体角色只写项目文件。示例必须通用，或明确标注“非本项目”。

## 5. 冲突与优先级

- 流程细节以 `requirements-analysis` skill 为准；仓库事实以 `docs/` 下的文档为准。
- 本文件与 skill 冲突、或文档之间冲突且无法判断时，停下来问，不自行选边。

## 6. 提交

- 提交信息用中文，沿用 `docs:`、`refactor:` 等前缀。
- 不提交 `docs/PPT/`、临时文件和本地产物。
- 推送前运行 `python tools/requirements/reqtool.py check refs`；CI 会在 push/PR 运行 `check all`。

本文件不记录会过期的信息；进度和待决事项一律看 `docs/STATUS.md`。
