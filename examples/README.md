# 可运行示例

本目录包含 `src/dao_science/` 工程接口的整合示例，帮助读者把「符号 → 代码 → 数据」的链路跑通。

## 示例列表

| 文件 | 说明 | 涉及模块 |
|---|---|---|
| `auditable_node_demo.py` | 波浪功率调度 + 硬件熔断器 + 可审计记忆 | `scheduler`、`hardware`、`experience` |

## 运行

```bash
pip install -e .
python examples/auditable_node_demo.py
```

> 这些示例是教学性质的脚本，不进入 `pytest` 测试套件。
