# 模型目录

源文件在 `src/`，导出图在 `img/`。目录、格式和拆页规则见 `.claude/skills/requirements-analysis/references/diagram-delivery.md`。

“含待定点”表示图已定稿，但图中标注的局部口径仍待确认；待定点见 `dialogue.md` 与 `STATUS.md`。

| 图题 | 类型 | 回答的问题 | 源文件 | 图文件 | 主要来源 | 状态 |
|---|---|---|---|---|---|---|
| 5E 学习智能体行为 | 行为地图 | 学生在不同页面、不同问题下智能体怎么表现；哪些能做、哪些拒答；数据和记忆边界是什么 | `src/agent-behavior-map.mmd` | `img/agent-behavior-map.svg` | REQ-AGENT-001～010、Q-132～144 | 已定稿·含待定点 |
| 五步引导状态 | 状态图 | 五步引导如何进入、每一步做什么、何时结束 | `src/agent-five-e-guide-state.mmd` | `img/agent-five-e-guide-state.svg` | REQ-AGENT-001、REQ-AGENT-003、Q-135；Q-134、Q-183 待回答 | 已定稿·含待定点 |
| 内容变更连锁反应 | 活动图 | 改名、新增、重新上传、删除内容，或修改成绩、知识点后，完成状态、诊断、总览、推荐计划和通知如何变化 | `src/course-content-change-cascade.mmd` | `img/course-content-change-cascade.svg` | REQ-COURSE-003/010/013/015、REQ-DIAG-002/004/007/008、REQ-RECO-004/005/008、REQ-NOTIF-001/002/003、Q-030、Q-102、D-013、D-014 | 已定稿 |
| 课程内容与知识点关系 | 领域类图 | 课程、章节、节点、练习、题目、知识点之间是什么关系 | `src/course-content-knowledge-relations.mmd` | `img/course-content-knowledge-relations.svg` | REQ-COURSE-001/002/003/006/014/015、REQ-DIAG-001/002/003、glossary | 已定稿 |
| 练习提交到推荐 | 时序图 | 一次练习提交后，成绩、学习事件、章节诊断、课程掌握总览、推荐计划和通知按什么顺序发生 | `src/course-submit-to-recommend.mmd` | `img/course-submit-to-recommend.svg` | REQ-COURSE-006/007、REQ-LOG-002、REQ-DIAG-004/007/008、REQ-RECO-001/004/005/006/008、REQ-NOTIF-002/003、S-056、D-014 | 已定稿 |
| 数字孪生采集数据清单 | 数据清单（Markdown 表） | 数字孪生每天同步哪些数据，每类已确认包含什么，哪些字段或口径待定 | `src/dt-data-inventory.md` | `img/dt-data-inventory.png` | REQ-DT-001、Q-147、Q-182、Q-101、Q-102、REQ-LOG-001～005、REQ-DIAG-004/005/007、REQ-PROF-001/002、REQ-RECO-002/003、REQ-AGENT-009 | 已定稿·含待定点 |
| 数字孪生输出结构 | 内容结构图 | 数字孪生输出哪些内容，章节预测、学习趋势、模拟对比分别包含什么 | `src/dt-output-structure.mmd` | `img/dt-output-structure.svg` | REQ-DT-002/003/004/006、Q-148/149/150/152/153/154/155/159 | 已定稿·含待定点 |
| 预测可用性与输出判定 | 决策表（Markdown 表） | 章节已完成、服务不可用、数据不足、部分知识点不足、数据足够时分别输出什么 | `src/dt-prediction-decision-table.md` | `img/dt-prediction-decision-table.png` | REQ-DT-002、REQ-DT-006、Q-148/149/152/153/154/157 | 已定稿·含待定点（Q-179 顺序） |
| 数字孪生同步与请求 | 活动图 | 数字孪生每天同步哪些数据；预测、趋势、模拟请求时用哪份数据；是否回写其他模块 | `src/dt-sync-and-request.mmd` | `img/dt-sync-and-request.svg` | REQ-DT-001～006、Q-147/155/156/157/182、D-015 | 已定稿 |
| 学习趋势判定 | 决策表（Markdown 表） | 可用指标数、改善项数、恶化项数如何合成改善、稳定、恶化或数据不足 | `src/dt-trend-decision-table.md` | `img/dt-trend-decision-table.png` | REQ-DT-003、Q-151、glossary 学习趋势 | 已定稿 |
| 学习结果与支持数据关系 | 领域类图 | 完成状态、练习提交、作答、学习事件、章节诊断、课程掌握总览、推荐计划、复习练习、画像和通知之间是什么关系 | `src/learning-result-relations.mmd` | `img/learning-result-relations.svg` | REQ-COURSE-005/007/008/009、REQ-DIAG-004/005/007/008、REQ-RECO-002/003/005/008、REQ-LOG-001/002/003/005、REQ-PROF-001、REQ-NOTIF-004、glossary | 已定稿 |
| 推荐计划状态 | 状态图 | 推荐计划从生成到完成经历哪些状态；接受、更新、未掌握知识点清空时如何迁移 | `src/recommendation-plan-state.mmd` | `img/recommendation-plan-state.svg` | REQ-RECO-001/002/004/005/007/008、glossary 推荐计划/计划项、S-055、S-056、D-013、D-014 | 已定稿 |
| 学生一次学习旅程 | 旅程图（Mermaid timeline） | 学生从登录到关闭平台经历哪些阶段，每个阶段做什么、看到什么反馈 | `src/student-journey.mmd` | `img/student-journey.svg` | personas 学生场景、REQ-COURSE/DIAG/RECO/PROF/AGENT/DT/NOTIF | 已定稿 |
| 学生画像内容 | 内容结构图 | 学生画像包含哪些展示内容、四个维度各有哪些指标、如何生成和展示 | `src/student-profile-content.mmd` | `img/student-profile-content.svg` | REQ-PROF-001～005、Q-084/086/089/090/095/100/182、D-006、D-015 | 已定稿·含待定点 |
| 学生用例 | 用例图（flowchart 近似） | 学生在这套平台上能做什么 | `src/student-use-cases.mmd` | `img/student-use-cases.svg` | REQ-COURSE/DIAG/RECO/PROF/AGENT/DT/NOTIF/ACCT、Q-021 | 已定稿 |
| 教师一次教学旅程 | 旅程图（Mermaid timeline） | 教师从登录到关闭平台经历哪些阶段，每个阶段做什么、看到什么反馈 | `src/teacher-journey.mmd` | `img/teacher-journey.svg` | personas 教师场景、REQ-COURSE/DIAG/RECO/PROF/INTV/DT | 已定稿 |
| 教师用例 | 用例图（flowchart 近似） | 教师在这套平台上能做什么 | `src/teacher-use-cases.mmd` | `img/teacher-use-cases.svg` | REQ-COURSE/DIAG/RECO/PROF/INTV/DT/ACCT、Q-021 | 已定稿 |
