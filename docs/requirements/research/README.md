# 对标调研

每个平台一份 brief，命名 `<平台>.md`；模块综合 brief 命名 `<模块>.md`；背景/主题 brief 命名 `<主题>.md`；汇总矩阵 `comparison-matrix.md`。

预综合/工作稿命名 `<模块>-pre-synthesis.md`，不计入正式 brief；正式 brief 在边界确认后创建。

## 现有资料状态

- 模块综合 brief：`account.md`、`agent.md`、`course-content.md`、`diagnosis.md`、`digital-twin.md`、`intervention.md`、`learning-record.md`、`notification.md`、`profile.md`、`recommendation.md`，是正式对标调研 brief。用于生成 Q 和支撑 AI 草案，不作需求来源或覆盖依据。
- `5e.md` 是 5E 教学模式背景/主题 brief，不作为模块正式 brief；5E 学习智能体模块以 `agent.md` 为准。
- 分平台 brief（`canvas.md`、`moodle.md`、`open-edx.md`、`xapi.md`）、`comparison-matrix.md` 和 `learning-record-pre-synthesis.md` 是预分析/工作材料，不作为正式 brief 单独使用。
- 资料中的 Q/P/REQ 引用可能指向已删除的对话记录，只作线索。

Brief 固定六段：检索问题、来源清单、需求观察、设计线索、与本项目的差异、生成的 Q。

规则见 `.claude/skills/requirements-analysis/references/research-guide.md`。`P` 可以生成 Q，也可以支撑 AI 草案；草案需人确认，设计细节进 `docs/design-notes.md`。

快速调研不写正式 brief，输出 P 观察 + Q + 可选 AI 草案；草案标“AI 提议”，人确认后写入。
