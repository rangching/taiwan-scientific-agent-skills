# Taiwan Scientific Agent Skills｜臺灣學術繁中科學 Agent Skills 庫

> 衍生自 [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)（MIT 授權，原作者 K-Dense Inc.）。
> 本庫為**臺灣學術界適用的繁體中文版**，採**中英雙語對照**：英文為主、繁中為輔，方便對照上游更新。
> Derived from K-Dense Scientific Agent Skills, localized for Taiwan academia (zh-Hant-TW / English).

[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE.md)
[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](plugin.json)

## 來源與致謝 Origin

* 上游：K-Dense Inc. Scientific Agent Skills（166 skills，v2.69.0），論文 arXiv:2609.00065，使用本庫請引用原論文，見 `CITATION.cff`。
* 其中 `docx`、`pdf`、`pptx`、`xlsx` 四個 skills 系借用 Anthropic 作品，各目錄內 `LICENSE.txt` 保持原樣。
* 本庫改作與臺灣新增內容同樣以 MIT 釋出。

## 版本對照 Version mapping

本庫各 release 對應的上游快照（upstream snapshot）：

| 本庫版本 | 上游版本 | 上游 commit | 上游日期 | 本次內容 |
| --- | --- | --- | --- | --- |
| v0.1.0-zh-Hant | v2.69.0 | `49c6e97` | 2026-09-21 | 骨架＋26 skills＋台灣新增 3 |
| v0.2.0-zh-Hant | v2.69.0 | `49c6e97` | 2026-09-21 | ＋30（累計 56） |
| v0.3.0-zh-Hant | v2.69.0 | `49c6e97` | 2026-09-21 | ＋30（累計 86） |
| v0.4.0-zh-Hant | v2.69.0 | `49c6e97` | 2026-09-21 | ＋30（累計 116） |
| v1.0.0-zh-Hant | v2.69.0 | `49c6e97` | 2026-09-21 | ＋50（166 全量） |
| v1.1.0-zh-Hant | v2.69.0 | `49c6e97` | 2026-09-21 | 完整 CI＋`description_zh` 遷入 metadata＋台灣第 4 skill |

* 各 skill 的 `metadata` 內有 `upstream: K-Dense-AI/scientific-agent-skills` 來源標記
 （`what-if-oracle` 因上游原有同名欄位，改記為 `zh-tw-upstream`），
  對照上表 commit 即可還原當時的上游原文。
* 上游更新頻繁，本庫按 `docs/上游同步.md` 每月同步一次；同步後此表會新增一列。
* 上游 repo：https://github.com/K-Dense-AI/scientific-agent-skills

## 內容 Contents（v1.1.0：上游 166 全量＋台灣新增 4＋完整 CI）

* `skills/`：上游 166 個全數收錄（完整複製＋繁中導讀＋`metadata.description_zh`）。
* `skills-tw/`：臺灣在地新增 4 個（見下）。
* `tests/`＋`.github/workflows/`：移植上游結構契約測試與 `skills-ref` 驗證 CI，
  每個 PR 自動檢查規格相容。
* `skills-tw/`：臺灣在地新增 4 個：
  * `nstc-grant-writing`：國科會專題研究計畫書架構與查核表
  * `tw-research-ethics`：人體研究法、個資法、IRB/REC 送審流程導引（僅流程輔助）
  * `tw-scholar-search`：Airiti 華藝、博碩士論文系統、國家圖書館檢索流程
  * `tw-compute-data`：TWCC、國網中心、校級 HPC 上機與 NHIRD 管制資料申請導引（僅流程輔助）

首批 26 個：database-lookup、paper-lookup、scientific-writing、citation-management、
exploratory-data-analysis、scientific-visualization、statsmodels、scikit-learn、
hypothesis-generation、experimental-design、scanpy、anndata、biopython、bioservices、
gget、pydeseq2、pysam、rdkit、deepchem、clinical-reports、research-grants、
peer-review、iso-standards-readiness、analytical-method-validation、
literature-review、statistical-analysis。

第二批 30 個（藥化＋影像＋臨床＋多體學）：datamol、diffdock、medchem、molfeat、
pytdc、molecular-dynamics、esm、pydicom、pathml、histolab、neurokit2、
paperclip、paperzilla、pyopenms、matchms、pathway-enrichment、torch-geometric、
pymc、networkx、matplotlib、seaborn、umap-learn、scvi-tools、scvelo、
cellxgene-census、arboreto、bulk-rnaseq、clinical-decision-support、
pkpd-modeling、primekg。

第三批 30 個（工程＋資料＋寫作）：polars、polars-bio、dask、vaex、nextflow、
zarr-python、tiledbvcf、lamindb、datalad、geopandas、astropy、sympy、qiskit、
cirq、pennylane、qutip、pytorch-lightning、transformers、shap、pyzotero、
markitdown、latex-posters、scientific-slides、infographics、
markdown-mermaid-writing、scientific-schematics、exa-search、open-notebook、
protocolsio-integration、opentrons-integration。

第四批 30 個（實驗室自動化＋方法＋基因體）：benchling-integration、
labarchive-integration、latchbio-integration、dnanexus-integration、
omero-integration、ginkgo-cloud-lab、pylabrobot、treatment-plans、
relsa-severity-assessment、what-if-oracle、scientific-brainstorming、
scientific-critical-thinking、scholar-evaluation、venue-templates、
statistical-power、bids、imaging-data-commons、depmap、onekgpd、
alphagenome、genomic-intelligence、pathogen-variant-surveillance、
genomic-coordinates、phylogenetics、scikit-bio、cobrapy、glycoengineering、
research-lookup、bgpt-paper-search、autoskill。

第五批 50 個（收尾全量）：adaptyv、aeon、arbor、consciousness-council、deepspot-m、
deeptools、dhdna-profiler、docx※、etetoolkit、flowio、fluidsim、
folklore-variant-evidence、generate-image、geniml、geomaster、get-available-resources、
gtars、hugging-science、hypogenic、lab-hardware-cad、liteparse、
market-research-reports、matlab、modal、ncats-arax、neuropixels-analysis、
ontology-term-resolution、openpiv、optimize-for-gpu、pacsomatic、parallel-web、
pdf※、pi-agent、pptx※、pptx-posters、pufferlib、pyhealth、pymatgen、pymoo、
rowan、scikit-survival、simpy、stable-baselines3、tamarind、timesfm-forecasting、
torchdrug、uncertainty-and-units、usfiscaldata、waypoint-bio、xlsx※。
（※為 Anthropic 借用作品，本體與 LICENSE.txt 原樣保留，僅加繁中導讀。）

詳見 `docs/skills.md`。

## 雙語規範 Bilingual convention

* frontmatter `description` 維持英文原文（確保 Agent 檢索相容），繁中摘要放在 `metadata.description_zh`。
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
