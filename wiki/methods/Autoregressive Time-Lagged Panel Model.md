---
type: method
tags: [Methodology, Statistics, SEM, Longitudinal]
---

# Autoregressive Time-Lagged Panel Model (自迴歸時間滯後面版模型)

## 方法概述
自迴歸時間滯後面版模型（Autoregressive Time-Lagged Panel Model）是結構方程模型（SEM）中處理多波縱向追蹤資料（Longitudinal Panel Data）的黃金標準分析工具。它允許研究者在控制變數自身跨時間穩定性（Autoregressive Stabilities）的前提下，檢驗變數 $X$ 在時間點 $T_1$ 是否能跨時間預測變數 $Y$ 在時間點 $T_2$ 的變化（Cross-Lagged Effects），從而嚴謹評估變數之間的**時間先後順序與潛在因果方向**。

## 核心協定與實施步驟
1. **測量恆等性檢定（Measurement Invariance Testing）**：
   - 確保測量工具在不同時間點所測量的是同一個潛在構念（Construct）。
   - 檢定順序：
     - **Configural Invariance ($M_{CI}$)**：因素結構形態相同。
     - **Metric Invariance ($M_{MI}$)**：因素負荷量（Factor Loadings）跨時間受限等同。
     - **Scalar Invariance ($M_{SI}$)**：截距（Intercepts）跨時間受限等同。
     - **Residual Invariance ($M_{RI}$)**：殘差變異數跨時間受限等同。
2. **模型比較（Model Comparison）**：
   - **基準穩定模型 ($M_0$)**：僅包含各變數自身的自迴歸路徑（$X_{T1} \to X_{T2} \to X_{T3}$）。
   - **交叉滯後中介模型 ($M_1$)**：加入時間滯後中介路徑（如 $X_{T1} \to M_{T2} \to Y_{T3}$）及直接路徑（$X_{T1} \to Y_{T3}$）。
   - 評估指標：Satorra-Bentler $\chi^2$ 差值檢定、AIC、RMSEA、CFI。

## 代表性應用論文
- **[[2024 Jochmann et al - Procrastination, Depression and Anxiety Symptoms in University Students]]**：採用一年三波（每波間隔 6 個月，有效樣本 $n = 392$）的自迴歸面版模型，以 R 語言 `lavaan` 套件檢驗拖延、知覺壓力與憂鬱/焦慮症狀，成功推翻了知覺壓力的長期因果中介假說。
