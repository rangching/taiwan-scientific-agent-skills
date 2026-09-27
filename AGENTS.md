# Repository Guidance（本庫工作指引）

本庫沿用上游 K-Dense Scientific Agent Skills 的結構與規範，另加臺灣繁中雙語層。
上游完整規範見上游 `AGENTS.md`；本檔只列**差異處**，衝突時以本檔為準。

## 目錄結構

```text
plugin.json                 # Agent Plugins manifest，name=taiwan-scientific-agent-skills
skills/<skill-name>/        # 上游移植，目錄名＝frontmatter name，不可改名
├── SKILL.md
├── references/ / scripts/ / assets/  # 原樣保留
skills-tw/<skill-name>/     # 臺灣新增，同樣遵循 Agent Skills 規格
docs/                       # 翻譯規範、上游同步、skills 索引
```

## 雙語規則（必守）

1. 不新增 top-level frontmatter 欄位以外的自創欄位？**例外**：允許 `description_zh`（繁中摘要字串）一個，
   其餘一律放 `metadata` 內。這是為了相容上游驗證器而做的最小擴充。
2. `description`（英文）一字不改；`description_zh` 一句話繁中摘要。
3. 內文開頭插入 `> 本 skill 衍生自上游 ...` 導讀區塊＋繁中「何時使用／快速開始」短導讀，
   原英文內文完整保留在後。
4. `metadata.version` 維持引號字串；移植時沿用上游版本，不重編。
5. 用詞用台灣用法：程式、軟體、透過、設定、預設、資料庫。技術名詞（function、API、model、prompt）維持英文。

## 新增 skills-tw 規則

* 範圍限臺灣學術在地：法規流程、計畫寫作、中文文獻、本地運算資源。
* 法規、醫療、審查相關必須含警語：僅流程輔助，不構成法律或臨床決策。
* 不得收錄 secrets、API keys、私人 URL。

## 驗證

```bash
python3 scripts/check_structure.py   # 本庫輕量結構檢查（檔名、frontmatter、連結）
```

上游完整驗證（`skills-ref validate`、pytest）待全量移植後再引入。
