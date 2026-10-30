# 需求一致性检查工具

只读工具：只读取 `docs/` 下的文件，打印检查结果，不修改任何内容。

## 用法

在仓库根目录运行：

```bash
python tools/requirements/reqtool.py check q
python tools/requirements/reqtool.py check dor
python tools/requirements/reqtool.py check dor REQ-xxx
python tools/requirements/reqtool.py check models
python tools/requirements/reqtool.py check refs
python tools/requirements/reqtool.py check coverage
python tools/requirements/reqtool.py check gate module 学习诊断
python tools/requirements/reqtool.py check gate handoff
python tools/requirements/reqtool.py q next
```

也可以显式指定仓库路径：

```bash
python tools/requirements/reqtool.py <repo> check q
```

需要 Python 3.8+，无第三方依赖。

## 命令

### `check q`

检查 Q 相关的机械一致性，输出 `INFO` 和 `FAIL`。

**FAIL（退出码 1）**

- Q 索引与 Q 表开放 Q 不一致（缺、多、重复）；
- Q 索引顺序不符合“冲突 → 模块 → Q 号”；
- Q/S 状态值非法；
- 关联列仍有“待建”，或指向不存在的 Q/REQ；
- STATUS 待决事项与开放 Q 不一致；
- STATUS 阶段与开放 Q 矛盾；
- STATUS 当前模块不是第一条开放 Q 的模块；
- 开放 Q 不在 `coverage-scan.md`，或对应模块总览没有“已问待答”；
- 必读文件缺失；
- NFR 编号非法或重复；
- backlog 缺负责人、依赖不存在、自依赖、依赖环；
- 仍引用旧文件名；
- Q 索引类别非法、模块不在 `vision.md` 范围、建议顺序重复。

**INFO（不算失败）**

- Q 表/索引数量、开放 Q 数量、待建数量；
- 覆盖扫描中“已问待答”的模块数；
- 模型待定点数量；
- 移交前置和模块门禁的当前状态及原因。

当前阶段有开放 Q 是正常状态，所以 `check q` 仍然退出 0；只有机械不一致才退出 1。

### `check dor [REQ]`

检查故事卡是否满足 DoR 的机械部分。默认只打印失败项和汇总；加 `--verbose` 打印每条 PASS。

**FAIL**

- REQ 不存在；
- 标题、故事、验收标准、优先级、负责人、依赖为空；
- 验收标准缺少“给定…则…”或 Given-When-Then 结构（启发式）；
- 优先级不在 Must/Should/Could/Won't；
- 负责人不在 `docs/team.md` 的简称里；
- 依赖不存在、自依赖、依赖环。

**INFO**

- 未检查：故事来源、关联 Q（backlog 没有这些列）。

示例：

```
$ python tools/requirements/reqtool.py check dor
FAIL REQ-ACCT-002: 验收标准缺少“给定…则…”；负责人为空
INFO 未检查：故事来源、关联 Q（backlog 无列）
RESULT: FAIL (1/75)
```

### `check models`

检查 `models/README.md` 与 `models/src/`、`models/img/` 的一致性。

**FAIL**

- 源文件或图文件不存在、扩展名不对；
- 状态含“含待定点”但没有关联开放 Q；
- 状态含待定点，但源文件没有“待定/待确认/未定”注释；
- `src/`、`img/` 有未登记的源或图；
- 同一图同时存在 `.svg` 和 `.png`，或同一源同时存在 `.mmd` 和 `.md`。

**INFO**

- 模型行数、含待定点数量。`--verbose` 打印每条 PASS。

### `check refs`

检查项目文档中的路径、P-ID 和旧文件名。

**FAIL**

- `docs/...` 路径不存在（`docs/requirements/context.md` 可选，跳过）；
- `research/<name>.md` 或 `src/`、`img/` 路径不存在；
- `P-ID` 不在 `docs/requirements/research/sources/INDEX.md`；
- skill 的 `references/...` 或 `tools/...` 路径不存在；
- 仍引用旧文件名（`00-vision`、`01-personas`、`02-backlog`、`03-nfr`、`07-dialogue`、`08-decisions`、`04-hypotheses`、`05-traceability`、`06-changes`）。

**INFO**

- 扫描文档数、P-ID 引用数、路径引用数。

### `check coverage`

检查每个模块的 27 项扫描、维度聚合和模块总览是否一致。

**FAIL**

- 模块缺扫描节或模块总览；
- 扫描项不是 27 项，或缺/多子提问；
- 扫描记录或聚合状态非法；
- 某维有开放 Q，但聚合不是“已问待答”；
- 某维没有开放 Q，但聚合是“已问待答”；
- 总览某维与聚合不一致；
- 扫描节的模块不在 `vision.md` 范围。

**INFO**

- 模块数量；`--verbose` 打印每条模块 PASS。

### `check gate module <模块|缩写>`

检查一个模块能否进入确认。

**FAIL**

- 模块不在 `vision.md` 范围；
- coverage-scan 缺模块总览，或六维有“未问”；
- 该模块 27 项扫描不完整，或聚合/总览不一致；
- 模块有开放 Q；
- 全局仍有“待建”关联列。

**INFO**

- 模块名/缩写、负责角色、六维状态、开放 Q 数量。

### `check gate handoff`

检查能否移交设计。只做机械前置检查，语义判断仍按 `handoff.md`。

**FAIL（阻断移交）**

- 开放 Q；
- 关联列仍有“待建”；
- 有“含待定点”模型；
- NFR 编号非法或重复；
- 有 REQ 未通过 DoR；
- 模块门禁：模块缺总览、六维有“未问”、有开放 Q 的模块；
- 覆盖扫描未通过。

**INFO**

- 当前阶段（移交触发还需“需求确认完成”或用户明确要求）；
- 待建数量、模型待定点数量、NFR 数量、DoR 结果、模块门禁结果。

当前有开放 Q 时会 `FAIL`，这是预期：它不是“检查当前状态”，而是“检查能否移交”。

### `q next`

按“确定冲突 → 可能冲突/无法判断 → 普通缺口；同层按模块顺序、再按 Q 号”计算下一问。

输出：`next`、`module`、`question`、`category`、`reason`。没有开放 Q 时输出 `none`，退出码 2。

## 退出码

| 码 | 含义 |
|---|---|
| 0 | 检查通过（所有 `check` 命令）或找到下一问（`q next`） |
| 1 | 发现机械不一致或存在阻断项（所有 `check` 命令） |
| 2 | 没有开放 Q（`q next`） |
| 64 | 命令用法错误 |

## 不检查的内容

- 这条 Q 该不该问、答案是否正确；
- 冲突是否真实、故事是否有价值；
- 验收标准是否可观察；
- 哪些问题是“设计阶段定”；
- 故事来源、故事关联 Q、NFR/S 的模块归属（当前数据模型没有这些列）。

这些仍由 AI 或人判断。工具只负责机械一致性。

## 与 skill 的关系

`requirements-analysis` skill 在会话开始、写入前、移交前提示运行 `check q`；需要选下一条 Q 时运行 `q next`。`FAIL` 项不得绕过；工具不可用时按 skill 手工检查。
