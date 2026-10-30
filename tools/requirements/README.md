# 需求一致性检查工具

只读工具：只读取 `docs/` 下的文件，打印检查结果，不修改任何内容。

## 用法

在仓库根目录运行：

```bash
python tools/requirements/reqtool.py check q
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

### `q next`

按“确定冲突 → 可能冲突/无法判断 → 普通缺口；同层按模块顺序、再按 Q 号”计算下一问。

输出：`next`、`module`、`question`、`category`、`reason`。没有开放 Q 时输出 `none`，退出码 2。

## 退出码

| 码 | 含义 |
|---|---|
| 0 | 检查通过（`check q`）或找到下一问（`q next`） |
| 1 | 发现机械不一致（`check q`） |
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
