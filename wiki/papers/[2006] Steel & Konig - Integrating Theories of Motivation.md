---
title: "Integrating Theories of Motivation"
authors: ["Piers Steel", "Cornelius J. König"]
year: 2006
source: "raw/paper/[2006] Steel & Konig - Integrating Theories of Motivation.pdf"
doi_or_url: "10.5465/AMR.2006.22527462"
tags: [Motivation, TemporalDiscounting, DecisionTheory]
---

# Integrating Theories of Motivation

- **核心結論 (TL;DR)**：本文整合 Picoeconomics（雙曲貼現）、Expectancy Theory（期望理論）、Cumulative Prospect Theory（累積展望理論）與 Need Theory（需求理論），提出「時間動機理論」（[[Temporal Motivation Theory]]，簡稱 TMT），建立以「時間延遲」與「衝動性」為核心的統一人類決策數學模型。
- **文獻脈絡**：繼承自 Ainslie (1992) 的雙曲貼現模型與 Vroom (1964) 的期望理論，為 [[2007 Steel - The Nature of Procrastination]] 的 Meta-Analysis 提供理論根基，並與 [[2013 Sirois & Pychyl - Procrastination and the Priority of Short-Term Mood Regulation]] 形成認知決策 vs. 情緒調節的互補對照。

## 1. 研究動機 (Why)
- **學門割裂痛點**：人類動機理論長期割裂於經濟學（理性選擇）、心理學（自我調節與特質）與行為主義（強化時程）。缺乏跨學門共識（Consilience）。
- **靜態模型盲點**：傳統期望理論（$E \times V$）是片段式（episodic）與靜態的，無法解釋跨時間的「偏好逆轉」（Preference Reversal，例如：今天計畫下週讀書，下週卻選擇打電動）與非理性拖延。

## 2. 核心方法與技術創新 (How)
- **TMT 數學公式架構**：
  $$
  \text{Utility} = \sum_{i=1}^k \frac{E^+ \times V^+}{Z + \Gamma^+(T - t)} + \sum_{i=k+1}^n \frac{E^- \times V^-}{Z + \Gamma^-(T - t)}
  $$
- **核心變數解析**：
  - $E$ (Expectancy)：成功獲得報酬的期望機率（受自我效能 Self-efficacy 影響）。
  - $V$ (Value)：結果的吸引力或負向厭惡感（Task Aversiveness 與 Need for Achievement）。
  - $\Gamma$ (Gamma)：對時間延遲的敏感度，本質即為人格特質中的「衝動性」（Impulsiveness）。
  - $T - t$ (Delay)：距離獲得回報或面臨懲罰的時間距離。
  - $Z$：常數，防止當延遲接近零時效用無限大。
- **簡化通用形式**：
  $$
  \text{Utility} = \frac{E \times V}{\Gamma D}
  $$

## 3. 關鍵實證與實驗結果 (Results)
- **解釋大學生寫報告的動力曲線**：學期初因截止日遙遠（$D$ 極大），寫作業效用遠低於當下社交活動；唯有截止日逼近（$D$ 趨近於 0），作業的效用才呈雙曲急劇上升，超越社交誘惑。
- **目標設定理論的數學詮釋**：將長期目標拆解為近期次目標（Proximal subgoals），能大幅縮短感知延遲 $D$，使任務效用長期維持在背景誘惑之上。
- **群體工作步調驗證**：重新分析 Gersick (1989) 與 Chang et al. (2003) 團隊時間發言數據，證實團隊工作步調非線性，而是符合雙曲貼現加速特徵。

## 4. 局限性與學術批判 (Limitations & Critiques)
- 模型參數繁多（區分收益與損失、期望轉換率），在實證情境中同時精準量化個人參數極具挑戰。
- 偏重理性認知評估與時間折扣，對突發性負向情緒的「即時情緒逃避機制」著墨較少（後由 Sirois & Pychyl, 2013 補充）。

## 5. 實體關聯 (Entities)
- 核心概念：[[Temporal Motivation Theory]], [[Irrational Delay]], [[Present vs Future Self]]
- 涉及方法：[[Psychometric Meta-Analysis]]
- 關聯文獻：[[2007 Steel - The Nature of Procrastination]], [[2013 Sirois & Pychyl - Procrastination and the Priority of Short-Term Mood Regulation]]
