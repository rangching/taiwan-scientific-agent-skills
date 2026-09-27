# 參與貢獻 Contributing（繁體中文）

## 歡迎的貢獻

* 繁中翻譯校對（錯字、台灣用詞、雙語格式）
* 補齊上游 skills 移植（照批次認領）
* 新增 `skills-tw/` 臺灣在地 skills（法規、計畫寫作、中文文獻、本地運算資源）

## 流程

1. 一個 skill 一個 PR（或一個批次一個 PR，先開 issue 認領）。
2. 移植 PR 必須：目錄原樣複製、`description` 不動、`metadata.description_zh` 加繁中摘要、加繁中導讀區塊。
3. 新增 skills-tw 必須：目錄名＝frontmatter `name`、`metadata.version` 從 `"1.0"` 開始、含警語（如涉及法規醫療）。
4. 跑過 `python3 scripts/check_structure.py` 再送 PR。

## 不接受

* 改動上游 `scripts/`、`references/` 程式邏輯（除非修正錯誤並註明）。
* 刪除英文原文只留中文。
* 含 secrets、API keys、私人資料。
