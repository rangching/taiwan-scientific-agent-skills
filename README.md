# Taiwan Scientific Agent Skills｜臺灣學術繁中科學 Agent Skills 庫

> 衍生自 [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)（MIT 授權，原作者 K-Dense Inc.）。
> 本庫為**臺灣學術界適用的繁體中文版**，採**中英雙語對照**：英文為主、繁中為輔，方便對照上游更新。
> Derived from K-Dense Scientific Agent Skills, localized for Taiwan academia (zh-Hant-TW / English).

[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE.md)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](plugin.json)

## 來源與致謝 Origin

* 上游：K-Dense Inc. Scientific Agent Skills（166 skills，v2.69.0），論文 arXiv:2609.00065，使用本庫請引用原論文，見 `CITATION.cff`。
* 其中 `docx`、`pdf`、`pptx`、`xlsx` 四個 skills 系借用 Anthropic 作品，各目錄內 `LICENSE.txt` 保持原樣。
* 本庫改作與臺灣新增內容同樣以 MIT 釋出。

## 內容 Contents（v0.1.0：骨架＋首批）

* `skills/`：首批 24 個上游 skills（完整複製＋繁中導讀＋`description_zh`），其餘分批補齊至 166。
* `skills-tw/`：臺灣在地新增 3 個：
  * `nstc-grant-writing`：國科會專題研究計畫書架構與查核表
  * `tw-research-ethics`：人體研究法、個資法、IRB/REC 送審流程導引（僅流程輔助）
  * `tw-scholar-search`：Airiti 華藝、博碩士論文系統、國家圖書館檢索流程

首批 24 個：database-lookup、paper-lookup、scientific-writing、citation-management、
exploratory-data-analysis、scientific-visualization、statsmodels、scikit-learn、
hypothesis-generation、experimental-design、scanpy、anndata、biopython、bioservices、
gget、pydeseq2、pysam、rdkit、deepchem、clinical-reports、research-grants、
peer-review、iso-standards-readiness、analytical-method-validation。

詳見 `docs/skills.md`。

## 雙語規範 Bilingual convention

* frontmatter `description` 維持英文原文（確保 Agent 檢索相容），另加 `description_zh` 繁中摘要。
* 內文標題雙語並列，段落繁中在前、英文原文保留在後；指令、參數、變數名維持英文。
* 用詞見 `docs/翻譯規範.md`。

## 安裝使用 Usage

本庫維持 Agent Skills 開放標準＋Agent Plugins 封裝，可直接取用：

```bash
# 整庫複製（擇一）
git clone https://github.com/rangching/taiwan-scientific-agent-skills.git ~/.agents/skills/taiwan-scientific-agent-skills
# 或只取單一 skill
cp -r taiwan-scientific-agent-skills/skills/scanpy ~/.agents/skills/
```

支援 Cursor、Claude Code、Codex、Gemini CLI 等相容主機；`plugin.json` 可作為單一 plugin 載入。

## 免責聲明 Disclaimer

* Skills 可執行程式碼、存取網路，安裝前請先閱讀各 `SKILL.md`。
* 法規、臨床相關 skills（`tw-research-ethics`、`clinical-reports` 等）僅供研究流程輔助，
  不構成法律認定、診斷、治療或審查通過保證，正式送審以各校 IRB/REC、主管機關公告為準。

## 上游同步 Upstream sync

見 `docs/上游同步.md`，每月合併上游一次，英文段為準、繁中段標示待更新。

## 參與 Contributing

見 `CONTRIBUTING.md`，歡迎補翻譯、新增臺灣在地 skills。
