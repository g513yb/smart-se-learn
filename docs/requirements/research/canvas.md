# Canvas 对标 brief

## 1. 检索问题

教师在学习记录与分析中能看到什么、能做什么？学生能看到什么？

## 2. 来源清单

| P-ID | 标题 | 机构 | URL | HTTP | 访问日期 | 类型 |
|---|---|---|---|---|---|---|
| P-004 | Video: What is New Analytics? | Instructure Community | https://community.canvaslms.com/t5/Canvas-Video-Shorts/Video-What-is-New-Analytics/ta-p/650868 | 200 | 2026-10-23 | 官方社区视频与文字稿 |
| P-005 | How do I view New Analytics for a student in a course? | Arkansas State University KB（Canvas 指南镜像） | https://kb.astate.edu/books/canvas-instructor-how-tos/page/how-do-i-view-new-analytics-for-a-student-in-a-course/export/pdf | 000 | 2026-10-23 | 镜像，不可达，仅作线索 |
| P-007 | Canvas Analytics overview | Instructure | https://www.instructure.com/node/26391 | 000 | 2026-10-23 | 官方概览，超时 |
| P-008 | Data & Insights | Instructure | https://www.instructure.com/en-gb/solutions/data-insights | 000 | 2026-10-23 | 官方方案页，超时 |

说明：P-004 可直接抓取；P-005 / P-007 / P-008 不可达，仅作线索，不作为主要依据。

## 3. 需求观察（用户可见行为）

### 教师

- 查看课程与学生分析、课程成绩。
- 查看每周在线活动：平均页面浏览与参与次数，按周一到周日统计。
- 查看学生标签页、缺交与迟交作业、沟通记录。
- 使用学生上下文卡片查看参与率。
- 查看模块进度、掌握度成绩册、视频参与洞察、风险学生提醒。
- 导出 CSV，向学生发消息。

### 学生

- 视频说明学生可查看自己的成绩、活动与沟通数据，需具备相应权限；具体范围待确认。
- 模块进度可见。

### 管理员

- 查看标准报告、数据导出和 SIS 数据。

### 时效

- P-004 称数据约 24 小时刷新；P-005 镜像称 8～24 小时。两者不一致，已生成 Q-014。

## 4. 设计线索

| DSN | 做法 | 备注 |
|---|---|---|
| DSN-007 | 周活动聚合视图 | 视图设计 |
| DSN-008 | 缺交 / 迟交报告与消息联动 | 交互设计 |
| DSN-009 | 事件级数据导出与 BI 对接 | 数据导出设计 |
| DSN-010 | 参与度定义：提交作业、测验、讨论、公告、会议、页面 | 指标口径 |
| DSN-011 | 分析刷新与缓存策略 | 性能与时效设计 |

## 5. 与本项目的差异

- Canvas 以课程管理和评分为中心；本项目需要更细的行为与认知状态数据。
- 刷新延迟对教师干预的时效性可能是约束，需要确认。
- 学生端可查看的数据范围比教师端窄，具体边界待确认。
- 主要来源是官方社区视频，覆盖范围有限；P-005 等镜像不可达，结论需复核。

## 6. 生成的 Q

Q-002、Q-003、Q-010、Q-011、Q-012、Q-013、Q-014、Q-018、Q-020。
