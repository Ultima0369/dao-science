# 项目概念图谱：导航 Project Dao.Science

## Project Concept Map: Navigating Project Dao.Science

---

本文档提供 Project Dao.Science 全部 22 个模块之间的概念依赖关系图，帮助读者找到适合自己兴趣的阅读路径。

```mermaid
flowchart TB
    subgraph "Layer 0: 动机与认知框架"
        WHY["为什么重要<br/>why_this_matters.md<br/>三重危机 + 四重收敛"]
        L0L7["L0-L7 频谱<br/>L0_L7_spectrum.md<br/>事实层次 + 认知地形图"]
    end
    
    subgraph "Layer 1: 第一性原理"
        DAO["道作为过程<br/>01_dao_as_process.md<br/>道 ≡ -∇G(π)<br/>预测编码梯度流"]
        ONE["一即带宽<br/>02_one_as_bandwidth.md<br/>AB(t)=Cmax−RDMN(t)"]
        MAP["相非物<br/>03_map_not_territory.md<br/>心智内容=万物之相"]
        PHIL["科学哲学<br/>04_philosophy_of_science.md<br/>L0-L7 元框架"]
    end
    
    subgraph "Layer 2: 心智模型"
        ATTN["注意力动力学<br/>attention_model.md<br/>α 参数收放自如"]
        AMYG["本能劫持<br/>100ms_model.md<br/>杏仁核-PFC 竞争"]
        NEURO["神经重塑回路<br/>neuroplasticity_loop.md<br/>理入→行入→Hebbian"]
        DMN["DMN-自我-内感受<br/>dmn_self_model.md<br/>吾丧我的神经三角"]
        SOCIAL["社会认知<br/>social_cognition.md<br/>镜像共鸣+同体大悲"]
    end
    
    subgraph "Layer 3: 实践方法"
        LIRU["理入<br/>li_ru.md<br/>见地建立<br/>下调叙事自我精度"]
        BAO["报冤行<br/>01_embrace_suffering.md<br/>认知重评+情感命名"]
        SUI["随缘行<br/>02_flow_with_causes.md<br/>奖励系统重新校准"]
        WU["无所求行<br/>03_seek_nothing.md<br/>Wanting vs Liking"]
        CHENG["称法行<br/>04_act_in_accordance.md<br/>降低 SoA+六度优化"]
    end
    
    subgraph "Layer 4: 应用"
        AI["AI 治理<br/>ai_governance.md<br/>知止不殆+主动停车"]
        JING["境教<br/>education_by_field.md<br/>环境设计作为教学法"]
        CLINICAL["临床心理健康<br/>clinical_mental_health.md<br/>四行↔CBT/ACT/MBCT"]
        CREATIVITY["创造力与创新<br/>creativity_innovation.md<br/>DMN-ECN 耦合+称法创造"]
        SYMBIOSIS["碳硅共生<br/>carbon_silicon_symbiosis.md<br/>生态位互补+被需要"]
    end
    
    %% Cross-layer dependencies
    WHY --> DAO
    L0L7 --> MAP
    L0L7 --> PHIL
    
    DAO --> ONE
    DAO --> MAP
    ONE --> ATTN
    MAP --> DMN
    PHIL --> AI
    
    ATTN --> AMYG
    AMYG --> NEURO
    DMN --> SOCIAL
    DMN --> LIRU
    
    LIRU --> BAO
    BAO --> SUI
    SUI --> WU
    WU --> CHENG
    
    CHENG --> AI
    CHENG --> CREATIVITY
    BAO --> CLINICAL
    SUI --> CLINICAL
    ATTN --> JING
    SOCIAL --> JING
    ONE --> SYMBIOSIS
    AI --> SYMBIOSIS
    
    style WHY fill:#fff9c4,stroke:#f9a825
    style L0L7 fill:#fff9c4,stroke:#f9a825
    style DAO fill:#e3f2fd,stroke:#1565c0
    style ONE fill:#e3f2fd,stroke:#1565c0
    style MAP fill:#e3f2fd,stroke:#1565c0
    style PHIL fill:#e3f2fd,stroke:#1565c0
    style ATTN fill:#fce4ec,stroke:#c62828
    style AMYG fill:#fce4ec,stroke:#c62828
    style NEURO fill:#fce4ec,stroke:#c62828
    style DMN fill:#fce4ec,stroke:#c62828
    style SOCIAL fill:#fce4ec,stroke:#c62828
    style LIRU fill:#f3e5f5,stroke:#6a1b9a
    style BAO fill:#f3e5f5,stroke:#6a1b9a
    style SUI fill:#f3e5f5,stroke:#6a1b9a
    style WU fill:#f3e5f5,stroke:#6a1b9a
    style CHENG fill:#f3e5f5,stroke:#6a1b9a
    style AI fill:#e8f5e9,stroke:#2e7d32
    style JING fill:#e8f5e9,stroke:#2e7d32
    style CLINICAL fill:#e8f5e9,stroke:#2e7d32
    style CREATIVITY fill:#e8f5e9,stroke:#2e7d32
    style SYMBIOSIS fill:#e8f5e9,stroke:#2e7d32
```

## 阅读路径

### 路径 1：理论优先（第一性原理驱动）
适合希望先建立完整理论框架的读者。

1. `0_motivation/why_this_matters.md` — 为什么这个项目重要
2. `0_motivation/L0_L7_spectrum.md` — 认知频谱框架
3. `1_first_principles/01_dao_as_process.md` — 道作为预测编码梯度流
4. `1_first_principles/02_one_as_bandwidth.md` — 一作为觉知带宽
5. `1_first_principles/03_map_not_territory.md` — 心智内容 = 表征 ≠ 实在
6. `1_first_principles/04_philosophy_of_science.md` — 科学知识的认知层级
7. → 然后进入 Layer 2（心智模型）

### 路径 2：实践优先（行入驱动）
适合希望直接开始实践的读者。

1. `3_methodology/li_ru.md` — 理入：建立正确的见地
2. `3_methodology/xing_ru/01_embrace_suffering.md` — 报冤行：拥抱苦难
3. `3_methodology/xing_ru/02_flow_with_causes.md` — 随缘行：随顺因缘
4. `3_methodology/xing_ru/03_seek_nothing.md` — 无所求行：停止执着
5. `3_methodology/xing_ru/04_act_in_accordance.md` — 称法行：与实相协调
6. → 回到 Layer 1 理解理论根基

### 路径 3：应用驱动
适合关注特定应用场景的读者。

- **AI 安全**：`4_applications/ai_governance.md` → `4_applications/carbon_silicon_symbiosis.md`
- **教育**：`4_applications/education_by_field.md` → `2_models/social_cognition.md`
- **心理健康**：`4_applications/clinical_mental_health.md` → `3_methodology/xing_ru/`
- **创造力**：`4_applications/creativity_innovation.md` → `2_models/attention_model.md`

### 路径 4：神经科学优先
适合神经科学背景的读者。

1. `2_models/attention_model.md` — 注意力动力学
2. `2_models/100ms_model.md` — 本能劫持与情绪调控
3. `2_models/neuroplasticity_loop.md` — 神经重塑的工程化描述
4. `2_models/dmn_self_model.md` — DMN-自我-内感受三角
5. `2_models/social_cognition.md` — 社会认知与镜像共鸣
6. → 然后进入 Layer 3 了解实践方法

## 学术预印本

|- 8 篇 LaTeX 预印本覆盖全部 22 个模块的核心内容。参见 `paper/README.md` 获取完整索引。

---

> 本文档是 Project Dao.Science 的导航入口。将本文档添加到 `mkdocs.yml` 的 nav 中作为首页可提供交互式导航。
