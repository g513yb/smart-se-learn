# 文件模板

本文件只定义 `docs/` 下各文件的结构，不预填项目内容。字段无内容时写“待确认”或“无”。文件缺失时按本文件结构创建。各文件的定位、AI 填充步骤和判定规则见 `file-lifecycle.md`。

## 项目状态 `docs/STATUS.md`

```markdown
# 项目状态

- 当前阶段：
- 下一步：
- 待决事项：
  - 
```

## 团队与分工 `docs/team.md`

```markdown
# 团队与分工

成员：

| 负责范围 | 负责人 |
|---|---|
| | |
```

## 愿景 `docs/requirements/00-vision.md`

结构见 `vision-guide.md` 第 3 节。

## 角色 `docs/requirements/01-personas.md`

结构见 `persona-guide.md` 第 3 节。

## 业务上下文 `docs/requirements/context.md`

```markdown
# 业务上下文

| 事实 | 说明 |
|---|---|
| | |
```

## Backlog `docs/requirements/02-backlog.md`

```markdown
# Backlog

| ID | 标题 | 故事 | 验收标准 | 优先级 | 负责人 | 依赖 |
|---|---|---|---|---|---|---|
```

字段定义见 `story-card.md`。

## NFR `docs/requirements/03-nfr.md`

```markdown
# 非功能需求

| 类别 | 指标 | 场景与边界 |
|---|---|---|
```

字段与提问见 `nfr-checklist.md`。

## 变更记录 `docs/requirements/06-changes.md`

```markdown
# 变更记录

| CR-ID | 日期 | 类型 | 目标需求 | 变更前 | 变更后 | 原因 / 依据 | 影响范围 | 冲突检查 | 决策 | 状态 |
|---|---|---|---|---|---|---|---|---|---|---|
```

类型与状态见 `file-lifecycle.md`。

## 对话记录 `docs/requirements/07-dialogue.md`

结构见 `dialogue-log.md`。

## 决策记录 `docs/requirements/08-decisions.md`

结构见 `decision-log.md`。

## 覆盖矩阵 `docs/requirements/coverage.md`

```markdown
# 模块覆盖矩阵

| 模块 | 角色 | 旅程 | 对象 | 规则 | 横切 | 质量 | 对标调研 |
|---|---|---|---|---|---|---|---|
```

状态定义见 `coverage-scan.md` 第 7 节。

## 覆盖扫描 `docs/requirements/coverage-scan.md`

每个模块一节：

```markdown
## 模块：<名称>

- 扫描日期：
- 模块边界来源：
- 使用 brief：
- 扫描人：

### 输入清单

见 `coverage-scan.md` 第 2 节。

### 扫描记录

见 `coverage-scan.md` 第 9 节。

### 维度聚合

见 `coverage-scan.md` 第 7 节。

### 清单外建议

| 建议 | 依据 | 是否批准 |
|---|---|---|
| | | |

### 输出

- 新增 S（如有用户原话）：
- 新增 Q：
- 更新 `coverage.md`：
```

## 术语表 `docs/requirements/glossary.md`

```markdown
# 术语表

| 术语 | 定义 |
|---|---|
```

## 设计线索 `docs/design-notes.md`

```markdown
# 设计线索

| 编号 | 来源 | 观察到的做法 | 可能适用阶段 | 备注 |
|---|---|---|---|---|
```

## 模型目录 `docs/requirements/models/`

一图一文件，规则见 `modeling-guide.md`。

## 调研目录 `docs/requirements/research/`

命名、brief 六段和状态规则见 `research-guide.md`；预分析资料状态见该目录 `README.md`。
