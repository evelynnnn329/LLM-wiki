---
title: "Procrastination, depression and anxiety symptoms in university students: a three-wave longitudinal study on the mediating role of perceived stress"
authors: ["Anna Jochmann", "Burkhard Gusy", "Tino Lesener", "Christine Wolter"]
year: 2024
source: "raw/paper/[2024] Jochmann et al - Procrastination, Depression and Anxiety Symptoms in University Students.pdf"
doi_or_url: "10.1186/s40359-024-01761-2"
tags: [LongitudinalStudy, MentalHealth, PerceivedStress, ProcrastinationHealthModel]
---

# Procrastination, depression and anxiety symptoms in university students: a three-wave longitudinal study on the mediating role of perceived stress

- **核心結論 (TL;DR)**：針對 392 名大學生進行的一年三波縱向面版研究（Three-wave longitudinal study），證實特質拖延長期直接預測憂鬱與焦慮症狀；然而**意外推翻了經典「拖延-健康模型（[[Procrastination-Health Model]]）」的核心假設**：知覺壓力（Perceived Stress）在長期（6個月/12個月）並非拖延損害心理健康的中介變數！
- **文獻脈絡**：直接檢驗由 Sirois et al. (2003, 2013) 在 [[2013 Sirois & Pychyl - Procrastination and the Priority of Short-Term Mood Regulation]] 中提出的健康中介途徑，並與 [[2007 Steel - The Nature of Procrastination]] 的跨期後果實證呼應，是目前檢驗拖延與心理疾病因果鏈最新且最嚴謹的縱向研究之一。

## 1. 研究動機 (Why)
- **實證盲點**：以往支持「拖延 $\rightarrow$ 壓力 $\rightarrow$ 身心疾病」的證據大多來自橫斷面研究（Cross-sectional）或極短時間追蹤（$\le 3$ 個月），無法確立長期時間動態下的因果關係。
- **核心假設 (Hypotheses)**：
  - H1：拖延隨時間推移會顯著導致知覺壓力增加。
  - H2：知覺壓力隨時間推移會顯著導致憂鬱與焦慮症狀增加。
  - H3：知覺壓力中介了拖延對憂鬱與焦慮症狀的長期影響。

## 2. 核心方法與技術創新 (How)
- **縱向研究設計**：德國柏林自由大學大學生健康監測計畫，1 年內追蹤 3 次（T1、T2、T3，每波間隔 6 個月）。
- **樣本情況**：T1 施測 3,420 人，三波完整填答有效樣本 $n = 392$。
- **統計分析協定**：
  - 使用 R 語言 `lavaan` 套件進行結構方程模型（SEM）。
  - 自迴歸時間滯後面版模型（[[Autoregressive Time-Lagged Panel Model]]）。
  - 嚴格檢驗測量恆等性（Measurement Invariance：Configural, Metric, Scalar, Residual Invariance）。

## 3. 關鍵實證與實驗結果 (Results)
- **假設檢定結果**：
  - **H1 拒絕**：拖延（T1）到知覺壓力（T2）以及拖延（T2）到知覺壓力（T3）的時間滯後路徑均不顯著（$\beta = .072$ 與 $.063$）。
  - **H2 拒絕**：知覺壓力（T1）到憂鬱/焦慮（T2）以及知覺壓力（T2）到憂鬱/焦慮（T3）的路徑亦不顯著（$\beta = .128$ 與 $.073$）。
  - **H3 僅部分支持**：拖延（T1）到憂鬱與焦慮症狀（T3）存在顯著的直接長期路徑（$\beta = 0.16, p < .001$），但**知覺壓力的中介路徑完全不成立**！
- **重要理論洞見**：
  - **急性壓力不等於慢性壓力**：學生因拖延造成的壓力多集中於期末前夕的「急性壓力」（Acute Stress），考後即獲緩解，不必然沉澱為全年的「慢性知覺壓力」（Chronic Stress）。
  - **替代中介機制之啟發**：拖延損害心理健康的真正長期途徑，很可能是負向情感與道德情緒（內疚、自責、羞愧感，如 Sirois & Pychyl 2013 所述）或健康行為惡化（如睡眠品質低落），而非普遍性的主觀知覺壓力。

## 4. 局限性與學術批判 (Limitations & Critiques)
- **樣本流失率高**：三波流失率達 88.5%，流失分析顯示三波全參與者原本的拖延程度即顯著低於中途流失者（存在健康倖存者偏差）。
- **測量時點效應**：三次測量時機皆落於期末考前夕的敏感階段，可能使整體壓力基準偏高，掩蓋了學期間的長期波動。
- **性別偏差**：有效追蹤樣本中女性佔 74%，代表性受限。

## 5. 實體關聯 (Entities)
- 核心概念：[[Procrastination-Health Model]], [[Short-Term Mood Regulation]], [[Present vs Future Self]]
- 涉及方法：[[Autoregressive Time-Lagged Panel Model]]
- 關聯文獻：[[2013 Sirois & Pychyl - Procrastination and the Priority of Short-Term Mood Regulation]], [[2007 Steel - The Nature of Procrastination]]
