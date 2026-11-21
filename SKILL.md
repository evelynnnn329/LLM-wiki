---
name: procrastination-wiki-presentation-loop
description: >
  根據「拖延症自救研究所」LLM Wiki 的封閉知識庫，
  生成 8–15 頁手繪筆記風 HTML 教學簡報，並透過
  程式化檢查 + AI 審查的三輪 Loop 保證品質與學術嚴謹性。
version: "1.0"
created: "2026-11-22"
project: "拖延症自救研究所"
---

# SKILL.md — HTML 簡報生成 Loop 規格書
## Procrastination Wiki → HTML Presentation Loop

> **設計原則**：本 Loop 由實際修改經驗歸納，聚焦於「可重複執行、可追溯錯誤、不虛構執行結果」。
> 每一輪必須如實記錄，不得聲稱執行了未真正進行的步驟。

---

## 1. 目標（Goal）

| 項目 | 規格 |
|:--|:--|
| **輸入** | 使用者指定的教學主題（需已有 Wiki 知識覆蓋） |
| **輸出** | 8–15 頁 HTML 教學簡報，存放於 `presentations/` |
| **知識邊界** | 100% 封閉於現有 `wiki/` 內容，嚴禁使用外部搜尋或模型自身訓練知識 |
| **視覺風格** | 保持手繪筆記風（奶油色背景、粉彩卡片、黑線框、圓角） |
| **目標受眾** | 大學生；語言：繁體中文，術語保留英文 |
| **最多輪次** | 3 輪（含初始生成） |

---

## 2. Loop 整體流程

```
使用者輸入主題
      │
      ▼
Phase 0: Wiki 知識可行性評估
      │  ─── 知識不足 ───▶ 告知邊界，停止
      │
      ▼
Phase 1: 規劃大綱（大綱確認後才生成 HTML）
      │  ─── 使用者修改大綱 ─▶ 重新規劃
      │  ─── 使用者確認 ──────▶
      │
      ▼
Phase 2: 生成 HTML 草稿
      │
      ▼
Phase 3: 程式化檢查（自動）
      │
      ▼
Phase 4: AI 審查（人工）
      │
      ├── 有問題 ─▶ 生成問題清單 ─▶ 局部修正
      │                │
      │                └─▶ 重回 Phase 3（最多 3 輪）
      │
      └── 無問題或已達 3 輪
            │
            ▼
      Phase 5: 交付 + 更新 wiki/log.md
```

---

## 3. 各 Phase 詳細規格

### Phase 0｜Wiki 知識可行性評估

**輸入**：使用者的教學主題
**操作**：
1. 閱讀 `wiki/index.md` 確認有無相關論文頁、概念頁、主題頁。
2. 評估是否能覆蓋至少 5 個不同的教學重點。

**停止條件（知識不足）**：
- Wiki 完全沒有該主題的論文頁。
- 有論文頁但數據不足以支撐 8 頁以上的獨立教學內容。

**輸出**：「可執行」或「知識不足，列出具體缺口」

---

### Phase 1｜規劃大綱

**輸入**：通過 Phase 0 的主題
**操作**：
1. 以結構化表格列出每頁：頁碼、標題、核心教學目標（1 句話）、對應 Wiki 來源。
2. **呈現給使用者確認，使用者核可後才進入 Phase 2**。

**大綱表格格式**（範本）：

| 頁 | 標題 | 教學目標 | Wiki 來源 |
|:--|:--|:--|:--|
| 1 | 封面 | 揭示主題全貌 | — |
| 2 | … | … | papers/... |

**停止條件**：使用者確認大綱，或明確表示放棄。

---

### Phase 2｜生成 HTML 草稿

**輸入**：已確認的大綱
**技術規格**：
- 單一 HTML5 檔案，完全離線可用（無外部 CDN）
- 瀏覽器翻頁：← → 鍵盤、按鈕、Space 鍵
- 頁碼顯示：`Slide X / N`
- 視覺：繼承現有 CSS 變數（`--bg-color`, `--pastel-*`, `--ink-color`）
- 每頁含：分類標籤（slide-category）、標題（slide-title）、文獻來源（source-tag）

**禁止**：
- 使用 raw LaTeX（`$...$`）——改用語意標籤或 Unicode
- Markdown 語法殘留（`**粗體**`、`[[連結]]`）
- 外部字型或圖片 CDN

**輸出**：`presentations/<主題名>.html`

---

### Phase 3｜程式化檢查（Programmatic Checks）

**執行工具**：`scripts/check_presentation.py <html檔案路徑>`

| 編號 | 檢查項目 | 通過條件 |
|:--|:--|:--|
| C1 | HTML 可解析 | HTMLParser 無例外 |
| C2 | 投影片數量 | 8 ≤ n ≤ 15 |
| C3 | 每頁有標題 | 所有 `slide-title` 非空 |
| C4 | 每頁有文獻來源 | 所有頁含 `.source-tag` |
| C5 | 每頁有教學內容 | 超過 10 字的非標題文字 |
| C6 | 翻頁按鈕存在 | `prevBtn`、`nextBtn` ID |
| C7 | 鍵盤操作實作 | `ArrowRight`、`ArrowLeft` |
| C8 | 互動功能存在 | `showScenarioAnalysis` 函式（若簡報含互動頁） |
| C9 | 無 Markdown 粗體 | body 中無 `**...**` |
| C10 | 無 Wiki 連結語法 | HTML 中無 `[[...]]` |
| C11 | 圖表非實測標注 | 含「非真實受試者」或「概念曲線」等字串 |
| C12 | Ground Truth 數字存在 | 核心效應值均出現（見數字清單） |
| C13 | 16:9 版面適配 | headless Edge 測試：scrollHeight ≤ clientHeight |
| C14 | 無外部 CDN | 無 cdn. / googleapis 等網址 |

**核心數字 Ground Truth 清單**（來源：Wiki 論文頁）：

| 數值 | 意義 | Wiki 來源 |
|:--|:--|:--|
| ρ = -0.75 | 盡責性與拖延 | Steel (2007) 表2 |
| ρ = -0.73 | 自我控制與拖延 | Steel (2007) 表3 |
| ρ = 0.52 | 衝動性與拖延 | Steel (2007) 表2 |
| ρ = 0.44 | 任務厭惡感與拖延 | Steel (2007) 表4 |
| ρ = -0.04 | 完美主義（總體） | Steel (2007) 表5 |
| ρ = 0.28 | 神經質與拖延 | Steel (2007) 表2 |
| β = 0.16 | 拖延預測憂鬱焦慮 | Jochmann et al. (2024) |
| 90.6% | 自我調節介入研究比例 | Salguero-Pazos (2023) 表4 |
| 28.1% | 自我效能介入研究比例 | Salguero-Pazos (2023) 表4 |
| 3.1% | 焦慮介入研究比例 | Salguero-Pazos (2023) 表4 |
| n = 392 | Jochmann 有效樣本數 | Jochmann et al. (2024) §Methods |

**輸出**：終端機報告 + `presentations/check_report.json`

---

### Phase 4｜AI 審查（人工核查清單）

> 程式無法自動判斷以下項目，需人工對照 Wiki 核查。

| 編號 | 類別 | 審查規則 | 操作指引 |
|:--|:--|:--|:--|
| A1 | 科學嚴謹性 | 未將 ρ / r 誤寫為因果 | 確認含效應值的句子用「相關」「預測」而非「導致」「証實」 |
| A2 | 科學嚴謹性 | 未過度推論研究結論 | 重點確認 Jochmann 2024 β=0.16：縱貫統計預測，非 RCT 因果 |
| A3 | 數據核對 | 研究數字與 Wiki 吻合 | 核對所有百分比、效應值與 wiki/papers/*.md |
| A4 | 數據核對 | Salguero 百分比明確澄清為篇數比例，非成功率 | 確認第 9 頁有「非有效率」等澄清文字 |
| A5 | 知識邊界 | 未加入 Wiki 未記載的研究 | 所有引用可在 wiki/ 找到對應條目 |
| A6 | 教學品質 | 術語有中文解釋或生活舉例 | 確認 Hyperbolic Discounting、Giving in to feel good 等有在地化說明 |
| A7 | 教學品質 | TMT 偏好逆轉點位於曲線交會處 | 以 Python bezier 計算驗算 SVG circle 的 cx/cy 是否在交點上（±1px 容差） |
| A8 | 教學品質 | 第 6 頁 Step 2 符合短期情緒調節理論 | 確認文字反映「Giving in to feel good」機制，非舊版「自制力耗損」 |
| A9 | 格式規範 | 第 10 頁區分文獻歸納 vs 理論推導 | 確認兩格卡片標題有明確區分標示 |
| A10 | 格式規範 | source-tag 採學術引用格式 | 確認格式為「作者 (年份)」，不含 `[[...]]` |

---

### Phase 5｜交付與日誌更新

**操作**：
1. 確認 HTML 已存於 `presentations/<主題名>.html`。
2. 在 `wiki/log.md` 追加記錄：
   ```markdown
   ## [YYYY-MM-DD] presentation | <主題名>
   - 生成簡報：presentations/<主題名>.html
   - 執行輪次：X 輪
   - 程式化通過率：14/14
   - AI 審查狀態：人工核查完成 / 尚待核查
   - 剩餘問題：（若有）
   ```

---

## 4. 修正規則（Loop 迭代）

### 4.1 問題清單格式

每輪發現問題後，輸出以下格式再執行修正：

```
【問題清單 — 第 X 輪】
頁碼：Slide N
類別：程式化 / AI審查 / 科學嚴謹性 / 格式
問題描述：（具體說明）
修正建議：（具體操作）
```

### 4.2 局部修正原則

- **只修改問題清單中指出的位置**，不重新生成整份簡報。
- **保留**：已通過的頁面、CSS 風格、翻頁 JS、互動功能。
- 修正後必須重新執行 Phase 3 + Phase 4。

### 4.3 停止條件

| 條件 | 行動 |
|:--|:--|
| 所有 C1–C14 通過 + AI 審查無疑慮 | 立即停止，進入 Phase 5 |
| 已完成 3 輪（含初始生成） | 停止，列出剩餘未解決問題 |
| Wiki 不支援某個數據或推論 | 刪除或改為保守表述，不得捏造 |
| 使用者明確要求停止 | 立即停止 |

---

## 5. 歷史錯誤模式（由實際修改經驗整理）

> 以下為本專案曾實際遭遇的問題，已納入 C 與 A 規則：

| 頁碼 | 錯誤類型 | 根本原因 | 對應規則 |
|:--|:--|:--|:--|
| Slide 4 | 完美主義 ρ=-0.04 被描述成「完美主義導致拖延」 | 混淆相關與因果 | A1、A2 |
| Slide 5 | TMT 偏好逆轉點的 SVG circle 未在曲線交點 | 未驗算貝茲曲線交叉座標 | A7 |
| Slide 6 | Step 2 寫「自制力耗損」而非情緒調節機制 | 未對照 Sirois & Pychyl (2013) 文字 | A8 |
| Slide 8 | Jochmann β=0.16 被描述為「已証實拖延導致憂鬱」 | 誤將統計預測等同因果 | A1、A2 |
| Slide 8 | `**未呈現統計上的顯著中介效果**` Markdown 語法殘留 | 直接將 Wiki md 語法複製貼入 HTML | C9 |
| Slide 9 | 90.6% 被描述成「時間管理有效率 90.6%」 | 未理解研究設計（篇數比例 ≠ 成功率） | A4 |
| Slide 10 | 自我同情介入效果被寫成「研究证實」 | 未區分文獻歸納 vs 理論推導建議 | A9 |
| 全頁 | source-tag 保留 `[[2007 Steel...]]` 語法 | 忘記將 Obsidian 連結轉換為學術格式 | A10、C10 |
| 全頁 | 文字在 1366×768 螢幕溢出 | slide max-height 設定錯誤 | C13 |

---

## 6. 目錄結構

```text
LLM WIKI/
├── AGENTS.md                    # 專案 Agent 規範
├── SKILL.md                     # 本 Loop 規格書（此檔案）
├── scripts/
│   └── check_presentation.py    # Phase 3 程式化檢查腳本
├── presentations/
│   ├── procrastination_self_help.html   # 目前主要簡報
│   └── check_report.json        # 最新一次程式化檢查結果（JSON）
├── wiki/                        # 封閉知識庫
│   ├── index.md
│   ├── log.md
│   ├── papers/
│   ├── concepts/
│   ├── methods/
│   └── topics/
└── raw/paper/                   # 原始 PDF（唯讀）
```

---

## 7. 實作狀態說明

| 功能 | 狀態 |
|:--|:--|
| Phase 0–1（Wiki 評估 + 大綱確認） | ✅ 已定義；由 Agent 人工執行 |
| Phase 2（HTML 生成） | ✅ 已定義；由 Agent 人工執行 |
| Phase 3（程式化檢查） | ✅ 已實作 → `scripts/check_presentation.py` |
| Phase 4（AI 審查清單） | ✅ 已定義；需人工對照 Wiki 核查 |
| Phase 4（AI 審查自動化） | ⬜ 尚未實作（需 NLP 語義分析，超出目前環境） |
| Phase 5（交付 + log 更新） | ✅ 已定義；由 Agent 人工執行 |
| 自動三輪 Loop 修正 | ⬜ 尚未實作（架構設計完成，執行仍為人工迭代） |
