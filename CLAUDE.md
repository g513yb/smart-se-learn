# CLAUDE.md

本文件是项目的常驻工作手册，每次会话自动载入。它只承载团队分工、流程入口、文档地图、文档约定和协作原则；领域事实与需求细节一律以 `docs/` 下的文档为准，本文件不复述。

## 1. 项目定位

智能软件工程学习平台，面向软件工程专业的师生，覆盖「学习—学习记录—学习诊断—学生画像—内容推荐—教师干预」主线，并包含 5E 学习智能体与学生数字孪生两个智能模块。

范围、目标与非目标见 `docs/requirements/00-vision.md`。

## 2. 用户与角色

- 学生
- 教师
- 管理员

角色的定义、目标与场景见 `docs/requirements/01-personas.md`。

## 3. 团队与分工

成员：课程组、智能组。

| 负责范围 | 负责人 |
|---|---|
| 教学业务层（六条主线） | 课程组 |
| 智能层与平台基础（5E 学习智能体、学生数字孪生、内容上传与管理） | 智能组 |

每条需求设一名负责人和一名评审人，交叉评审，不得自审。任一成员可确认任意需求，记录确认人和日期；确认不等于评审。

## 4. 开发方式

敏捷开发，按周迭代。需求何时算准备好、何时算完成，以及评审与变更的具体做法，见 requirements skill。

## 5. 文档地图

| 路径 | 用途 | 何时读 |
|---|---|---|
| `.claude/skills/requirements-analysis/SKILL.md` | 需求分析流程 | 执行需求流程时 |
| `docs/STATUS.md` | 当前阶段与待决事项 | 会话开始、不确定进度时 |
| `docs/requirements/00-vision.md` | 愿景、范围、目标与非目标 | 开始任何需求讨论前 |
| `docs/requirements/context.md` | 业务上下文（已确认的流程、角色、对象、规则） | 开始分析前、每次问答后 |
| `docs/requirements/01-personas.md` | 角色、目标、场景 | 讨论用户相关需求前 |
| `docs/requirements/02-backlog.md` | 需求故事池 | 新增、修改或领取需求前 |
| `docs/requirements/coverage.md` | 模块覆盖矩阵 | 模块首访、模块评审前 |
| `docs/requirements/03-nfr.md` | 非功能需求 | 涉及性能、安全、可用性时 |
| `docs/requirements/04-hypotheses.md` | 研究假设卡 | 涉及 5E 智能体、数字孪生或 AI 能力前 |
| `docs/requirements/05-traceability.md` | 需求追踪矩阵 | 改动需求或提交代码前 |
| `docs/requirements/06-changes.md` | 变更记录 | 修改已确认需求前 |
| `docs/requirements/07-questions.md` | 问答记录与待确认清单 | 写需求前、遇到任何缺口时 |
| `docs/requirements/glossary.md` | 术语表 | 需求讨论、命名、接口设计前 |
| `docs/requirements/models/` | 模型图源（Mermaid） | 需要出图或引用模型前 |
| `docs/requirements/research/` | 对标调研 brief | 进入新模块、需要参考时 |
| `docs/design-notes.md` | 设计线索，不进入需求 | 记录或查阅实现参考时 |

文档尚未建立时，按此结构创建。

## 6. 文档与建模约定

- 文件与目录使用小写 kebab-case；正文用中文。
- 编号：需求 `REQ-<模块缩写>-<三位序号>`，参考来源 `P-<三位序号>`，设计线索 `DSN-<三位序号>`；backlog、追踪矩阵、提交信息中使用同一编号。
- 图统一用 Mermaid 源码存放，一图一文件，文件名与图题一致。
- 文档和讨论中引用需求一律使用编号。

## 7. 协作工作原则

- 不臆造需求：没有来源的内容标记为待确认，不直接写成需求。
- 每条需求可溯源到明确来源（访谈、场景走查、既有文档或明确决策）。
- 修改已确认的需求或基线文档前先确认，再记录变更。
- 本文件不记录会过期的信息；进度与待决事项一律看 `docs/STATUS.md`。
