---
name: tw-compute-data
description: Navigate Taiwan academic computing and controlled data application flow including TWCC, NCHC, campus HPC onboarding and NHIRD/human database application checklists. Process guidance only. Use for compute planning and data application preparation.
license: MIT
metadata:
  description_zh: "臺灣運算與管制資料申請導引：TWCC、國網中心、校級 HPC 上機流程，健保資料庫與人體生物資料庫申請查核表，僅流程輔助。"
  version: "1.0"
  skill-author: taiwan-scientific-agent-skills
  zh-tw-added: "2026-09-28"
---

# 臺灣運算與管制資料申請導引 Taiwan Compute & Data

> **警語**：本 skill 僅為申請流程輔助。各平台計費、審查結果、資料釋出以 TWCC、國網中心、
> 各校計中、衛福部資料科學中心最新公告為準；管制資料之使用須經正式審查通過，
> 不得以本文件取代申請或審查。

## 繁中導讀 Zh-Hant Guide

### 何時使用

- 規劃論文、計畫的運算資源（GPU、HPC、大型記憶體）時，比較 TWCC、國網中心、校級 HPC。
- 準備健保資料庫（NHIRD）、人體生物資料庫等管制資料申請文件前自我檢查。

## 運算資源速覽（流程用）

| 來源 | 用途 |
| --- | --- |
| TWCC（台灣 AI 雲） | GPU 容器運算服務，適合深度學習訓練 |
| 國網中心 NCHC | 高速計算主機、儲存、科學計算諮詢 |
| 校級 HPC／計中 | 各校叢集電腦、排程系統（多採 SLURM），校內計費較優惠 |

### 上機查核表

- [ ] 估算資源：GPU 時數、CPU 核心數、記憶體、儲存、預估期程。
- [ ] 確認帳號身分別（計畫主持人、學生）與經費來源（計畫支應或自費）。
- [ ] 學會排程指令（sbatch／squeue／scancel）與模組載入（module load）。
- [ ] 程式先在小資料試跑，確認可重現再送大工作。
- [ ] 敏感資料不上傳公開雲，只用核可環境。

## 管制資料申請速覽（流程用）

| 來源 | 用途 |
| --- | --- |
| 健保資料庫 NHIRD | 去識別化健保申報資料，需經審查於核可環境分析 |
| 衛福部資料科學中心 | 跨資料庫串連加值應用，現場或遠端分析 |
| 人體生物資料庫 | 檢體與健康資料，需倫理審查與使用審查雙軌 |

### 申請查核表

- [ ] 研究計畫書、IRB／REC 核准文件備齊（見 `tw-research-ethics`）。
- [ ] 變項清單最小化：只申請分析必需欄位。
- [ ] 資料管理規劃：存取人員、儲存位置、保存年限、銷毀方式。
- [ ] 經費編列含資料使用費與分析人力。
- [ ] 發表前依規定送審查（部分資料庫要求發表前審閱）。

## 常見退件原因

變項超範圍、缺倫理核准、資料管理規劃空白、經費未編資料使用費。
