# 一致性修复日志 / Consistency Fix Log

> 时间：2026-06-13  
> 范围：CLAIMS 登记册 ↔ 可验证单元（VU）双向链接、证据徽章 `[S]` 一致性  
> 状态：已修复并通过构建与审计脚本验证

---

## 1. 审计发现

### 1.1 VU-01/02/03 未写入「对应主张」

| VU | 主题 | 对应主张 | 备注 |
|---|---|---|---|
| VU-01 | DMN-岛叶双稳态切换 | **C07** | `2_models/dmn_self_model.md` 已关联，但 VU 头部缺少反向链接 |
| VU-02 | 杏仁核-前额叶竞争窗口 | **C06** | `2_models/100ms_model.md` 已关联，但 VU 头部缺少反向链接 |
| VU-03 | DMN-ECN 动态耦合与顿悟 | **C25（新增）** | 此前无专门主张承接该仿真单元 |

### 1.2 主张证据徽章缺少 `[S]`

多个主张已链接到带 Python 仿真的 VU，但 `证据徽章` 未包含 **仿真 [S]**：

| 主张 | 关联 VU | 修复前徽章 | 修复后徽章 |
|---|---|---|---|
| C05 注意力=精度优化 | VU-05 | F + N + B | **F + S + N + B** |
| C07 DMN 下调释放觉知带宽 | VU-01 | F + N + B | **F + S + N + B** |
| C10 涌现 ≠ 相变 | VU-04 | F + M | **F + S + M** |
| C15 AI 需要知止协议 | VU-06 | F + M | **F + S + M** |
| C18 碳硅生态位互补 | VU-07 | F + M | **F + S + M** |

C06、C21、C23、C24 此前已正确包含 `[S]`，未改动。

---

## 2. 修复内容

### 2.1 新增主张 C25（中英同步）

- **中文**：`C25：创造力源于 DMN-ECN 动态耦合`
- **英文**：`C25: Creativity Arises from Dynamic DMN-ECN Coupling`
- **徽章**：`F + S + N + B`
- **可信度**：中-高
- **关联文件**：
  - `4_applications/creativity_innovation.md`
  - `verifiable_units/vu_03_dmn_ecn.md`
- **位置**：在 `CLAIMS.md` / `CLAIMS.en.md` 的「应用层」C24 之后、「方法论层」之前插入；同时在总览汇总表中追加一行。

### 2.2 补全 VU 头部「对应主张」字段

- `verifiable_units/vu_01_dmn_insula.md`：增加 `> **对应主张**：`CLAIMS.md` C07`
- `verifiable_units/vu_02_amygdala_pfc.md`：增加 `> **对应主张**：`CLAIMS.md` C06`
- `verifiable_units/vu_03_dmn_ecn.md`：增加 `> **对应主张**：`CLAIMS.md` C25`

### 2.3 更新 CLAIMS 证据徽章与汇总表

- `CLAIMS.md`：C05/C07/C10/C15/C18 的详情区徽章与总览表同步加入 `[S]`；新增 C25 详情区与汇总表行。
- `CLAIMS.en.md`：与中文版保持徽章、主张编号、汇总表顺序完全一致。

---

## 3. 验证结果

### 3.1 既有审计脚本

```bash
python scripts/audit_links.py          # No broken internal .md links
python scripts/audit_math_delimiters.py # No obvious unmatched inline math
python scripts/audit_nav_coverage.py    # All .md files referenced in nav
mkdocs build --strict                   # Build succeeded
```

### 3.2 VU ↔ CLAIM 双向一致性脚本

自定义检查确认：

- 全部 10 个 VU（VU-01 至 VU-10）均已写入 `对应主张`；
- 每个带仿真脚本的 VU，其对应主张的证据徽章均包含 `[S]`；
- 每个主张关联文件中的 VU 路径均存在，且仿真状态与徽章一致；
- 中英 `CLAIMS` 登记册的主张数量、徽章、汇总表 ID 顺序完全一致（25 条）。

### 3.3 额外检查

- 所有 VU 引用的 `simulations/*.py` 脚本均存在；
- 每个 VU 都有对应的 `.en.md` stub 文件；
- 所有 VU 已加入 `mkdocs.yml` 导航。

---

## 4. 剩余事项

以下问题在本次一致性修复中**未处理**，建议后续跟进：

1. **英文内容 stub 大量存在**：仅核心模块与新增 VU 有完整英译，早期 VU 与部分应用文件仍为 stub。
2. **`mkdocs-static-i18n` DeprecationWarning**：`Theme._vars` 访问警告，非阻塞，但建议在插件更新后跟进。
3. **CRLF/LF 警告**：Git 持续提示行尾符转换，不影响构建，可统一配置 `.gitattributes`。
4. **C25 的英文 VU stub**：`vu_03_dmn_ecn.en.md` 仍为翻译中提示，待完整翻译后同步元数据。

---

## 5. 修改文件清单

```text
CLAIMS.md
CLAIMS.en.md
verifiable_units/vu_01_dmn_insula.md
verifiable_units/vu_02_amygdala_pfc.md
verifiable_units/vu_03_dmn_ecn.md
AUDIT_FIX_LOG_2026-06-13.md
```

---

> 本日志由一致性修复工具链生成，作为 `AUDIT_REPORT_2026-06-13.md` 的后续行动记录。
