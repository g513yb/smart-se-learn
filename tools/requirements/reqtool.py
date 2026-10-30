import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

OPEN = {"待回答", "部分回答"}
VALID_Q = {"待回答", "部分回答", "已确认", "已废弃"}
VALID_S = {"已记录", "已废弃"}
OLD_NAMES = (
    "00-vision", "01-personas", "02-backlog", "03-nfr", "07-dialogue", "08-decisions",
    "04-hypotheses", "05-traceability", "06-changes",
)
CAT_RANK = {"确定冲突": 0, "可能冲突": 1, "无法判断": 1, "普通": 2}


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_dialogue(base):
    text = read(os.path.join(base, "docs/requirements/dialogue.md"))
    section = ""
    qindex, qrows, srows = [], [], []
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if line.startswith("| Q-"):
            c = cells(line)
            if section.startswith("待答 Q 索引") and len(c) >= 5:
                qindex.append({"id": c[0], "module": c[1], "summary": c[2], "category": c[3], "order": c[4]})
            elif section.startswith("缺口问题") and len(c) >= 6:
                qrows.append({"id": c[0], "question": c[1], "basis": c[2], "status": c[3], "answer": c[4], "link": c[5]})
        elif line.startswith("| S-"):
            c = cells(line)
            if section.startswith("用户原话") and len(c) >= 4:
                srows.append({"id": c[0], "text": c[1], "status": c[2], "link": c[3]})
    return text, qindex, qrows, srows


def parse_status(base):
    text = read(os.path.join(base, "docs/STATUS.md"))
    pending, active = [], False
    stage, module = "", ""
    for line in text.splitlines():
        if line.startswith("- 当前阶段："):
            stage = line.split("：", 1)[1].strip()
        elif line.startswith("- 当前模块："):
            module = line.split("：", 1)[1].strip()
        elif line.startswith("- 待决事项"):
            active = True
        elif active and line.lstrip().startswith("- "):
            pending.extend(re.findall(r"Q-\d{3}", line))
        elif active and line.startswith("## "):
            break
    return text, stage, module, pending


def parse_vision_modules(base):
    text = read(os.path.join(base, "docs/requirements/vision.md"))
    line = next((l for l in text.splitlines() if "包含：" in l), "")
    part = line.split("包含：", 1)[1] if "包含：" in line else ""
    modules = []
    for name in part.split("、"):
        name = re.sub(r"（.*?）", "", name).strip().rstrip("。")
        if name:
            modules.append(name)
    return text, modules


def parse_coverage(base):
    text = read(os.path.join(base, "docs/requirements/coverage-scan.md"))
    in_overview, rows = False, {}
    for line in text.splitlines():
        if line.startswith("## 模块覆盖总览"):
            in_overview = True
            continue
        if in_overview and line.startswith("## "):
            break
        if in_overview and line.startswith("| ") and not line.startswith("|---"):
            c = cells(line)
            if len(c) >= 8 and c[0] != "模块":
                rows[c[0]] = c[1:7]
    return text, rows


def parse_models(base):
    path = os.path.join(base, "docs/requirements/models/README.md")
    text = read(path)
    pending = []
    for line in text.splitlines():
        if line.startswith("| ") and "含待定点" in line:
            c = cells(line)
            pending.append(c[0] if c else line)
    return text, pending


def parse_nfr(base):
    text = read(os.path.join(base, "docs/requirements/nfr.md"))
    rows = []
    for line in text.splitlines():
        if line.startswith("| NFR-"):
            c = cells(line)
            rows.append(c[0])
    return text, rows


def parse_backlog(base):
    text = read(os.path.join(base, "docs/requirements/backlog.md"))
    rows = []
    for line in text.splitlines():
        if line.startswith("| REQ-"):
            c = cells(line)
            if len(c) >= 7:
                rows.append({
                    "id": c[0], "title": c[1], "story": c[2],
                    "acceptance": c[3], "priority": c[4],
                    "owner": c[5], "deps": c[6],
                })
    return text, rows


def parse_team_roles(base):
    text = read(os.path.join(base, "docs/team.md"))
    roles = set()
    for line in text.splitlines():
        if line.startswith("| ") and not line.startswith("|---"):
            c = cells(line)
            if len(c) >= 3 and c[0] not in ("角色",):
                roles.add(c[1])
    return roles


def find_cycles(graph):
    visiting, done, cycles = set(), set(), []

    def dfs(node, stack):
        if node in visiting:
            cycles.append(stack[stack.index(node):] + [node])
            return
        if node in done:
            return
        visiting.add(node)
        for nxt in graph.get(node, []):
            dfs(nxt, stack + [nxt])
        visiting.remove(node)
        done.add(node)

    for node in graph:
        dfs(node, [node])
    return cycles


def order_open(open_rows, module_order):
    def key(row):
        rank = CAT_RANK.get(row.get("category", "普通"), 2)
        modules = [m.strip() for m in row.get("module", "").split("、")]
        mi = min((module_order.index(m) for m in modules if m in module_order), default=len(module_order))
        num = int(row["id"].split("-")[1])
        return (rank, mi, num)

    return sorted(open_rows, key=key)


def check_q(base):
    dialogue_text, qindex, qrows, srows = parse_dialogue(base)
    status_text, stage, current_module, status_pending = parse_status(base)
    vision_text, module_order = parse_vision_modules(base)
    coverage_text, coverage_rows = parse_coverage(base)
    models_text, pending_models = parse_models(base)
    nfr_text, nfr_ids = parse_nfr(base)
    backlog_text, backlog_rows = parse_backlog(base)

    issues, infos = [], []
    qmap = {q["id"]: q for q in qrows}
    if len(qrows) != len(qmap):
        issues.append("Q 表编号重复")
    if len(srows) != len({s["id"] for s in srows}):
        issues.append("S 表编号重复")
    open_rows = [q for q in qrows if q["status"] in OPEN]
    open_ids = {q["id"] for q in open_rows}
    idx_ids = [x["id"] for x in qindex]
    req_ids = {r["id"] for r in backlog_rows}

    if len(idx_ids) != len(set(idx_ids)):
        issues.append("Q 索引有重复编号")
    missing = sorted(open_ids - set(idx_ids))
    extra = sorted(set(idx_ids) - open_ids)
    if missing:
        issues.append(f"Q 索引缺少开放 Q：{', '.join(missing)}")
    if extra:
        issues.append(f"Q 索引含非开放 Q：{', '.join(extra)}")

    bad_status = [q["id"] for q in qrows if q["status"] not in VALID_Q]
    if bad_status:
        issues.append(f"Q 状态非法：{', '.join(bad_status)}")
    bad_s = [s["id"] for s in srows if s["status"] not in VALID_S]
    if bad_s:
        issues.append(f"S 状态非法：{', '.join(bad_s)}")

    wait_build = [x["id"] for x in srows + qrows if "待建" in x["link"]]
    if wait_build:
        issues.append(f"关联列仍为“待建”：{', '.join(wait_build)}")

    for x in srows + qrows:
        for rid in re.findall(r"REQ-[A-Z]+-\d{3}", x["link"]):
            if rid not in req_ids:
                issues.append(f"{x['id']} 关联了不存在的 {rid}")
        for qid in re.findall(r"Q-\d{3}", x["link"]):
            if qid not in qmap:
                issues.append(f"{x['id']} 关联了不存在的 {qid}")

    if set(status_pending) != open_ids:
        only_status = sorted(set(status_pending) - open_ids)
        only_q = sorted(open_ids - set(status_pending))
        if only_status:
            issues.append(f"STATUS 多列了：{', '.join(only_status)}")
        if only_q:
            issues.append(f"STATUS 漏列了：{', '.join(only_q)}")

    if stage == "待决事项处理中" and not open_rows:
        issues.append("STATUS 阶段为“待决事项处理中”，但没有开放 Q")
    if stage in ("需求确认完成", "已移交设计") and open_rows:
        issues.append(f"STATUS 阶段为“{stage}”，但仍有 {len(open_rows)} 条开放 Q")

    idxmap = {x["id"]: x for x in qindex}
    ordered = order_open([
        dict(q, module=idxmap.get(q["id"], {}).get("module", ""), category=idxmap.get(q["id"], {}).get("category", "普通"))
        for q in open_rows
    ], module_order) if open_rows else []
    if qindex and open_rows:
        expected = [q["id"] for q in ordered]
        if expected != idx_ids:
            issues.append(f"Q 索引顺序与规则不一致：应为 {', '.join(expected)}")
    if open_rows:
        first = ordered[0]
        mods = [m.strip() for m in idxmap.get(first["id"], {}).get("module", "").split("、") if m.strip()]
        if current_module in ("", "无", "多个"):
            issues.append(f"STATUS 当前模块应写第一条开放 Q 的模块，当前为“{current_module or '空'}”")
        elif mods and current_module not in mods:
            issues.append(f"STATUS 当前模块“{current_module}”不在第一条开放 Q 的模块 {mods} 中")

    for x in qindex:
        if x["category"] not in CAT_RANK:
            issues.append(f"{x['id']} 类别非法：{x['category']}")
        for m in [m.strip() for m in x["module"].split("、") if m.strip()]:
            if m not in module_order:
                issues.append(f"{x['id']} 模块不在 vision 范围：{m}")
    orders = [x["order"] for x in qindex]
    if len(orders) != len(set(orders)):
        issues.append("Q 索引建议顺序有重复")

    for q in open_rows:
        modules = [m.strip() for m in next((x["module"] for x in qindex if x["id"] == q["id"]), "").split("、") if m.strip()]
        if q["id"] not in coverage_text:
            issues.append(f"{q['id']} 未出现在 coverage-scan")
        for m in modules:
            if m in coverage_rows and "已问待答" not in coverage_rows[m]:
                issues.append(f"{m} 有开放 Q，但模块总览没有“已问待答”")

    required = [
        "docs/STATUS.md", "docs/team.md",
        "docs/requirements/vision.md", "docs/requirements/personas.md",
        "docs/requirements/backlog.md", "docs/requirements/nfr.md",
        "docs/requirements/dialogue.md", "docs/requirements/decisions.md",
        "docs/requirements/glossary.md", "docs/requirements/coverage-scan.md",
        "docs/requirements/models/README.md", "docs/design-notes.md",
    ]
    for rel in required:
        if not os.path.exists(os.path.join(base, rel)):
            issues.append(f"缺少文件：{rel}")

    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in (".git", "PPT", "tools")]
        for fn in filenames:
            if not fn.endswith((".md", ".mmd")):
                continue
            p = os.path.join(dirpath, fn)
            try:
                t = read(p)
            except Exception:
                continue
            for old in OLD_NAMES:
                if old in t:
                    issues.append(f"{os.path.relpath(p, base)} 仍引用旧名称 {old}")

    bad_nfr = [x for x in nfr_ids if not re.match(r"NFR-\d{3}$", x)]
    if bad_nfr:
        issues.append(f"NFR 编号非法：{', '.join(bad_nfr)}")
    if len(nfr_ids) != len(set(nfr_ids)):
        issues.append("NFR 编号重复")

    ids = {r["id"] for r in backlog_rows}
    graph = {}
    for r in backlog_rows:
        if not r["owner"]:
            issues.append(f"{r['id']} 缺负责人")
        deps = re.findall(r"REQ-[A-Z]+-\d{3}", r["deps"])
        graph[r["id"]] = [d for d in deps if d != r["id"]]
        for d in deps:
            if d == r["id"]:
                issues.append(f"{r['id']} 自依赖")
            elif d not in ids:
                issues.append(f"{r['id']} 依赖不存在的 {d}")
    for cyc in find_cycles(graph):
        issues.append("依赖环：" + " → ".join(cyc))

    infos.append(f"Q 表：{len(qrows)} 条，开放 {len(open_rows)} 条")
    infos.append(f"Q 索引：{len(qindex)} 条")
    infos.append(f"S/Q 关联列：{len(wait_build)} 处“待建”")
    infos.append(f"STATUS 待决事项：{len(status_pending)} 条")
    infos.append(f"覆盖扫描：{len(coverage_rows)} 个模块，{sum(1 for v in coverage_rows.values() if '已问待答' in v)} 个有“已问待答”")
    infos.append(f"NFR：{len(nfr_ids)} 条")
    infos.append(f"backlog：{len(backlog_rows)} 条")
    infos.append(f"模型待定点：{len(pending_models)} 张")
    reasons = []
    if open_rows:
        reasons.append(f"{len(open_rows)} 条开放 Q")
    if wait_build:
        reasons.append(f"{len(wait_build)} 处待建")
    if pending_models:
        reasons.append(f"{len(pending_models)} 张含待定点模型")
    infos.append(f"移交前置：{'未通过（' + '、'.join(reasons) + '）' if reasons else '通过'}")
    open_modules = sorted({m.strip() for q in open_rows for m in idxmap.get(q["id"], {}).get("module", "").split("、") if m.strip()})
    infos.append(f"模块门禁：{'未通过（' + '、'.join(open_modules) + ' 有开放 Q）' if open_modules else '通过'}")

    print("== check q ==")
    for x in infos:
        print("INFO", x)
    if issues:
        for x in issues:
            print("FAIL", x)
        print(f"RESULT: FAIL ({len(issues)} 项)")
        return 1
    print("RESULT: PASS")
    return 0


def collect_dor_issues(base):
    _, backlog = parse_backlog(base)
    roles = parse_team_roles(base)
    by_id = {r["id"]: r for r in backlog}
    issues = {}

    def add(rid, msg):
        issues.setdefault(rid, []).append(msg)

    seen = set()
    for r in backlog:
        if r["id"] in seen:
            add(r["id"], "REQ 编号重复")
        seen.add(r["id"])

    allowed_priority = {"Must", "Should", "Could", "Won't", "Won’t"}
    graph = {r["id"]: re.findall(r"REQ-[A-Z]+-\d{3}", r["deps"]) for r in backlog}

    for r in backlog:
        rid = r["id"]
        for field, label in (("title", "标题"), ("story", "故事"), ("acceptance", "验收标准"),
                             ("priority", "优先级"), ("owner", "负责人"), ("deps", "依赖")):
            if not r[field].strip():
                add(rid, f"{label}为空")
        acc = r["acceptance"]
        if acc and not (
            ("给定" in acc and any(x in acc for x in ("则", "当", "如果", "后")))
            or ("Given" in acc and "When" in acc and "Then" in acc)
        ):
            add(rid, "验收标准缺少“给定…则…”或 Given-When-Then")
        if r["priority"] and r["priority"] not in allowed_priority:
            add(rid, f"优先级非法：{r['priority']}")
        if r["owner"] and r["owner"] not in roles:
            add(rid, f"负责人不在 team.md：{r['owner']}")
        for d in re.findall(r"REQ-[A-Z]+-\d{3}", r["deps"]):
            if d == rid:
                add(rid, "自依赖")
            elif d not in by_id:
                add(rid, f"依赖不存在：{d}")

    for cyc in find_cycles(graph):
        add(cyc[0], "依赖环：" + " → ".join(cyc))

    return issues, backlog, by_id


def check_dor(base, target=None, verbose=False):
    issues, backlog, by_id = collect_dor_issues(base)
    if target and target not in by_id:
        print(f"FAIL {target}: 不存在")
        print("RESULT: FAIL")
        return 1

    selected = [r for r in backlog if target is None or r["id"] == target]
    failed = [r["id"] for r in selected if r["id"] in issues]
    for r in selected:
        rid = r["id"]
        if rid in issues:
            print(f"FAIL {rid}: " + "；".join(issues[rid]))
        elif verbose:
            print(f"PASS {rid}")
    print("INFO 未检查：故事来源、关联 Q（backlog 无列）")
    print(f"RESULT: {'FAIL' if failed else 'PASS'} ({len(failed)}/{len(selected)})")
    return 1 if failed else 0


def check_gate_handoff(base):
    _, qindex, qrows, srows = parse_dialogue(base)
    _, stage, _, _ = parse_status(base)
    _, module_order = parse_vision_modules(base)
    _, coverage_rows = parse_coverage(base)
    _, pending_models = parse_models(base)
    _, nfr_ids = parse_nfr(base)
    dor_issues, backlog, _ = collect_dor_issues(base)

    open_rows = [q for q in qrows if q["status"] in OPEN]
    idxmap = {x["id"]: x for x in qindex}
    idx_order = {x["id"]: int(x["order"]) if x["order"].isdigit() else 999 for x in qindex}
    open_rows.sort(key=lambda q: idx_order.get(q["id"], 999))
    wait_build = [x["id"] for x in srows + qrows if "待建" in x["link"]]
    blockers, infos = [], []

    infos.append(f"阶段：{stage}（移交触发还需“需求确认完成”或用户明确要求）")
    if open_rows:
        blockers.append(f"开放 Q：{len(open_rows)} 条（{', '.join(q['id'] for q in open_rows)}）")
    else:
        infos.append("开放 Q：0")
    if wait_build:
        blockers.append(f"待建关联列：{len(wait_build)} 处")
    else:
        infos.append("待建关联列：0")
    if pending_models:
        blockers.append(f"含待定点模型：{len(pending_models)} 张（{', '.join(pending_models)}）")
    else:
        infos.append("含待定点模型：0")

    bad_nfr = [x for x in nfr_ids if not re.match(r"NFR-\d{3}$", x)]
    if bad_nfr or len(nfr_ids) != len(set(nfr_ids)):
        blockers.append("NFR 编号非法或重复")
    else:
        infos.append(f"NFR：{len(nfr_ids)} 条编号合法")

    if dor_issues:
        ids = sorted(dor_issues)
        more = "…" if len(ids) > 10 else ""
        blockers.append(f"DoR 未通过：{len(ids)} 条（{', '.join(ids[:10])}{more}）")
    else:
        infos.append(f"DoR：0/{len(backlog)} 未通过")

    module_issues = []
    for m in module_order:
        if m not in coverage_rows:
            module_issues.append(f"{m} 缺模块总览")
        elif "未问" in coverage_rows[m]:
            module_issues.append(f"{m} 六维有未问")
    open_modules = sorted({
        m.strip() for q in open_rows
        for m in idxmap.get(q["id"], {}).get("module", "").split("、") if m.strip()
    })
    if open_modules:
        module_issues.append("开放 Q 模块：" + "、".join(open_modules))
    if module_issues:
        blockers.append("模块门禁：" + "；".join(module_issues))
    else:
        infos.append("模块门禁：通过")

    print("== check gate handoff ==")
    for x in infos:
        print("INFO", x)
    for x in blockers:
        print("FAIL", x)
    print(f"RESULT: {'FAIL' if blockers else 'PASS'} ({len(blockers)} 项)")
    return 1 if blockers else 0


def extract_q_ids(text):
    ids = []
    for m in re.finditer(r"Q-(\d{3})\s*[～~]\s*(?:Q-)?(\d{3})", text):
        a, b = int(m.group(1)), int(m.group(2))
        ids.extend(f"Q-{i:03d}" for i in range(a, b + 1))
    for m in re.finditer(r"Q-(\d{3})((?:/\d{3})+)", text):
        ids.append(f"Q-{int(m.group(1)):03d}")
        for part in m.group(2).split("/")[1:]:
            ids.append(f"Q-{int(part):03d}")
    ids.extend(re.findall(r"Q-\d{3}", text))
    seen, out = set(), []
    for x in ids:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def parse_models_table(base):
    text = read(os.path.join(base, "docs/requirements/models/README.md"))
    rows = []
    for line in text.splitlines():
        if line.startswith("| ") and not line.startswith("|---"):
            c = cells(line)
            if len(c) >= 7 and c[0] != "图题":
                rows.append({
                    "title": c[0],
                    "src": c[3].strip("`"),
                    "img": c[4].strip("`"),
                    "sources": c[5],
                    "status": c[6],
                })
    return text, rows


def check_models(base, verbose=False):
    _, _, qrows, _ = parse_dialogue(base)
    open_ids = {q["id"] for q in qrows if q["status"] in OPEN}
    _, rows = parse_models_table(base)
    mdir = os.path.join(base, "docs/requirements/models")
    src_dir = os.path.join(mdir, "src")
    img_dir = os.path.join(mdir, "img")
    issues = {}

    def add(title, msg):
        issues.setdefault(title, []).append(msg)

    pending = 0
    for r in rows:
        src = os.path.join(mdir, r["src"]) if r["src"] else ""
        img = os.path.join(mdir, r["img"]) if r["img"] else ""
        if not r["src"] or not os.path.exists(src):
            add(r["title"], f"源文件不存在：{r['src'] or '空'}")
        elif not r["src"].endswith((".mmd", ".md")):
            add(r["title"], f"源扩展名不对：{r['src']}")
        if not r["img"] or not os.path.exists(img):
            add(r["title"], f"图文件不存在：{r['img'] or '空'}")
        elif not r["img"].endswith((".svg", ".png")):
            add(r["title"], f"图扩展名不对：{r['img']}")
        if "含待定点" in r["status"]:
            pending += 1
            qids = set(extract_q_ids(r["sources"] + " " + r["status"]))
            if not (qids & open_ids):
                add(r["title"], "含待定点但没有关联开放 Q")
            if src and os.path.exists(src):
                st = read(src)
                if not any(x in st for x in ("待定", "待确认", "未定")):
                    add(r["title"], "状态含待定点，但源文件没有待定注释")

    src_files = sorted(os.listdir(src_dir)) if os.path.isdir(src_dir) else []
    img_files = sorted(os.listdir(img_dir)) if os.path.isdir(img_dir) else []
    listed_src = {r["src"] for r in rows if r["src"]}
    listed_img = {r["img"] for r in rows if r["img"]}
    for fn in src_files:
        if fn.endswith((".mmd", ".md")) and f"src/{fn}" not in listed_src:
            add("README", f"源文件未登记：src/{fn}")
    for fn in img_files:
        if fn.endswith((".svg", ".png")) and f"img/{fn}" not in listed_img:
            add("README", f"图文件未登记：img/{fn}")

    img_stems = {}
    for fn in img_files:
        stem, ext = os.path.splitext(fn)
        if ext in (".svg", ".png"):
            img_stems.setdefault(stem, set()).add(ext)
    for stem, exts in img_stems.items():
        if len(exts) > 1:
            add("README", f"同一图多种格式：{stem} {sorted(exts)}")

    src_stems = {}
    for fn in src_files:
        stem, ext = os.path.splitext(fn)
        if ext in (".mmd", ".md"):
            src_stems.setdefault(stem, set()).add(ext)
    for stem, exts in src_stems.items():
        if len(exts) > 1:
            add("README", f"同一源多种格式：{stem} {sorted(exts)}")

    for r in rows:
        if r["title"] in issues:
            print(f"FAIL {r['title']}: " + "；".join(issues[r["title"]]))
        elif verbose:
            print(f"PASS {r['title']}")
    if "README" in issues:
        print("FAIL README: " + "；".join(issues["README"]))
    print(f"INFO 模型：{len(rows)} 行；含待定点 {pending} 张")
    print(f"RESULT: {'FAIL' if issues else 'PASS'} ({len(issues)} 项)")
    return 1 if issues else 0


def check_refs(base):
    issues = set()
    scanned = pref = pathref = 0
    index_path = os.path.join(base, "docs/requirements/research/sources/INDEX.md")
    pids = set(re.findall(r"P-\d{3}", read(index_path))) if os.path.exists(index_path) else set()
    if not pids:
        issues.add("sources/INDEX.md 缺失或没有 P-ID")

    docs_root = os.path.join(base, "docs")
    for dp, dns, fns in os.walk(docs_root):
        dns[:] = [d for d in dns if d != "PPT"]
        for fn in fns:
            if not fn.endswith((".md", ".mmd")):
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, base)
            scanned += 1
            t = read(p)
            for pid in re.findall(r"P-\d{3}", t):
                pref += 1
                if pid not in pids:
                    issues.add(f"{rel}: P-ID 不在 INDEX：{pid}")
            for path in re.findall(r"docs/[A-Za-z0-9_./-]+\.(?:md|mmd|svg|png)", t):
                if any(x in path for x in "<>*"):
                    continue
                if path == "docs/requirements/context.md":
                    continue
                pathref += 1
                if not os.path.exists(os.path.join(base, path)):
                    issues.add(f"{rel}: 路径不存在：{path}")
            for m in re.findall(r"(?<![A-Za-z0-9_/])research/([A-Za-z0-9_-]+)\.md", t):
                pathref += 1
                target = f"docs/requirements/research/{m}.md"
                if not os.path.exists(os.path.join(base, target)):
                    issues.add(f"{rel}: 路径不存在：{target}")
            for m in re.findall(r"(?<![A-Za-z0-9_/])((?:src|img)/[A-Za-z0-9_.-]+\.(?:md|mmd|svg|png))", t):
                pathref += 1
                target = f"docs/requirements/models/{m}"
                if not os.path.exists(os.path.join(base, target)):
                    issues.add(f"{rel}: 路径不存在：{target}")

    skill_root = os.path.join(base, ".claude/skills/requirements-analysis")
    for dp, dirs, fns in os.walk(skill_root):
        for fn in fns:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, base)
            t = read(p)
            for m in re.findall(r"references/([A-Za-z0-9_-]+\.md)", t):
                if not os.path.exists(os.path.join(skill_root, "references", m)):
                    issues.add(f"{rel}: 路径不存在：references/{m}")
            for path in re.findall(r"tools/[A-Za-z0-9_./-]+", t):
                if any(x in path for x in "<>*"):
                    continue
                if not os.path.exists(os.path.join(base, path)):
                    issues.add(f"{rel}: 路径不存在：{path}")

    for dp, dns, fns in os.walk(base):
        dns[:] = [d for d in dns if d not in (".git", "PPT", "tools")]
        for fn in fns:
            if not fn.endswith((".md", ".mmd")):
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, base)
            t = read(p)
            for old in OLD_NAMES:
                if old in t:
                    issues.add(f"{rel}: 旧名称 {old}")

    print("== check refs ==")
    print(f"INFO 文档：{scanned}；P-ID 引用：{pref}；路径引用：{pathref}")
    for x in sorted(issues):
        print("FAIL", x)
    print(f"RESULT: {'FAIL' if issues else 'PASS'} ({len(issues)} 项)")
    return 1 if issues else 0


def parse_glossary_modules(base):
    text = read(os.path.join(base, "docs/requirements/glossary.md"))
    out = {}
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        c = cells(line)
        if len(c) < 2:
            continue
        m = re.match(r"(.+?)（([A-Z]+)）", c[0])
        if m:
            out[m.group(1).strip()] = m.group(2)
    return out


def parse_team_scopes(base):
    text = read(os.path.join(base, "docs/team.md"))
    rows = []
    for line in text.splitlines():
        if line.startswith("| ") and not line.startswith("|---"):
            c = cells(line)
            if len(c) >= 3 and c[0] != "角色":
                rows.append((c[0], c[1], c[2]))
    return rows


def check_gate_module(base, target=None):
    if not target:
        print("usage: reqtool.py check gate module <模块|缩写>", file=sys.stderr)
        return 64
    _, module_order = parse_vision_modules(base)
    glossary = parse_glossary_modules(base)
    reverse = {v: k for k, v in glossary.items()}
    name = reverse.get(target.upper(), target)
    if name not in module_order:
        print(f"FAIL 模块不在 vision 范围：{target}")
        print("RESULT: FAIL")
        return 1

    _, qindex, qrows, srows = parse_dialogue(base)
    _, coverage_rows = parse_coverage(base)
    blockers, infos = [], []
    abbr = glossary.get(name, "")
    infos.append(f"模块：{name}" + (f"（{abbr}）" if abbr else ""))
    roles = [r[0] for r in parse_team_scopes(base) if name in r[2]]
    if roles:
        infos.append("负责角色：" + "、".join(roles))

    if name not in coverage_rows:
        blockers.append("coverage-scan 缺模块总览")
    else:
        dims = coverage_rows[name]
        infos.append("六维：" + "、".join(
            f"{d}={s}" for d, s in zip(("角色", "旅程", "对象", "规则", "横切", "质量"), dims)
        ))
        if "未问" in dims:
            blockers.append("六维有“未问”")

    idxmap = {x["id"]: x for x in qindex}
    open_qs = [
        q["id"] for q in qrows
        if q["status"] in OPEN and name in [
            m.strip() for m in idxmap.get(q["id"], {}).get("module", "").split("、")
        ]
    ]
    if open_qs:
        blockers.append("开放 Q：" + "、".join(open_qs))
    else:
        infos.append("开放 Q：0")

    wait_build = [x["id"] for x in srows + qrows if "待建" in x["link"]]
    if wait_build:
        blockers.append(f"待建关联列（全局）：{len(wait_build)} 处")
    else:
        infos.append("待建关联列：0")

    print(f"== check gate module {name} ==")
    for x in infos:
        print("INFO", x)
    for x in blockers:
        print("FAIL", x)
    print(f"RESULT: {'FAIL' if blockers else 'PASS'} ({len(blockers)} 项)")
    return 1 if blockers else 0


def q_next(base):
    _, qindex, qrows, _ = parse_dialogue(base)
    _, module_order = parse_vision_modules(base)
    open_rows = [q for q in qrows if q["status"] in OPEN]
    if not open_rows:
        print("none")
        return 2
    enriched = []
    for q in open_rows:
        idx = next((x for x in qindex if x["id"] == q["id"]), {})
        enriched.append(dict(q, module=idx.get("module", ""), category=idx.get("category", "普通"), summary=idx.get("summary", q["question"])))
    nxt = order_open(enriched, module_order)[0]
    print("next:", nxt["id"])
    print("module:", nxt["module"])
    print("question:", nxt["question"])
    print("category:", nxt["category"])
    print("reason: 类别优先 → 模块顺序 → Q 号")
    return 0


USAGE = "usage: reqtool.py [repo] check q | check dor [REQ] | check models | check refs | check gate module <模块> | check gate handoff | q next"


def main():
    args = sys.argv[1:]
    if not args:
        print(USAGE, file=sys.stderr)
        return 64
    if args[0] in ("-h", "--help"):
        print(USAGE)
        return 0
    if args[0] in ("check", "q"):
        base, cmd, rest = ".", args[0], args[1:]
    else:
        base = args[0]
        cmd = args[1] if len(args) > 1 else ""
        rest = args[2:]
    if cmd == "check" and rest[:1] == ["q"]:
        return check_q(base)
    if cmd == "check" and rest[:1] == ["dor"]:
        args = [x for x in rest[1:] if not x.startswith("--")]
        target = args[0] if args else None
        return check_dor(base, target, "--verbose" in rest)
    if cmd == "check" and rest[:1] == ["models"]:
        return check_models(base, "--verbose" in rest)
    if cmd == "check" and rest[:1] == ["refs"]:
        return check_refs(base)
    if cmd == "check" and rest[:2] == ["gate", "module"]:
        return check_gate_module(base, rest[2] if len(rest) > 2 else None)
    if cmd == "check" and rest[:2] == ["gate", "handoff"]:
        return check_gate_handoff(base)
    if cmd == "q" and rest[:1] == ["next"]:
        return q_next(base)
    print(USAGE, file=sys.stderr)
    return 64


if __name__ == "__main__":
    sys.exit(main())
