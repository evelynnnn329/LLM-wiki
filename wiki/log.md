# 知識庫演進日誌 (Changelog)

記錄知識庫所有的生命週期事件（Ingest、Query 沉澱、Lint 健康檢查）。每次操作皆會追加一筆記錄。

---

## [2026-11-21] init | 知識庫架構初始化
- 建立學術知識庫基礎目錄架構：`raw/paper/`、`wiki/papers/`、`wiki/concepts/`、`wiki/methods/`、`wiki/topics/`。
- 初始化 `wiki/index.md` 與 `wiki/log.md`。
- 配置專屬作業指引 `AGENTS.md`。

## [2026-11-22] ingest | 拖延心理學五大奠基與最新實證文獻
- 匯入五篇論文筆記：
  - [[2006 Steel & Konig - Integrating Theories of Motivation]]
  - [[2007 Steel - The Nature of Procrastination]]
  - [[2013 Sirois & Pychyl - Procrastination and the Priority of Short-Term Mood Regulation]]
  - [[2023 Salguero-Pazos & Reyes-de-Cozar - Interventions to Reduce Academic Procrastination]]
  - [[2024 Jochmann et al - Procrastination, Depression and Anxiety Symptoms in University Students]]
- 建立核心概念頁：[[Temporal Motivation Theory]], [[Short-Term Mood Regulation]], [[Present vs Future Self]], [[Procrastination-Health Model]], [[Irrational Delay]]
- 建立研究方法頁：[[Autoregressive Time-Lagged Panel Model]], [[Psychometric Meta-Analysis]], [[Academic Procrastination Interventions]]
- 建立主題綜述頁：[[Mechanisms of Procrastination - From Time Discounting to Mood Regulation and Health]]
- 同步更新 [[index]]。

## [2026-11-22] presentation | 為什麼我們總是拖到最後一刻？——拖延心理學與改善方法
- 依據 Wiki 封閉知識庫生成 11 頁完整教學簡報：`presentations/procrastination_self_help.html`
- 來源映射：[[2006 Steel & Konig - Integrating Theories of Motivation]], [[2007 Steel - The Nature of Procrastination]], [[2013 Sirois & Pychyl - Procrastination and the Priority of Short-Term Mood Regulation]], [[2023 Salguero-Pazos & Reyes-de-Cozar - Interventions to Reduce Academic Procrastination]], [[2024 Jochmann et al - Procrastination, Depression and Anxiety Symptoms in University Students]]
- 嚴格落實科學查核：區分相關性與因果關係、落實知覺壓力非中介之最新實證、嵌入自我覺察測驗。

## [2026-11-22] revision | 精修 HTML 教學簡報內容與科學查核
- 檔案：`presentations/procrastination_self_help.html`
- 重點調整：
  1. 第 1 頁降低學術詞彙門檻，貼近大專生語言。
  2. 第 2 頁核對 Steel (2007) 80%~95% 拖延盛行率原義，區分曾有拖延 vs 慢性困擾。
  3. 第 3 頁精簡非理性延遲與策略性延遲比較，避免過度絕對化表述。
  4. 第 4 頁修正完美主義（總體關聯微弱但他人期望型仍有 r=.18）與焦慮（衝動性中介）解釋，避免因果化。
  5. 第 5 頁 TMT 以圖解與情境為主，公式作補充，明確標註示意圖非實測數據。
  6. 第 6 頁簡化短期情緒調節為 4 步循環圖，減少冗餘術語。
  7. 第 7 頁由「診斷」調整為「情境分析」，保留互動反饋。
  8. 第 8 頁客觀表述 Jochmann (2024) 縱貫預測關聯，不直接宣稱因果證實，並嚴謹詮釋知覺壓力非中介之意涵。
  9. 第 9 頁澄清 Salguero-Pazos (2023) 百分比代表研究關注篇數佔比，非介入成功率。
  10. 第 10 頁清楚區分「論文直接支持之策略」與「理論衍生之生活建議」。
  11. 第 11 頁精簡總結，保留課後 3 分鐘微行動。
  12. 技術檢查：全面移除可能造成離線解析錯誤的 raw LaTeX，改以標準語意標籤呈現；加入 slide 內部捲軸與 flex-shrink 控制，確保在 1366x768 筆電螢幕不發生溢出。
