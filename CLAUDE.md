# CLAUDE.md

本文件是项目的常驻工作手册，每次会话自动载入。它只承载流程入口、文档地图、文档约定和协作原则；团队名单与分工见 `docs/team.md`，领域事实与需求细节一律以 `docs/` 下的文档为准，本文件不复述。

## 1. 开发方式

敏捷开发，按周迭代。需求何时算准备好、何时算完成，以及确认与变更的具体做法，见 requirements skill。

## 2. 文档地图

| 路径 | 用途 | 何时读 |
|---|---|---|
| `.claude/skills/requirements-analysis/SKILL.md` | 需求分析流程 | 执行需求流程时 |
| `docs/team.md` | 团队成员与负责范围 | 需要分配负责人时 |
| `docs/STATUS.md` | 当前阶段与待决事项 | 会话开始、不确定进度时 |
| `docs/requirements/00-vision.md` | 愿景、范围、目标与非目标 | 开始任何需求讨论前 |
| `docs/requirements/context.md` | 业务上下文（其他文件不收录的已确认稳定事实） | 开始分析前、每次问答后 |
| `docs/requirements/01-personas.md` | 角色、目标、场景 | 讨论用户相关需求前 |
| `docs/requirements/02-backlog.md` | 需求故事池 | 新增、修改或领取需求前 |
| `docs/requirements/coverage-scan.md` | 模块六维扫描记录与覆盖总览 | 模块首访、模块状态变化时 |
| `docs/requirements/03-nfr.md` | 非功能需求 | 涉及性能、安全、可用性时 |
| `docs/requirements/07-dialogue.md` | 对话记录：用户原话 S 与缺口问题 Q | 写需求前、遇到任何缺口时 |
| `docs/requirements/08-decisions.md` | 决策记录（D） | 冲突、基线变更、需要决策时 |
| `docs/requirements/glossary.md` | 术语表 | 需求讨论、命名、接口设计前 |
| `docs/requirements/models/` | 模型图源与导出图 | 需要出图或引用模型前 |
| `docs/requirements/models/README.md` | 建模图目录（图题、类型、源、图、来源） | 查找、新增或修改图时 |
| `docs/requirements/research/` | 对标调研 brief | 进入新模块、需要参考时 |
| `docs/design-notes.md` | 设计线索，不进入需求 | 记录或查阅实现参考时 |

文档尚未建立时，按此结构创建。从零建立时，按 requirements skill 的“初始化”顺序执行；不预建空文件，不预填内容。

## 3. 文档与建模约定

- 文件与目录使用小写 kebab-case；正文用中文。
- 编号：需求 `REQ-<模块缩写>-<三位序号>`，用户原话 `S-<三位序号>`，缺口问题 `Q-<三位序号>`，决策 `D-<三位序号>`，参考来源 `P-<三位序号>`，设计线索 `DSN-<三位序号>`；backlog、提交信息中使用同一编号。
- 图源统一用 Mermaid（表格用 Markdown 表）存放，一图一源；源在 `docs/requirements/models/src/`，导出图在 `docs/requirements/models/img/`，同一图只保留一种图像格式；文件名与图题一致。目录见 `models/README.md`，输出与拆页规则见 skill 的 `diagram-delivery.md`。
- 文档和讨论中引用需求一律使用编号。

## 4. 协作工作原则

- 团队名单与负责范围见 `docs/team.md`；每条需求设一名负责人。
- AI 可以生成、起草和提议内容；最终写入文件前必须由人确认，有依据不等于可以写入。确认在对话中完成，不记录确认人/日期；无评审环节。
- 不臆造需求：没有来源的内容标记为待确认，不直接写成需求。
- 每条需求可溯源到明确来源（访谈、场景走查、既有文档或明确决策）。
- 修改已确认的需求或基线文档前先确认，再记录变更。
- 项目基线（`00-vision.md`、`01-personas.md`）的变更由人确认；具体记录方式见对应 skill 规则。本文件及 skill 的管理/流程规则变更记录在文件本身，不写项目 D。
- 需求文档只放标题、指针、表头和项目内容；流程、管理、确认规则只放本文件和 skill references。需求文档里出现规则文字，视为缺陷：移到 skill，不在原处新增。
- 管理文件（本文件、skill references）只写结构、字段、含义、规则和通用示例；项目概念、事实、需求和具体角色只写项目文件。示例必须通用，或明确标注“非本项目”。
- 本文件不记录会过期的信息；进度与待决事项一律看 `docs/STATUS.md`。
