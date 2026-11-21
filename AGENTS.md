# AGENTS.md - Academic Paper LLM Wiki Schema

本文件定義 Agent 在維護此學術論文知識庫時的角色職責、目錄規範、語言標準與標準作業程序（SOP）。
本專案為**「拖延症自救研究所」**，以拖延心理學學術論文為核心知識來源。架構借鑑 Andrej Karpathy 的 LLM Wiki 模式：**「LLM 負責讀取、總結、交叉引用與維護，使用者負責選題、探索與審閱，形成持續累積複利的 Markdown 知識庫；並在需要時將 Wiki 知識轉化為具教學價值的 HTML 簡報」**。

---

## 1. 核心原則與語言規範

1. **語言規範**：
   - **內文說明、分析論述與結構標題**：一律使用**繁體中文**撰寫。
   - **專有名詞保留**：遇**模型名稱**（Model Names）、**技術術語**（Technical Terms）、**評測指標**（Metrics）、以及**論文原文標題**（Paper Titles）時，**直接保留英文**，以維持學術精準度與檢索一致性。
2. **Obsidian 與 Markdown 規範**：
   - 跨文件引用一律使用 Obsidian 雙向連結語法：`[[頁面名稱]]`（頁面名稱不需加上 `.md` 副檔名，不使用繁瑣的相對路徑）。
   - 數學公式使用標準 LaTeX 格式：行內公式 `$E = mc^2$`，獨立展示區塊 `$$...$$`。
   - 所有筆記皆需附帶結構化 YAML Frontmatter，方便未來擴充與檢索。
3. **適用學術範疇（Cross-Disciplinary）**：
   - 本庫聚焦於心理學與跨學門學術研究（包含心理學、行為經濟學、教育介入與身心健康等）。
   - 聚焦於學術四要素：動機 (Why)、方法 (How)、結果 (Results)、批判 (Limitations)。
4. **知識複利核心（Compounding Artifact）**：
   - 論文不只是單篇獨立筆記，必須主動與既有的 `concepts/`、`methods/`、`topics/` 頁面互相串接、標記矛盾、補強證據鏈。
5. **封閉知識庫原則（Closed-World Assumption for Presentation）**：
   - 當產出教學簡報或回答特定問題時，**嚴格只能使用現有 Wiki 已記載的知識**。
   - 嚴禁自行進行外部搜尋或編造 Wiki 之外的研究結論。若資料不足，必須誠實向使用者說明。

---

## 2. 目錄架構 (Architecture)

```text
.
├── AGENTS.md                  # 本指引文件（Agent 系統準則與 SOP）
├── scripts/                   # 自動化輔助腳本（PDF 下載、文字抽取等）
│   └── paper_utils.py
├── raw/                       # 原始來源層（Immutable，唯讀）
│   └── paper/                 # 所有論文 PDF 存放處（唯一指定路徑）
├── presentations/             # HTML 教學簡報輸出目錄
└── wiki/                      # 知識庫核心層（Agent 維護，持續更新）
    ├── index.md               # 知識庫總目錄（分類列出所有條目與單行結論）
    ├── log.md                 # 時間軸演進日誌（記錄每次 Ingest、Query 沉澱、Lint 與 Presentation 生成）
    ├── papers/                # 單篇論文分析頁
    ├── concepts/              # 核心理論、假說、現象與定義頁
    ├── methods/               # 研究方法、實驗設計、演算法與協定頁
    └── topics/                # 主題綜述、跨文獻對比、學術爭議與演進頁
```

---

## 3. 原始來源管理規範 (Raw Sources Handling)

1. **本地 PDF 上傳**：
   - 當使用者在對話中提供 PDF 檔案時，**必須確保將該 PDF 儲存至 `raw/paper/` 目錄**。
   - 檔名規範：`[年份] 第一作者姓氏 - 論文簡稱.pdf`，例如：`[2007] Steel - The Nature of Procrastination.pdf`。
2. **arXiv 連結與線上來源**：
   - 當使用者提供 arXiv 連結（如 `https://arxiv.org/abs/2310.06825`）或 arXiv ID（如 `2310.06825`）時：
     - **必須自動下載 PDF 並儲存至 `raw/paper/`**。
     - 執行指令：`python scripts/paper_utils.py download <arxiv_url_or_id>`。
     - 該腳本會自動抓取中繼資料（標題、作者、年份、Abstract）並命名儲存。
3. **來源不可變原則 (Immutability)**：
   - 存入 `raw/paper/` 的 PDF 檔案為知識庫的原始事實依據（Ground Truth），一旦存入嚴禁修改。

---

## 4. 四大核心作業流程 (Operations)

### 流程一：論文消化 (Ingest Workflow) - 半自動互動式

當使用者提供新論文或要求 Ingest 時，嚴格執行以下步驟：

#### Step 1: 讀取與解析 (Extract)
- 確保 PDF 已放置於 `raw/paper/`。
- 讀取論文全文或前置章節，提取基礎 Metadata（Title, Authors, Year, Publication/DOI/arXiv ID）。

#### Step 2: 提煉標準學術四要素 (Draft Synthesis)
在對話中向使用者呈現該論文的精華提煉（使用繁體中文，術語保留英文）：
- **TL;DR**：1~2 句話概括論文核心貢獻。
- **1. 研究動機 (Why)**：為了解決什麼過去理論/實驗的盲點或痛點？核心假設 (Hypothesis) 為何？
- **2. 核心方法與技術創新 (How)**：具體設計（數學架構、實驗協定、演算法），關鍵創新點 (Key Trick) 是什麼？
- **3. 關鍵實證與實驗結果 (Results)**：主要實驗設定、基準對照（Baselines）、量化指標成果。
- **4. 局限性與學術批判 (Limitations & Critiques)**：未經檢驗的強假設、實驗條件侷限、潛在樣本偏差、作者未說清之處。

#### Step 3: 提議擴散更新方案 (Compounding Proposal)
**在寫入檔案前，主動向使用者提出更新提案**：
> 「我提議針對這篇論文進行以下知識庫更新：
> 1. 建立論文頁面：`wiki/papers/[[YYYY Author - Title]]`
> 2. 新建/更新概念頁：`wiki/concepts/[[相關概念]]`
> 3. 更新方法頁：`wiki/methods/[[相關方法]]`（補充該方法在本論文中的改良或應用）
> 4. (若有) 更新主題頁：`wiki/topics/[[相關學術爭論]]`
> 5. 同步登記至 `wiki/index.md` 與 `wiki/log.md`
> 請問您是否同意此規劃，或有特別想強調的角度？」

#### Step 4: 經確認後執行寫入 (Execute)
使用者確認後，執行檔案寫入：
1. 建立 `wiki/papers/` 下的論文頁面。
2. 建立或更新對應的 `wiki/concepts/`、`wiki/methods/` 頁面，加入雙向連結 `[[...]]`。
3. 在 `wiki/index.md` 對應分類中加入該條目與單行結論。
4. 在 `wiki/log.md` 追加一筆日誌：
   ```markdown
   ## [YYYY-MM-DD] ingest | 論文標題
   - 新增論文筆記：[[檔案名稱]]
   - 更新關聯實體：[[概念A]], [[方法B]]
   ```

---

### 流程二：綜合提問與沉澱 (Query & Synthesis Workflow)

1. **檢索策略**：
   - 當使用者提問跨論文問題（如「目前庫內針對 X 現象有哪些不同解釋？」或「比較方法 A 與方法 B 的優缺點」）：
   - Agent **優先閱讀 `wiki/index.md`** 定位相關筆記，再深入讀取對應的 `wiki/papers/`、`wiki/concepts/`、`wiki/methods/`。
2. **回答格式**：
   - 綜合多篇論文進行論述，所有觀點必須精準附帶雙向引用連結（例如：根據 `[[2007 Steel - ...]]` 與 `[[2024 Jochmann - ...]]`）。
3. **知識沉澱反哺 (Save Back)**：
   - 若該回答形成了高價值的跨文獻對比或綜述，Agent 主動詢問：
     *「這是一份有價值的綜合分析，是否將其沉澱為 `wiki/topics/[[主題名稱]].md` 並記錄到索引中？」*
   - 經同意後建立該 Topic 頁面，使探索對話化為持久知識資產。

---

### 流程三：知識庫健康檢查 (Lint Workflow)

每隔一段時間或在使用者要求時，執行 Wiki Lint：
1. **死鏈檢查**：是否有 `[[...]]` 指向不存在的檔案？
2. **孤島檢查**：是否有任何頁面未被 `wiki/index.md` 或其他頁面引用？
3. **矛盾與衝突檢測**：是否有較新的論文推翻或挑戰了早期論文的結論，但尚未在舊頁面或概念頁中標註「Disputed」或「Contradicted by」？
4. **輸出 Lint 報告**，列出修正建議，確認後修復。

---

### 流程四：HTML 教學簡報生成 (Presentation Workflow)

當使用者提出一個教學簡報主題或要求生成簡報時，嚴格依序執行以下四步驟：

#### Step 1: 讀取 Wiki 知識 (Retrieve from Wiki Only)
- **檢索起點**：先完整閱讀 `wiki/index.md` 掌握既有條目，再調閱相關的 `papers/`、`concepts/`、`methods/` 與 `topics/` 筆記。
- **封閉事實原則**：生成簡報時**只能使用現有 Wiki 已記載的知識**。
- **禁止外部擴充與編造**：嚴禁自行搜尋外部網絡資料或加入 Wiki 未記載的研究結論。
- **邊界確認**：若現有 Wiki 的文獻儲備不足以完整覆蓋該主題的某些面向，應明確向使用者指出知識限制，絕不自行揣測或捏造心理學結論。

#### Step 2: 規劃教學簡報大綱 (Pedagogical Outline & Mapping)
- **教學導向 (Teaching-Oriented)**：簡報目的為「教學與引導改變」，而非單純的文獻回顧或摘要。需針對目標學習者（如大學生）的認知規律，設計循序漸進的學習路徑。
- **頁面核心焦點**：每一頁投影片必須有明確且單一的教學目標（Takeaway），避免認知超載。
- **來源映射 (Source Mapping)**：在規劃大綱時，每一頁的主要知識點皆需明確標記其對應的 Wiki 條目或論文來源（例如：對應 `[[Temporal Motivation Theory]]` 或 Steel, 2007）。
- **互動確認 (Outline Confirmation)**：在生成具體 HTML 程式碼前，**必須先向使用者展示簡報大綱、頁數規劃與核心教學點，待使用者確認或調整後再執行程式碼生成**。

#### Step 3: 生成 HTML 簡報 (Generate Interactive Presentation)
- **技術架構**：採用標準 HTML5、CSS 與必要的原生 JavaScript 製作成單一或清晰結構的網頁簡報檔案，存放於 `presentations/` 目錄。
- **瀏覽器獨立運行**：確保簡報可在現代主流瀏覽器中直接開啟，離線可用，無外部脆弱相依性。
- **核心互動控制**：
  - 具備基本的上一頁（Previous）、下一頁（Next）按鈕及鍵盤方向鍵（← / →）切換功能。
  - 明確顯示當前頁碼與總頁數（例如：`Slide 3 / 10`）。
- **視覺與語言風格**：
  - 內文使用繁體中文，關鍵學術術語與模型名稱保留英文。
  - 設計風格清楚、活潑、富現代感且排版舒適。
  - 善用圖解架構、對比表格、生活化情境卡片、以及簡單的互動小測驗（Quiz/Reflection）輔助教學理解。
  - **嚴格控制每頁字數**：避免投影片塞入過多密集長文字，採用要點、視覺區塊與關鍵字呈現，符合實際上台口頭講解的最佳實踐。

#### Step 4: 檢查簡報內容 (Verification & Fact-Checking)
生成簡報後，必須進行嚴謹的自我審查：
- **主題契合度**：確認內容緊扣使用者指定之主題與設定之教學對象。
- **知識一致性**：逐頁確認所有心理學定義、理論機制、統計數據與改善策略均能在 Wiki 找到對應依據。
- **科學嚴謹度**：**嚴禁將研究中的「相關性（Correlation）」誤寫為「因果關係（Causation）」**（例如：將「盡責性與拖延高度負相關」正確表述為特質關聯，而非單向因果；精準呈現 Jochmann 2024 中知覺壓力並非長期因果中介的最新結論）。
- **來源標示**：投影片關鍵理論與實證結果處應保留規範的學術來源標記（如：Steel, 2007；Sirois & Pychyl, 2013）。
- **功能與版面實測**：實際檢視 HTML 排版、字體大小、翻頁邏輯與控制按鈕是否運作流暢。
- **真實檢驗原則**：嚴格實事求是，未經實際檢查或無法確認的項目，不得對使用者宣稱已完成驗證。

---

## 5. 檔案格式範本

### 5.1 論文頁範本 (`wiki/papers/[YYYY] Author - Short Title.md`)

```markdown
---
title: "Paper Full English Title"
authors: ["Author 1", "Author 2"]
year: 2024
source: "raw/paper/[YYYY] Author - Short Title.pdf"
doi_or_url: "..."
tags: [DomainTag, MethodTag]
---

# Paper Full English Title

- **核心結論 (TL;DR)**：繁體中文總結核心發現。
- **文獻脈絡**：繼承自 [[先驗文獻]]，與 [[對立文獻]] 的觀察相左。

## 1. 研究動機 (Why)
- 說明既有文獻的盲點、實際問題背景與本文核心假說。

## 2. 核心方法與技術創新 (How)
- 實驗設計、數學推導（如 $f(x) = \sigma(Wx + b)$）與創新機制。

## 3. 關鍵實證與實驗結果 (Results)
- 實驗設定、對照組、關鍵指標數據與發現。

## 4. 局限性與學術批判 (Limitations & Critiques)
- 限制條件、潛在偏差與未解決問題。

## 5. 實體關聯 (Entities)
- 核心概念：[[概念A]], [[理論B]]
- 涉及方法：[[方法C]]
```

### 5.2 概念頁範本 (`wiki/concepts/Concept Name.md`)

```markdown
---
type: concept
tags: [Theory, Domain]
---

# Concept Name

## 定義與內涵
概念的嚴謹學術定義與繁體中文解釋。

## 相關核心公式 / 機制
$$
\text{Formula if applicable}
$$

## 文獻佐證與演進
- **提出者/經典基石**：[[相關論文A]]
- **後續修正/爭端**：[[相關論文B]] 發現此機制在特定條件下失效。
```

### 5.3 方法頁範本 (`wiki/methods/Method Name.md`)

```markdown
---
type: method
tags: [Methodology, Analysis]
---

# Method Name

## 方法概述
該研究方法、實驗協定或統計模型的核心目標與適用範疇。

## 核心協定與數學推導
實施步驟、數學公式或模型假設。

## 代表性應用論文
- [[相關論文A]]：首次將此方法應用於...
```

### 5.4 主題綜述頁範本 (`wiki/topics/Topic Name.md`)

```markdown
---
type: topic
tags: [Synthesis, LiteratureReview]
---

# Topic Name

## 主題脈絡與核心爭端
該研究主題的核心問題意識與歷史演進。

## 學派對照與論點演進
- **觀點 A（如理性選擇模型）**：[[論文 1]], [[論文 2]] 主張...
- **觀點 B（如情緒調節模型）**：[[論文 3]] 提出反駁...
- **最新實證檢驗**：[[論文 4]] 透過縱向面板模型發現...

## 開放性問題與未來方向
當前文獻尚未解決的矛盾點。
```

---

## 6. 「拖延症自救研究所」教學定位與專案指引

本專案旨在將嚴謹的拖延心理學學術文獻，轉化為能夠啟發學習者自我覺察與有效改善的教學工具。

### 6.1 核心教學主題
預定主題：**《為什麼我們總是拖到最後一刻？——拖延心理學與改善方法》**

### 6.2 教學定位矩陣
- **目標受眾 (Target Audience)**：大學生（面臨高度自主排程、課業要求、報告與期末考壓力的群體）。
- **教學風格 (Pedagogical Tone)**：**趣味與科學並重**。以生動、親切且具共鳴的語言切入，背後以嚴謹扎實的實證研究為後盾。
- **核心知識範疇 (Knowledge Scope)**：
  1. **拖延的嚴謹定義**：非理性延遲（Irrational Delay）與自主意圖落差。
  2. **深層心理成因**：短期情緒調節失敗（Giving in to feel good）、自我調節資源耗竭、衝動性（Impulsiveness）與自我效能（Self-efficacy）。
  3. **時間與動機機制**：Temporal Motivation Theory (TMT) 模型（雙曲貼現、時間距離與效用變化）。
  4. **拖延的實質影響**：對身心健康（憂鬱、焦慮、主觀健康）與學業表現的真實衝擊；釐清知覺壓力與慢性健康影響的最新實證爭辯。
  5. **科學改善策略**：基於動機與情緒的有效介入（次目標拆解 Proximal subgoals、情境刺激控制 Stimulus control、自我同情與接納承諾等），反思單純時間管理訓練的局限。
- **教學情境化 (Contextualization)**：
  - 廣泛連結大學生高度共鳴的生活與學業情境（如：學期初信誓旦旦但期末通宵肝報告、考前瘋狂整理桌面或滑手機、看見論文題目時的逃避）。
- **研究依據與生活案例界線 (Boundary of Evidence)**：
  - **嚴格事實依據**：所有的心理學理論、機制假設、統計數據與介入效果評估，必須 100% 來自現有 Wiki。
  - **案例定位**：生活情境與比喻僅作為「教學引導與認知鷹架（Scaffolding）」，必須清楚表達為教學範例，絕不得包裝或冒充成學術實證結論。
