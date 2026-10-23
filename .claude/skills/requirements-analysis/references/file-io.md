# 文件读写规则

本文件规定需求分析各阶段的文件读取、写入、来源和写法。读取和写入按本表执行；表外写入先问用户。

## 总则

### 读取

- 只读当前阶段需要的文件；不凭记忆补。
- 缺失或为空先报告；不把空文件当已知。
- 读到的内容必须能引用 `S/Q/D/R/P/REQ`；没有引用不算已知。
- `P` 只帮助提问，不作答案。

### 写入

- 只写有来源的内容；需求来源只写 `S/D/R`。
- `Q` 是问题，不是来源；Q 的回答另记 `S`。
- 追加优先；覆盖前保留旧版本（git + 变更记录）。
- 模板字段不得留空；无内容写“无”或“待确认”。
- AI 不能替人做决定：`D`、评审结果、确认人、确认日期由人填写。
- 设计内容只进 `design-notes.md` 的 `DSN-`，不进需求。

## 阶段读写

| 阶段 | 读 | 写 | 来源 | 关键规则 |
|---|---|---|---|---|
| 会话开始 | `CLAUDE.md`、`STATUS.md`、`context.md`、`glossary.md`、当前模块 brief、`07-dialogue.md` | 模块选择 S（如已指定） | 用户原话 | 未指定模块只列清单，不开始 |
| 1.0 边界 | `00-vision.md`、`context.md`、`glossary.md`、`02-backlog.md`、`07-dialogue.md` | S（模块选择）、范围 Q 或引用已有 Q | S + 缺失文档 | 边界不清停止；不做 brief/扫描 |
| 1a brief | `platform-candidates.md`、`sources/INDEX.md`、模块 brief、`07-dialogue.md` | `research/<模块>.md`、Q、`DSN-` | P | 只用已批准/部分验证；六段 + 完整性检查 |
| 1b 扫描 | `coverage-scan.md`、`coverage.md`、`02-backlog.md`、`07-dialogue.md`、`context.md`、`glossary.md`、`03-nfr.md`、`00-vision.md`、模块 brief | `coverage-scan.md`、`coverage.md`、Q | 显式引用 / D-覆盖扫描 / P | 27 项；无引用即未覆盖；只出 Q |
| 1c 缺口 | S/Q、`02-backlog.md`、`context.md`、`glossary.md`、`03-nfr.md`、`00-vision.md`、`01-personas.md`、`story-card.md` | S、Q、`context.md`、`glossary.md` | 用户/S + 检查项 | 先记 S；无引用即缺口；不重复 Q |
| 成形 | S/Q、`story-card.md`、`conflict-check.md`、`02-backlog.md`、`03-nfr.md`、`00-vision.md`、`glossary.md`、`context.md`、`05-traceability.md`、`design-notes.md` | backlog 故事卡、冲突检查、Q、`DSN-` | S/D/R + 冲突证据 | 只重述不新增；DoR；冲突检查 |
| 排序 | `02-backlog.md`、`08-decisions.md` | 优先级、优先级依据、D | 人的 S/D | 人决定；AI 不决定 |
| 建模 | `modeling-guide.md` | `models/*.mmd` | 需求 / 上下文 | 一图一文件；按需 |
| 评审 | `02-backlog.md`、冲突检查、`review-checklist.md`、`05-traceability.md`、`03-nfr.md`、`glossary.md`、`context.md` | backlog 评审结果 / 日期 | 评审人 | 评审人 ≠ 负责人；五查 |
| 确认 | `02-backlog.md`、`05-traceability.md` | backlog 确认人 / 日期、状态、traceability | 人的确认 | AI 不能标已确认 |
| 交接 | `02-backlog.md`、`05-traceability.md` | traceability 交接 | 人的确认 | AC 可执行后移交 |
| 变更 | 目标需求、`06-changes.md`、`05-traceability.md`、`02-backlog.md`、`conflict-check.md`、`03-nfr.md`、`00-vision.md`、`glossary.md`、`context.md` | CR、backlog 状态 / 字段、traceability、D | S/D + 影响 / 冲突 | 前后、影响、决策；旧版本保留 |
| 冲突 | `conflict-check.md`、`02-backlog.md`、`03-nfr.md`、`00-vision.md`、`glossary.md`、`context.md`、`05-traceability.md` | 冲突记录、Q、CR、D | S/Q/REQ/P | 不选边；确定冲突停止 |
| NFR | `nfr-checklist.md`、`02-backlog.md` | `03-nfr.md`、Q | S/D/R | 无来源写 Q |
| 假设 | `hypothesis-card.md`、brief | `04-hypotheses.md`、Q | S/D/R/P | 指标 / 失败判据 |
| 知识回填 | S/Q | `context.md`、`glossary.md` | S | 只写已确认事实 |
| 状态 | `STATUS.md` | `STATUS.md` | 人的 D | 阶段 / 下一步变化时更新 |

## 文件明细

| 文件 | 读时机 / 内容 | 写时机 / 内容 | 来源 | 写法 |
|---|---|---|---|---|
| `CLAUDE.md` | 每次会话自动 | 基线变更时 | D | 修改前确认；记 `06-changes.md` |
| `STATUS.md` | 会话开始 | 阶段 / 下一步变化 | D | 更新条目 |
| `00-vision.md` | 会话开始、1.0、冲突 | 范围 / 目标 / 非目标确认后 | S/D/R | 更新章节；基线变更记 CR |
| `context.md` | 会话开始、1b、1c、冲突 | Q 确认后 | S | 追加 / 更新事实，标来源 |
| `01-personas.md` | 1c、冲突 | 角色确认后 | S/D/R | 更新角色表 |
| `02-backlog.md` | 会话开始、1b、1c、成形、冲突 | 故事卡、优先级、评审、确认、状态 | S/D/R | 追加 / 更新行；字段见模板 |
| `03-nfr.md` | 1b、冲突 | NFR 确认后 | S/D/R | 追加指标；无来源写 Q |
| `04-hypotheses.md` | 1b、成形 | 假设卡创建 | S/D/R/P | 追加卡片 |
| `05-traceability.md` | 冲突、变更、评审、交接 | 确认 / 设计 / 提交 / 测试 / 交接 | backlog / design / commits / tests | 追加 / 更新行 |
| `06-changes.md` | 变更、冲突 | 变更 / 冲突决策 | S/D | 追加 CR；前后 / 影响 / 决策 |
| `07-dialogue.md` | 会话开始、1.0、1b、1c、成形 | S / Q / 回答 | 用户 / AI | 追加；回答记 S |
| `08-decisions.md` | 冲突、排序、基线变更 | 人做决定时 | S/Q/REQ/R/P | 追加 D；AI 只记录 |
| `coverage.md` | 1b、会话开始 | 扫描后 | 扫描记录 | 更新六维 |
| `coverage-scan.md` | 1b | 扫描后 | 27 项判断 | 填表 / 聚合 |
| `glossary.md` | 会话开始、1b、1c | Q 确认后 | S | 更新术语 |
| `models/` | 建模 | 需要出图 | 需求 / 上下文 | Mermaid 一图一文件 |
| `research/<模块>.md` | 1a、1b | 1a brief | P | 六段 + 完整性检查 |
| `platform-candidates.md`、`sources/INDEX.md` | 1a | 来源验证 / 新增 | P | 更新状态 / 索引 |
| `design-notes.md` | 成形、冲突 | 发现设计线索 | P/Q | 追加 `DSN-` |

## 状态词表

- 需求 / 候选：候选 / 已确认 / 开发中 / 已验收 / 已废弃 / 已拒绝 / 变更中
- CR：提议 / 已批准 / 已执行 / 已拒绝 / 已关闭
- D：已决定 / 已废弃
- S：已记录 / 已废弃
- Q：待回答 / 已确认 / 已废弃

## 评审、确认、决定

- 评审结果写 `02-backlog.md` 的评审结果 / 评审日期：通过 / 退回 / 待评审 + 不通过项摘要。
- 确认人 / 确认日期写 `02-backlog.md`；AI 不能填。
- 决定写 `08-decisions.md` 的 D 表；决策人必须是姓名。
- 优先级依据写 `02-backlog.md` 的“优先级依据”，引用 D/S/Q。
- 变更决策写 `06-changes.md` 的“决策”，引用 D。

## 剩余待补

- `STATUS.md` 的更新负责人没有规定，目前只有“阶段 / 下一步变化时”规则。
- 基线变更的“两人一致同意”规则尚未写入 `CLAUDE.md`，需要用户确认。
- NFR 和假设卡只有来源规则，写入确认流程仍较简。
