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
├── POSITIONING.md                      # 道科学是什么：定位声明
├── FINAL_VISION.md                     # 最终愿景：在复杂面前保持鲜活
├── README.md                           # 项目愿景、核心公理、快速入门
├── CONTRIBUTING.md                     # 本文件
├── GLOSSARY.md                         # 概念索引与术语表
├── NOTATION.md                         # 符号约定与证据等级
├── mkdocs.yml                          # MkDocs Material 配置 + 导航树
├── requirements.txt                    # Python 依赖
│
├── 0_motivation/                       # 动机层
├── 1_first_principles/                 # 第一性原理
├── 2_models/                           # 心智模型
├── 3_methodology/                      # 实践方法
├── 4_applications/                     # 应用层
├── verifiable_units/                   # 可验证单元（形式化 + 模拟 + 协议）
├── simulations/                        # Python 可运行模拟脚本
├── scripts/                            # 文档同步、审计、CI 辅助脚本
├── paper/                              # 学术预印本（LaTeX）
└── .github/workflows/                  # CI/CD
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

### 最小作用量编辑原则

项目遵循 `POSITIONING.md` 中的最小作用量原理：每个贡献都应减少理解整个项目所需的总认知作用量。

- 新增概念必须有不可替代的功能；
- 新增方程必须消除歧义，而非制造迷惑；
- 新增模块必须能回链到核心框架（道、一、地图非疆域、L0-L7、涌现、偏离代价）；
- 中英翻译请遵循 [`TRANSLATION.md`](TRANSLATION.md) 中的不可译词汇原则；
- 新增应用必须包含滥用风险与反制设计；
- 如果删除某段文字后不影响理解，优先考虑删除。

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
