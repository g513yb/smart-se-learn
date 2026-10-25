# 来源登记

验证时间：2026-10-23。方法：`curl` 检查 HTTP 状态与页面标题，配合检索结果核对官方性；用户提供的 PDF 用标题、DOI 与正文核对。未登录、未绕过访问限制。

命名规则：`P-<三位序号>_<平台或主题>_<内容>_<年份或章节>.pdf`。旧目录页与首页移入 `_archive/`，不参与分析。

## 状态说明

- **已批准**：来源可达，内容与模块相关，可直接使用
- **部分验证**：来源存在，但只有目录/首页、文件不匹配，或为视频页面；只能使用摘要或目录，引用时必须标注
- **候选**：有线索但未验证，或只有预印本 / 二手来源；使用前需确认
- **缺失**：来源已定位，但文件尚未提供
- **排除**：不可达、非官方或已停止服务，不作为依据

## 一、来源总表

| P-ID | 标题 | 机构/作者 | 年份 | 类型 | 模块 | 状态 | 证据强度 | 备注 |
|---|---|---|---|---|---|---|---|---|
| P-001 | Moodle – Tracking progress | Moodle Docs | 2025 | 官方文档 | 学习记录 | 已批准 | 全文 | 完成状态、完成矩阵、报告 |
| P-002 | Moodle – Analytics | Moodle Docs | — | 官方文档 | 学习记录 / 诊断 | 已批准 | 全文 | 学习分析与风险学生 |
| P-003 | Open edX Aspects Overview | Open edX Docs | Redwood | 官方文档 | 学习记录 | 已批准 | 摘要 | 教师端课程范围分析 |
| P-004 | Canvas – What is New Analytics? | Instructure Community | — | 官方社区视频 | 学习记录 | 已批准 | 视频 / 文字稿 | 教师与学生可见数据 |
| P-005 | AState KB – Canvas New Analytics 镜像 | — | — | 网页 | — | 排除 | — | 不可达（000） |
| P-006 | xAPI Base Standard | ADL / IEEE / ISO | 2025 | 标准 | 学习记录 | 已批准 | 摘要 | 记录模型与互操作 |
| P-007 | Canvas Analytics overview | Instructure | — | 官方网页 | — | 排除 | — | 超时（000） |
| P-008 | Data & Insights | Instructure | — | 官方网页 | — | 排除 | — | 超时（000） |
| P-009 | ALEKS Educator's Manual | ALEKS | — | 教师手册 | 诊断 / 画像 / 推荐 | 已批准 | — | 知识点掌握、报告、推荐工具 |
| P-010 | Khan Academy – reports | Khan Academy | — | 官方文档 | 诊断 / 画像 / 推荐 | 已批准 | 全文 | Activity / Skills / Assignment 报告 |
| P-011 | Khanmigo | Khan Academy | — | 产品文档 | 5E / 教师干预 | 已批准 | 全文 | 教师工具；营销性质，需交叉验证 |
| P-012 | 超星学习通 | 超星 | — | 页面 / 视频 | 学习记录 | 部分验证 | 页面级 / 视频 | 11 份分节文件，见文件清单 |
| P-013 | 雨课堂 | 雨课堂 | — | 官方帮助文章 | 诊断 / 画像 / 学习记录 | 部分验证 | 全文 / 页面级 | 成绩分析全文；分类索引页面级；其他教学数据文章待补 |
| P-014 | Tipple & Linden, ISEDJ 2026 | Tipple & Linden | 2026 | 学术论文 | 5E | 已批准 | 全文 | pp. 32-47 |
| P-015 | Smart Cyber Learning | IEEE | 2026 | 学术论文 | 5E | 已批准 | 全文 | 5E + 多智能体 + 自适应评估 |
| P-016 | TALPer / 因材網 | — | — | 官方页 | 5E | 部分验证 | — | 官方页不可达；用 P-026 间接补充 |
| P-017 | Precision Education 愿景 | arXiv | — | 观点性预印本 | 数字孪生 | 候选 | — | 适合生成问题 |
| P-018 | Classroom Simulacra | CHI 2025 / arXiv | 2025 | 预印本 | 数字孪生 | 已批准 | 摘要 | 学生行为模拟；同行评议版为 CHI 2025 |
| P-019 | 生成式 AI 模拟学习行为 | arXiv | — | 预印本 | 数字孪生 | 候选 | — | 可作交叉参考 |
| P-020 | Proposed Student Digital Twin Data Model | — | 2025 | 学术论文 | 数字孪生 | 已批准 | 全文 | DOI 与标题核对一致 |
| P-021 | Data-Driven Digital Twin for Engagement | — | 2025 | 学术论文 | 数字孪生 | 已批准 | 全文 | DOI 与标题核对一致 |
| P-022 | Digital Twin Universities | Zenodo | 2026 | 学术论文 | 数字孪生 | 已批准 | 全文 | 学生数字孪生框架 |
| P-023 | GitHub Classroom Docs | GitHub | — | 官方文档 | SE 课程 | 候选 | — | 历史参考；据检索摘要已于 2026-08-28 停服，待复核 |
| P-024 | PrairieLearn Docs | PrairieLearn | — | 官方文档 | SE 课程 | 已批准 | 摘要 | 题库、随机化题目、自动评测、外部评测、重判、API |
| P-025 | Autolab Docs | Autolab | — | 官方文档 | SE 课程 | 候选 | — | 自动评测平台；功能页待抽样 |
| P-026 | CACEt 2025 – 因材網自主學習精靈 | CACEt 2025 | 2025 | 学术论文 | 5E / TALPer | 已批准 | — | 学术间接来源；不是官方产品文档 |

## 二、文件清单

### 本地文件

| P-ID | 文件 | 内容 | 模块 |
|---|---|---|---|
| P-001 | `P-001_moodle_tracking_progress.pdf` | Moodle – Tracking progress | 学习记录 |
| P-002 | `P-002_moodle_analytics_plugins.pdf` | Moodle – Analytics | 学习记录 / 诊断 |
| P-010 | `P-010_khan_academy_reports_activity_skills.pdf` | How do I use Reports to view Activity, Skills, and Assignment score reports? | 诊断 / 画像 / 推荐 |
| P-011 | `P-011_khanmigo_teacher_tools.pdf` | What teacher tools are available on Khanmigo? | 5E / 教师干预 |
| P-012 | `P-012_chaoxing_9.2_class_report.pdf` | 超星 9.2 课堂报告 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.1_chapter_learning_count.pdf` | 9.3.1 章节学习次数统计 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.2_chapter_task_points.pdf` | 9.3.2 章节任务点统计 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.3_checkin_stats.pdf` | 9.3.3 课程签到统计 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.4_course_points.pdf` | 9.3.4 课程积分统计 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.5_assignment_stats.pdf` | 9.3.5 课程作业统计 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.6_chapter_quiz_stats.pdf` | 9.3.6 章节测验统计 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.7_exam_stats.pdf` | 9.3.7 课程考试统计 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.8_discussion_stats.pdf` | 9.3.8 课程讨论统计 | 学习记录 |
| P-012 | `P-012_chaoxing_9.3.9_teaching_alert_stats.pdf` | 9.3.9 教学预警统计 | 学习记录 / 干预 |
| P-012 | `P-012_chaoxing_9.4_grade_stats_export.pdf` | 9.4 成绩统计与导出 | 学习记录 |
| P-013 | `P-013_yuketang_score_analysis.pdf` | 雨课堂 成绩分析 | 诊断 / 画像 |
| P-013 | `P-013_yuketang_teaching_data_category.pdf` | 教学数据查收和分析（分类索引） | 学习记录 / 画像 |
| P-014 | `P-014_tipple_linden_2026.pdf` | Tipple & Linden 2026，5E + LMS 分析 | 5E |
| P-015 | `P-015_smart_cyber_learning_2026.pdf` | Smart Cyber Learning，IEEE 2026 | 5E |
| P-020 | `P-020_student_digital_twin_data_model_2025.pdf` | Student Digital Twin Data Model | 数字孪生 |
| P-021 | `P-021_digital_twin_engagement_2025.pdf` | Digital Twin for Student Engagement | 数字孪生 |
| P-022 | `P-022_digital_twin_universities_2026.pdf` | Digital Twin Universities | 数字孪生 |
| P-026 | `P-026_cacet_talper_2025.pdf` | 因材網自主學習精靈之自我調節行為 | 5E / TALPer |

### 远程可访问（未落盘）

| P-ID | URL | 内容 |
|---|---|---|
| P-003 | https://docs.openedx.org/projects/openedx-aspects/en/open-release-redwood.master/concepts/aspects_overview.html | Open edX Aspects |
| P-004 | https://community.canvaslms.com/t5/Canvas-Video-Shorts/Video-What-is-New-Analytics/ta-p/650868 | Canvas New Analytics 视频 |
| P-006 | https://opensource.ieee.org/xapi/xapi-base-standard-documentation | xAPI 标准 |
| P-009 | https://www.aleks.com/manual/pdf/educators-he.pdf | ALEKS 教师手册 |
| P-018 | https://arxiv.org/abs/2502.02780 | Classroom Simulacra |
| P-024 | https://docs.prairielearn.com/ | PrairieLearn Docs |

P-017、P-019、P-023、P-025 只有候选线索，URL 待补；P-016 官方页不可达；P-005、P-007、P-008 已排除。

## 三、模块与来源速览

| 模块 | 来源 |
|---|---|
| 学习记录 | P-001、P-002、P-003、P-004、P-006、P-012、P-013 |
| 学习诊断 / 学生画像 / 内容推荐 | P-009、P-010、P-011、P-012、P-013 |
| 5E 智能体 | P-014、P-015、P-016、P-026 |
| 学生数字孪生 | P-020、P-021、P-022、P-018、P-017、P-019 |
| 软件工程课程特有 | P-024、P-025、P-023 |
| 已排除 | P-005、P-007、P-008 |

## 四、汇总

| 状态 | 数量 | P-ID |
|---|---|---|
| 已批准 | 16 | P-001、P-002、P-003、P-004、P-006、P-009、P-010、P-011、P-014、P-015、P-018、P-020、P-021、P-022、P-024、P-026 |
| 部分验证 | 3 | P-012、P-013、P-016 |
| 缺失 | 0 | — |
| 候选 | 4 | P-017、P-019、P-023、P-025 |
| 排除 | 3 | P-005、P-007、P-008 |

## 五、缺口与补充建议

| 缺口 | 现状 | 建议 | 优先级 |
|---|---|---|---|
| 超星学情统计细节 | 9.3.x 为视频页面 | 补字幕或关键截图 | 中 |
| 雨课堂其他教学数据 | 只有成绩分析与分类索引 | 补课堂报告、学习分析、学生画像预警 | 中 |
| 教师干预 | 无预警系统来源 | Course Signals、Civitas 等 | 中 |
| 平台基础 | 无账号、权限、通知、内容上传的专门来源 | Moodle / Canvas / Open edX 对应文档 | 中 |
| 非功能与合规 | 无 ISO 29148、ISO 25010、隐私与等保来源 | 加入标准与合规来源 | 中 |

## 六、归档

| 文件 | 原因 |
|---|---|
| `_archive/P-012_chaoxing_toc_full.pdf` | 原目录页，已被 9.2 / 9.3 / 9.4 分节文件替代 |
| `_archive/P-013_yuketang_help_center_index.pdf` | 帮助中心首页，已被分类页与成绩分析文章替代 |

## 七、使用规则

- 只能使用“已批准”和“部分验证”的来源。
- “部分验证”必须标注目录、首页、视频页面或文件不匹配，结论需复核。
- “候选”来源使用前需用户确认；确认后在本表更新状态。
- “缺失”来源不得引用，直到文件补齐。
- “排除”来源不得写入 brief。
- 清单外平台需用户确认后加入，并记录。
