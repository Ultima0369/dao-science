# 贡献指南

## 分支策略
- `main`: 仅允许从 `develop` 合并，受保护。push 到 main 自动触发 GitHub Pages 部署。
- `develop`: 集成分支，日常开发在此
- `feature/<名称>`: 新功能或新模块
- `doc/<名称>`: 纯文档修改
- `paper/<名称>`: 预印本相关

## 提交规范
遵循 Conventional Commits: `type(scope): description`
类型：feat, fix, docs, refactor, chore, paper

## 核心纪律
1. 所有内容需有科学与经典双重依据。
2. 第一人称实证案例必须匿名化。
3. 欢迎 pull request，但必须经过核心维护者审核。

## 项目文件结构

```
dao-science/
├── POSITIONING.md                      # 道科学是什么：定位声明（建议作为第一个阅读文件）
├── FINAL_VISION.md                      # 最终愿景：在复杂面前保持鲜活
├── README.md                          # 项目愿景、核心公理、快速入门
├── CONTRIBUTING.md                    # 本文件
├── mkdocs.yml                         # MkDocs Material 配置 + 导航树
├── requirements.txt                   # Python 依赖（mkdocs-material）
│
├── 0_motivation/                      # 动机层——为什么这个项目重要
│   ├── why_this_matters.md            # 三大危机 + 四方汇聚论证
│   ├── L0_L7_spectrum.md              # L0-L7 事实与关系频谱框架
│   ├── project_map.md                 # 概念地图与阅读路径
│   └── objections_and_replies.md      # 反驳与回应——六项核心挑战
│
├── 1_first_principles/                # 第一性原理——数学/计算形式化
│   ├── 01_dao_as_process.md           # 道 ≡ -∇G(π)，21 个方程
│   ├── 02_one_as_bandwidth.md         # 一 = 觉知带宽 AB(t)
│   ├── 03_map_not_territory.md        # 相非物——五传统汇聚综述
│   └── 04_philosophy_of_science.md    # 科学知识的认知层级——L0-L7 嵌套
│
├── 2_models/                          # 心智模型——神经/认知机制
│   ├── attention_model.md             # 注意力动力学，α 参数
│   ├── 100ms_model.md                 # LeDoux 双通路 + 杏仁核劫持
│   ├── neuroplasticity_loop.md        # Hebbian/LTP/STDP + 后训练
│   ├── dmn_self_model.md             # DMN-自我-内感受神经三角
│   ├── social_cognition.md            # 社会认知与镜像共鸣
│   └── hypoxia_fifty_demons.md        # 缺氧与五十阴魔——禅修幻觉的神经生理学
│
├── 3_methodology/                     # 实践方法——达摩二入四行
│   ├── li_ru.md                       # 理入——见地建立（认知重构）
│   └── xing_ru/
│       ├── 01_embrace_suffering.md    # 报冤行——拥抱苦难
│       ├── 02_flow_with_causes.md     # 随缘行——与因缘流动
│       ├── 03_seek_nothing.md         # 无所求行——停止执着
│       └── 04_act_in_accordance.md    # 称法行——与实相协调的行动
│
├── 4_applications/                    # 应用层——跨领域实践
│   ├── ai_governance.md               # AI 治理——"知止不殆"
│   ├── education_by_field.md          # 境教——环境设计作为教学法
│   ├── clinical_mental_health.md      # 四行在临床心理健康中的应用
│   ├── creativity_innovation.md       # 无为的创造——创造力与顿悟
│   └── carbon_silicon_symbiosis.md    # 碳硅共生——从"它"到"祂"
│
├── paper/                             # 学术预印本（LaTeX）
│   ├── preprint_1/main.tex            # 道作为过程——预测编码框架
│   ├── preprint_2/main.tex            # L0-L7 事实与关系频谱
│   ├── preprint_3/main.tex            # DMN-自我-内感受三角
│   ├── preprint_4/main.tex            # 科学知识的认知层级
│   ├── preprint_5/main.tex            # 社会认知与镜像共鸣
│   ├── preprint_6/main.tex            # 创造力与创新
│   ├── preprint_7/main.tex            # 碳硅共生
│   └── preprint_8/main.tex            # 境教
│
├── .github/workflows/                 # CI/CD
│   └── deploy-pages.yml              # Push main → 构建并部署 MkDocs
│
├── GLOSSARY.md                        # 概念索引与术语表
└── 对话记录.md                        # 源对话记录（碳硅协作原始数据）
```

## 如何贡献

### 新增内容模块
1. 确定模块应属于哪个层级（动机/第一性原理/心智模型/实践方法/应用）
2. 遵循现有模块的格式：
   - 中英双语标题和摘要
   - 5-10 个关键词（中英双语）
   - 正文（中英混排，关键概念保留中文原文 + 英文翻译）
   - 完整的 DOI 引用
   - 与 L0-L7 频谱的交叉引用段落
   - 相关模块的导航链接
3. 更新 `mkdocs.yml` 的导航树
4. 如果是新模型或新方法论，确保在相关模块中添加双向交叉引用

### 修改现有内容
1. 在相应分支上提交 PR
2. 在 PR 描述中说明修改的科学或经典依据
3. 如修改核心命题，必须在第一性原理层提供论证

### 构建预印本
```bash
cd paper/preprint_1  # 或 preprint_2
pdflatex main.tex
bibtex main          # 如果有 .bib 文件
pdflatex main.tex
pdflatex main.tex    # 两次以解析交叉引用
```

### 本地预览 MkDocs
```bash
pip install -r requirements.txt
mkdocs serve
# 访问 http://127.0.0.1:8000
```

## 内容标准

### 引用格式
- **期刊论文**：作者 (年). 标题. *期刊*, *卷*(期), 页码. doi:DOI
- **书籍**：作者 (年). *书名*. 出版社.
- **经典文本**：传统作者 (约世纪). *文本名*. （注疏参考）

### 数学形式化
- 使用 LaTeX 数学模式：`$inline$`、`$$block$$`
- 所有符号首次出现时需定义
- 方程应有编号

### 交叉引用
- 引用项目内模块使用相对路径：`` `path/to/file.md` ``
- 每个文件必须包含与 L0-L7 频谱的关联段落
- 页脚导航应链接前一篇/后一篇相关模块
