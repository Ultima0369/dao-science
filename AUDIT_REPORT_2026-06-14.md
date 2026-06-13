# 项目深度审计报告：面向计算机科学受众的优化方向

**审计日期**：2026-06-14  
**审计范围**：全仓库（`1_first_principles/`、`2_models/`、`3_methodology/`、`4_applications/`、`verifiable_units/`、`simulations/`、`tools/n_of_1/`、`scripts/`、站点配置与流程）  
**目标受众假设**：GitHub 与学术预印本的主要读者为计算机科学、工程、逻辑背景较强，但对认知科学、复杂系统、非经典逻辑不一定熟悉的人群。  
**审计方法**：三名只读探索子代理并行审查内容形式化、导航可发现性、工具链可复现性；父代理综合并给出优先级排序。

---

## 1. 核心结论

本项目在**概念框架、符号统一、可验证单元（VU）架构、双语站点**上已经建立了相当高的完成度，尤其是：

- `NOTATION.md` 统一了符号约定；
- `CLAIMS.md` 主张登记册把理论承诺与证据等级挂钩；
- 每个 VU 都指向可运行的 `simulations/*.py`；
- MkDocs + `mkdocs-static-i18n` 已实现双语 suffix 模式。

然而，对于一个**逻辑思维强但跨学科背景不足**的 CS 读者，当前最大的摩擦不是“内容不够深”，而是：

> **地图与工具链的“可信度信号”还不够稳定**——符号不一致、英文 stub 森林、VU 实验设计不完整、CI 未覆盖全部仿真脚本、依赖未锁定。

这些瑕疵会让一个严谨的 CS 读者在 5 分钟内产生“这项目还没准备好”的印象，尽管其底层思想已经很硬。

---

## 2. 受众画像与阅读路径推断

| 读者类型 | 第一疑问 | 当前体验 | 优化杠杆 |
|---------|---------|---------|---------|
| 工程师 / 开源贡献者 | “这是库？框架？还是理论手册？” | README 未明确区分 | 在 README 顶部加 “What this repo is (and isn’t)” |
| 研究者 / 审稿人 | “ claims 有证据吗？能复现吗？” | CLAIMS/VU 架构好，但 badge 使用不一致 | 清理 badge、补全 VU 实验设计、加自动一致性检查 |
| 英文读者 | “英文版能看吗？” | 27 个 `.en.md` 仍是 stub | 优先翻译或临时下架英文 stub |
| 代码贡献者 | “怎么跑测试？依赖怎么装？” | 无 pytest、依赖未全锁定、CI 只跑 3 个仿真 | 加测试矩阵、锁定依赖、跑全部仿真 |
| 普通读者 | “我从哪开始？” | 阅读路径按兴趣分，无 CS 专属入口 | 在 POSITIONING 加 “工程师/CS 速读路径” |

---

## 3. 按主题汇总的问题与建议

### 3.1 内容形式化：符号与 badge 的纪律性

| ID | 严重度 | 位置 | 问题 | 建议修复方向 |
|----|--------|------|------|-------------|
| F1 | **严重** | `GLOSSARY.md:224`、`project_map.md:20`、`FINAL_VISION.md:223` | `AB(t)` 公式仍写为 `Cmax − RDMN(t)`，与 `NOTATION.md` 和 `02_one_as_bandwidth.md` 的归一化形式矛盾 | 全仓统一为 `AB(t) = 1 − [R_DMN(t) − R_0]/[R_max − R_0]`；加 CI lint 扫描旧字符串 |
| F2 | **严重** | `11_scale_and_moral_silence.md` | 使用了未定义的 `[P]` badge | 在 `NOTATION.md` 定义 `[P]`，或改用 `[B]` |
| F3 | **严重** | `10_de_and_ming.md` 头部、`CLAIMS.md` C23 | 声称 `[N]` 神经证据，但同文件承认“神经对应尚未精确定位” | 降级为 `[F/B/M]`，与 `VU-09` 保持一致 |
| F4 | **严重** | `08_space_time_and_modeling.md` | `[M]` 被当作“数学”而非 `NOTATION.md` 定义的“元伦理/规范”；`[N/B]` 压缩写法不规范 | 新增 `[Math]` badge 或改为文字说明；拆分为 `[N] + [B]` |
| F5 | **严重** | `VU-04` 至 `VU-07` 的 `.en.md` | 4 个英文 stub 只有 “English translation in progress” | 优先翻译，或临时从英文导航中移除 |
| F6 | **严重** | `VU-08/09/10` | 只有形式化+仿真，缺少实验方案（受试者、任务、主要指标、统计假设） | 补全实验设计草案，参照 VU-01/02/03 模板 |
| F7 | 中等 | `2_models/neuroplasticity_loop.md` | 文件在 Models 目录下却没有一个标准可塑性更新方程 | 增加 Hebbian / BCM / STDP 方程及参数表 |
| F8 | 中等 | `2_models/hypoxia_fifty_demons.md` | 因果语言强于证据，无仿真 |  soften 为“可检验假说”并补充局限段；如形式化则新增 VU+仿真 |
| F9 | 中等 | `1_first_principles/09_node_and_translation.md` | 自承缺少“节点质量量化指标” | 提出至少一个可计算代理指标，如翻译层互信息保持率或重构损失 |
| F10 | 中等 | `1_first_principles/04_philosophy_of_science.md` | 把哲学家映射到 L0-L7 更像概念类比，却标 `[F]` | 改为 `[Conceptual]` 或明确形式化标准 |

**形式化主题的关键信号**：CS 读者对“符号不自洽”和“badge 膨胀”极其敏感。F1–F4 是“地图 vs territory”层面的低级错误，会直接瓦解信任。

### 3.2 导航与 onboarding：降低第一印象摩擦

| ID | 严重度 | 位置 | 问题 | 建议修复方向 |
|----|--------|------|------|-------------|
| N1 | **严重** | 27 个 `.en.md` | 英文版大量 stub，切换语言后体验崩塌 | 优先翻译 `README`、`POSITIONING`、`L0_L7_spectrum`、`01_dao_as_process`、`CLAIMS`；或临时隐藏未翻译页 |
| N2 | 严重 | `README.md` | 未明确回答“这是库/框架/理论？” | 加 “What this repo is (and isn’t)” 盒子 |
| N3 | 严重 | `README.md` | `verifiable_units/` 与 `simulations/` 关系未说明 | 在项目结构表中加一行说明：VU 是文档，仿真脚本在 `simulations/` |
| N4 | 严重 | `CONTRIBUTING.md` | 门槛高，缺少“首次贡献”路径 | 增加低门槛任务清单：修引用、翻译段落、补 docstring、核对 badge |
| N5 | 中等 | `0_motivation/project_map.md` | Mermaid 图缺少 `management.md`、`management_field_theory.md` 两个应用节点 | 在 Layer 4 子图增加 MGMT、FIELD 节点 |
| N6 | 中等 | `GLOSSARY.en.md` | 英文术语表自称“完整版见中文 GLOSSARY.md” | 完成核心条目翻译，或顶部加覆盖范围说明 |
| N7 | 中等 | `mkdocs.yml` | nav_translations 手动维护，容易漂移 | 扩展 `audit_nav_coverage.py` 检查每个中文标题都有翻译 |
| N8 | minor | `tools/n_of_1/README.md` | 未接入 MkDocs 导航 | 在“附录”或“实践方法”中增加工具包入口 |
| N9 | minor | `agent/future-spec.md` | 孤立文件，未在 nav 或 README 中引用 | 决定公开/私有，公开则加入附录 |

### 3.3 工具链与可复现性：从“能跑”到“可信任”

| ID | 严重度 | 位置 | 问题 | 建议修复方向 |
|----|--------|------|------|-------------|
| T1 | **关键** | `simulations/amygdala_pfc_hijack.py`、`dmn_ecn_creativity.py` | 未设置 `matplotlib.use("Agg")`，headless/CI 会崩溃 | 所有绘图脚本加 `matplotlib.use("Agg")` |
| T2 | **关键** | `.github/workflows/ci-checks.yml` | CI 只跑 3 个仿真，其余 7 个可能损坏而不自知 | 发现/运行全部 `simulations/*.py`，或维护显式清单并校验 |
| T3 | 严重 | 全部 `scripts/` | 无测试、无类型检查、无 lint | 加 `pytest` 套件，CI 跑 `ruff` + `mypy` |
| T4 | 严重 | `simulations/requirements.txt` | 使用 `>=`，未来依赖会破坏可复现性 | 锁定精确版本，加 lockfile（`pip-compile` / `uv pip compile`） |
| T5 | 严重 | `tools/n_of_1/` | 无 `requirements.txt` | 加 pinned `requirements.txt` 并在 README 说明安装 |
| T6 | 严重 | `.github/workflows/deploy-pages.yml` | 部署前不跑审计脚本 | 在部署流程中加入 `audit_links.py`、`audit_nav_coverage.py`、`audit_math_delimiters.py` |
| T7 | 严重 | 仓库整体 | 无 `.gitattributes`，CRLF/LF 警告持续 | 加 `.gitattributes` 强制 LF |
| T8 | 中等 | `scripts/sync_docs.py` | `docs/` 镜像不会删除已移除的源文件；`docs/GLOSSARY.md` 被跟踪造成混淆 | 让 sync 先清空再复制；untrack `docs/GLOSSARY.md` 或改为从根目录动态生成 |
| T9 | 中等 | `scripts/audit_links.py` | 不检查锚点、图片/资产链接、外链 | 扩展支持锚点、资产、外链（带缓存） |
| T10 | 中等 | `scripts/audit_nav_coverage.py` | 正则解析 nav，可能漏掉带注释或引号的条目 | 用 YAML loader 或更严谨解析 |
| T11 | 中等 | `tools/n_of_1/scripts/l0_l7_radar.py` | CJK 字体回退缺少 macOS 字体 | 加入 `PingFang SC`、`Hiragino Sans GB` 等 |
| T12 | 中等 | `tools/n_of_1/schema.yaml` | 仅文档，未在脚本中加载校验 | 加校验模块，`log_entry.py` 与 `analyze.py` 共用 |
| T13 | 建议 | 根目录 | 无 `pyproject.toml` | 加最小 `pyproject.toml`，含元数据、可选依赖组、`ruff`/`mypy`/`pytest` 配置 |
| T14 | 建议 | `simulations/` | 输出 PNG/CSV 与源码混在一起 | 移到 `simulations/output/` 或 `assets/simulations/`，加 `.gitignore` |

---

## 4. 优先级与行动路线图

### 第一阶段：止血（1–3 天，提升可信度信号）

1. 修复 `AB(t)` 公式漂移（F1）。
2. 清理 badge 违规：F2、F3、F4。
3. 给所有绘图仿真脚本加 `matplotlib.use("Agg")`（T1）。
4. 加 `.gitattributes` 强制 LF（T7）。
5. 在 README 顶部加 “What this repo is / isn’t” 与 `verifiable_units/` vs `simulations/` 说明（N2、N3）。

### 第二阶段：补齐（1–2 周，让 VU 真正可验证）

6. 为 `VU-08/09/10` 补实验设计（F6）。
7. 翻译或隐藏 `VU-04–07` 英文 stub（F5）。
8. 锁定 `simulations/requirements.txt` 与 `tools/n_of_1/requirements.txt`（T4、T5）。
9. CI 跑全部仿真脚本（T2）。
10. 扩展 `audit_links.py` 与 `audit_nav_coverage.py`（T9、T10）。

### 第三阶段：工程化（2–4 周，建立可维护基础设施）

11. 加 `pytest` 测试矩阵，覆盖脚本与仿真（T3）。
12. 加 `ruff` + `mypy` + pre-commit（T3、T13）。
13. 部署流程加入全部审计脚本（T6）。
14. 加 `pyproject.toml` 与可选依赖组（T13）。
15. 完成 `GLOSSARY.en.md` 核心条目（N6）。

### 第四阶段：体验优化（持续）

16. 在 `POSITIONING.md` 增加 “CS/工程师速读路径”。
17. 为每个内容模块加标准页脚：上一页 / 下一页 / 回到项目图谱 / 对应 CLAIMS 条目。
18. 自动生成并维护公式索引。

---

## 5. 一句话总结

> 对 CS 读者来说，本项目的“硬核内容”已经存在，但“硬核工程包装”还差一口气。当前最高回报的投资不是继续写更多哲学，而是把符号、badge、VU 实验设计、英文翻译、CI 测试这五件事做到让逻辑控无法挑刺。

---

*报告生成：2026-06-14*  
*生成方式：探索子代理并行审查 + 父代理综合*
