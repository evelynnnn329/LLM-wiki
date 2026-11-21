---
type: method
tags: [Methodology, Statistics, MetaAnalysis]
---

# Psychometric Meta-Analysis (心理計量統合分析)

## 方法概述
心理計量統合分析（Psychometric Meta-Analysis）由 Frank L. Schmidt 與 John E. Hunter 提出，是心理學與組織行為學中匯總多項獨立實證研究的最嚴謹統計方法。其核心特色在於**系統性校正統計人為誤差（Statistical Artifacts）**，包括抽樣誤差（Sampling error）、測量工具信度不足（Measurement unreliability）以及受試者範圍限制（Range restriction），以推估真實總體的總效應值（True Score Correlation, $\rho$）。

## 核心校正協定
1. **抽樣誤差校正**：根據樣本數進行加權平均，計算樣本加權平均相關係數（$\bar{r}$）。
2. **測量誤差校正（衰減校正 Disattenuation）**：
   $$
   \rho = \frac{\bar{r}}{\sqrt{r_{xx} \cdot r_{yy}}}
   $$
   其中 $r_{xx}$ 與 $r_{yy}$ 為各變數量表的信度係數（如 Cronbach's $\alpha$）。
3. **區間估計**：
   - **信賴區間（Confidence Interval）**：反映平均效應值估計的統計精度。
   - **可信區間（Credibility Interval）**：反映校正後殘差變異（$SD_\rho$）在不同總體母群中的可推廣性（寬度過大暗示存在調節變數 Moderator）。

## 代表性應用論文
- **[[2007 Steel - The Nature of Procrastination]]**：對 216 篇研究、691 個效應值進行完整心理計量統合分析，校正了測量信度與年齡/學生樣本的範圍限制，產出拖延心理學史上最具公信力的相關性矩陣（如盡責性 $\rho = -.75$、神經質 $\rho = .28$、完美主義 $\rho = -.04$）。
