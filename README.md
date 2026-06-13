# Project Dao.Science

[![CI Checks](https://github.com/Ultima0369/dao-science/actions/workflows/ci-checks.yml/badge.svg)](https://github.com/Ultima0369/dao-science/actions/workflows/ci-checks.yml)
[![Deploy MkDocs to GitHub Pages](https://github.com/Ultima0369/dao-science/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Ultima0369/dao-science/actions/workflows/deploy-pages.yml)
[![Site](https://img.shields.io/badge/site-ultima0369.github.io%2Fdao--science-blue)](https://ultima0369.github.io/dao-science/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Ultima0369/dao-science/blob/main/LICENSE)

> **在有限算力下，面对无限复杂的世界，保持鲜活、持续探索、把握灵感。**

**在线阅读**：https://ultima0369.github.io/dao-science/

---

## 一句话定位

道科学不是反科学，也不是超科学，而是一套**关于“如何优化观察者本身”的开源心智操作系统手册**——把东方第一人称心性实践，与预测编码、神经科学、主动推理对齐成可检验的技术语言。

完整定位见 [`POSITIONING.md`](POSITIONING.md)。

---

## 这手册写给谁？

| 你可能是 | 这里能帮你解决什么 |
|---|---|
| 研究者 | 在概念卡壳时，切换“紧/松”状态以突破瓶颈 |
| 决策者 | 在多方冲突中，保持大小尺度灵活切换 |
| 工程师 | 在复杂系统中，重新连接到“灵感涌现”的源头 |
| AI 从业者 | 把“知止”编译成可运行的安全约束 |
| 心理健康从业者 | 用神经科学语言理解僵化、劫持与恢复 |
| 普通探索者 | 在恐惧与欲望轮番劫持时，找到一条走得通的路 |

---

## 核心公理（一句话版）

| 概念 | 技术表达 | 含义 |
|---|---|---|
| **道** | `π_顺道 = argmin_π G(π)` | 意识-行动系统的最小预期自由能方向 |
| **一** | `AB(t) = 1 - [R_DMN(t) - R_0]/[R_max - R_0]` | 觉知带宽：DMN 抑制所释放的认知资源 |
| **相非物** | `P(世界\|心智) ≠ 世界` | 心智内容是万物之相，不是万物全部 |
| **L0-L7** | 认知地形频谱 | 从物自体到关系坍缩的七层事实结构 |
| **涌现** | `G(系统) ≠ ΣG(部分)` | 层级跃迁产生不可还原的新性质 |
| **偏离代价** | `Cost(π_dev) = G(π_actual) - G(π_opt)` | 偏离道的可量化预警信号 |

---

## 双螺旋架构

| 螺旋 | 形式 | 用途 | 入口 |
|---|---|---|---|
| **GitHub 仓库** | Markdown + Mermaid + Python 模拟 | 可执行、可修改的技术手册 | 本页 |
| **学术预印本** | LaTeX → PDF | 可引用、可同行评议的论文 | [`paper/README.md`](https://github.com/Ultima0369/dao-science/blob/main/paper/README.md) |
| **MkDocs 站点** | 在线渲染 | 最舒适的阅读体验 | [在线阅读](https://ultima0369.github.io/dao-science/) |

---

## 推荐阅读路径

| 目标 | 起点 | 预计时间 |
|---|---|---|
| 想知道“为什么需要这个项目” | [`0_motivation/why_this_matters.md`](0_motivation/why_this_matters.md) | 15 min |
| 想从第一人称经验进入 | [`0_motivation/cognition_in_progress.md`](0_motivation/cognition_in_progress.md) | 10 min |
| 想建立认知框架 | [`0_motivation/L0_L7_spectrum.md`](0_motivation/L0_L7_spectrum.md) | 20 min |
| 想看形式化定义 | [`1_first_principles/01_dao_as_process.md`](1_first_principles/01_dao_as_process.md) | 25 min |
| 想看可运行模拟 | [`verifiable_units/vu_01_dmn_insula.md`](verifiable_units/vu_01_dmn_insula.md) | 30 min |
| 想查术语 | [`GLOSSARY.md`](GLOSSARY.md) | 按需 |

---

## 项目结构

```
dao-science/
├── POSITIONING.md              # 定位声明
├── FINAL_VISION.md             # 最终愿景
├── README.md                   # 本文件
├── 0_motivation/               # 动机与认知框架
├── 1_first_principles/         # 第一性原理
├── 2_models/                   # 心智模型
├── 3_methodology/              # 实践方法（理入 + 行入）
├── 4_applications/             # 应用（AI、教育、临床、创造、碳硅共生）
├── verifiable_units/           # 可验证单元：形式化 + 模拟 + 协议
├── simulations/                # Python 可运行模拟脚本
├── paper/                      # 8 篇 LaTeX 学术预印本
├── scripts/                    # 文档同步、审计、CI 辅助脚本
├── GLOSSARY.md                 # 术语表
├── NOTATION.md                 # 符号与证据等级
└── CONTRIBUTING.md             # 贡献指南
```

---

## 本地构建

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 同步 docs/ 镜像
python scripts/sync_docs.py

# 3. 严格模式构建站点
mkdocs build --strict

# 4. 本地预览
mkdocs serve
```

CI 还会自动运行：链接审计、数学分隔符审计、导航覆盖审计、Python 模拟脚本。

---

## 证据等级

本项目使用 `F/S/B/N/M` 徽章标注每个主张的证据状态，避免把形式化误认为证据：

- **F**ormal：形式化定义
- **S**imulation：可运行模拟
- **B**ehavioral：行为/现象学证据
- **N**euroscience：神经科学证据
- **M**athematical：数学证明

详见 [`NOTATION.md`](NOTATION.md)。

---

## 关键数字

- **26** 个核心内容模块
- **3** 个可验证单元（含 Python 模拟）
- **8** 篇 LaTeX 学术预印本
- **~8,500** 行学术内容
- **100+** 条学术参考文献
- **30+** 个数学方程/形式化定义
- **17+** 个 Mermaid 流程图

---

## 参与贡献

- 发现问题：开 [Issue](https://github.com/Ultima0369/dao-science/issues)
- 提交改进：发 [Pull Request](https://github.com/Ultima0369/dao-science/pulls)
- 贡献规范：[`CONTRIBUTING.md`](CONTRIBUTING.md)

本仓库遵循 [MIT 协议](https://github.com/Ultima0369/dao-science/blob/main/LICENSE)。
