# LectureS3_BinaryChoice_Semiparametric Proofreading Report

**File:** `Slides/LectureS3_BinaryChoice_Semiparametric.tex`
**Date:** 2026-05-06
**Total findings:** 26
**Lines:** 4642 | Frames: 147 main + 17 appendix

## Summary

| Category | Count | Severity Breakdown |
|---|---|---|
| Math | 4 | 1 critical, 3 major |
| Consistency | 9 | 2 critical, 5 major, 2 minor |
| Typo | 5 | 1 critical, 2 major, 2 minor |
| Grammar | 4 | 0 critical, 1 major, 3 minor |
| Quality | 4 | 0 critical, 0 major, 4 minor |
| **Total** | **26** | **5 critical, 11 major, 10 minor** |

---

## Top 5 Critical Issues

### Critical 1: Math contradiction in Manski rate explanation
- **Location:** Frame 76, lines 2305–2311
- **Current:** "MS 目标函数 ... 在最优 $\beta_0$ 处**二次平坦**：$S_\infty(\beta) - S_\infty(\beta_0) \sim -c \|\beta - \beta_0\|^2$ ... $\sim -c |\beta - \beta_0|^?$ ... 阶跃函数使总体目标 $S_\infty$ 在 $\beta_0$ 处只有**一阶斜率**（不是二阶曲率）"
- **Problem:** Self-contradictory ("二次平坦" then "一阶斜率"); literal `?` in math display.
- **Proposed:** Remove `^?` placeholder. Reconcile: Manski's $S_\infty$ has *quadratic* local curvature (under regularity); the cube-root rate comes from empirical-process bracketing entropy yielding fluctuations of order $n^{-1/2}\delta^{1/2}$ that balance the quadratic descent at $\delta\sim n^{-1/3}$.
- **Category:** Math
- **Severity:** Critical

### Critical 2: Math error in scale-invariance derivation
- **Location:** Frame 103, line 3166
- **Current:** `$G_{c}'(z') \cdot c \beta_0 = c \cdot G'(z'/c) \cdot c \beta_0 / c = G'(z) \cdot \beta_0$`
- **Problem:** Chain rule gives $G_c'(u) = (1/c)G'(u/c)$, NOT $c \cdot G'(u/c)$. Factor of $c$ is inverted.
- **Proposed:** `$G_{c}'(z') \cdot c \beta_0 = (1/c) \cdot G'(z'/c) \cdot c \beta_0 = G'(z) \cdot \beta_0$` (with $z = z'/c$)
- **Category:** Math
- **Severity:** Critical

### Critical 3: Han model arity inconsistency
- **Location:** Frame 64, lines 1923 vs 1928
- **Current:** Body: "$Y = D(X'\beta_0, \varepsilon)$" (D takes two args); next definitionbox: "$Y_i = D(X_i'\beta_0 + \varepsilon_i)$" (D takes one arg)
- **Proposed:** Standardize on Han (1987): "$Y = D(X'\beta_0 + \varepsilon)$" (single argument). Change line 1923.
- **Category:** Math / Consistency
- **Severity:** Critical

### Critical 4: TOC errors
- **Location:** Frame 10, lines 357, 359, 361
- **Current:** "9 & 其他半参数模型 & 加法、变系数、**多指标**"; "11 & ... & **五种方法**对比"; "附录 & **15 个**证明帧"
- **Proposed:** "多指数" (matches section title 3318); "八种方法" (Frames 122/126 compare 8 methods); "17 个证明帧" (appendix has C.1–C.17)
- **Category:** Consistency
- **Severity:** Critical

### Critical 5: Citation style split
- **Location:** Appendix lines 4170, 4316, 4380, 4439, 4468, 4540, 4638
- **Current:** Body uses `\textit{Author (Year)}`; appendix uses `\citep{key}` (e.g., `\citep{robinson1988}`, `\citep{newey1990}`)
- **Proposed:** Convert appendix `\citep{...}` calls to inline italic to match body convention.
- **Category:** Consistency
- **Severity:** Critical

---

## Major Issues

### Major 1: Appendix labels (C.1–C.17) misaligned with hypertargets (proof-c1, c2, c3, c5–c18)
- **Location:** Appendix lines 4117–4640
- **Current:** Hypertarget IDs skip c4 (jump from c3 to c5), end at c18; slide titles run sequentially C.1–C.17.
- **Proposed:** Either renumber slide titles to match hypertargets (C.1, C.2, C.3, C.5, …, C.18) or relabel hypertargets to proof-c1 through proof-c17 (and update 19 `\hyperlink{...}` references in body). Recommend the latter.
- **Category:** Consistency
- **Severity:** Major

### Major 2: Broken back-link
- **Location:** Line 4143
- **Current:** `\hfill\hyperlink{main-c1}{\beamergotobutton{返回}}`
- **Problem:** No `\hypertarget{main-c1}` exists in body. Also, only this one appendix slide has a back-link; the other 16 lack one.
- **Proposed:** Either add `\hypertarget{main-c1}{}` to Frame 18 OR remove this back-button (and remove the inconsistency).
- **Category:** Consistency
- **Severity:** Major

### Major 3: Terminology drift "展度" vs "尺度"
- **Location:** Lines 943, 4121, 4129
- **Current:** "展度归一化" / "(展度) 不可识别"
- **Problem:** Document predominantly uses "尺度" (lines 562–581) — "展度" is unconventional in Chinese econometrics.
- **Proposed:** Replace all "展度" with "尺度".
- **Category:** Consistency
- **Severity:** Major

### Major 4: Mixed Chinese-English axiomatic conditions
- **Location:** Frame 112, line 3454
- **Current:** "在 (i) compact support of $X$, (ii) $p(X) \in (0, 1)$ 强严格分隔, (iii) series 估计 $\hat p$, (iv) 适当矩条件下"
- **Proposed:** "在 (i) $X$ 的支撑紧, (ii) $p(X) \in (0, 1)$ 严格分隔零, (iii) 用 series 估计 $\hat p$, (iv) 适当矩条件下"
- **Category:** Grammar / Consistency
- **Severity:** Major

### Major 5: Typo "加方法" → "该方法"
- **Location:** Frame 107, line 3308
- **Current:** "**加方法**兼具参数解释性与非参数灵活性"
- **Proposed:** "**该方法**兼具参数解释性与非参数灵活性"
- **Category:** Typo
- **Severity:** Major

### Major 6: Duplicated word in marginal-effect formula
- **Location:** Frame 103, line 3160
- **Current:** "其中 $\hat G'$ 通过**核密度估计**核估计 $\hat G$ 的导数获得。"
- **Proposed:** "其中 $\hat G'$ 通过**对核估计 $\hat G$ 数值微分**获得。"
- **Category:** Typo / Grammar
- **Severity:** Major

### Major 7: Bracket mismatch in math
- **Location:** Appendix C.13, line 4489
- **Current:** "$\arg\max_s [Z(s) - \tfrac{1}{2} s' V_0 s\}]$"
- **Proposed:** "$\arg\max_s \{Z(s) - \tfrac{1}{2} s' V_0 s\}$"
- **Category:** Typo
- **Severity:** Major

### Major 8: "不效率" non-standard usage
- **Location:** Lines 1130, 1585, 2790, 2794, 2796
- **Current:** "Ichimura 一致估计 $\beta_0$，但不效率"
- **Problem:** "不效率" awkward in Chinese; standard term is "非有效".
- **Proposed:** "非有效" or "不达效率界". Change all 5 instances.
- **Category:** Grammar
- **Severity:** Major

### Major 9: Frame 76 contains literal `?`
- **Location:** Line 2307
- **Current:** "$S_\infty(\beta) - S_\infty(\beta_0) \sim -c |\beta - \beta_0|^?$"
- **Proposed:** Remove or replace with technical mechanism explanation (see Critical 1).
- **Category:** Typo / Math
- **Severity:** Major

### Major 10: Hard-coded "Frame 76" reference
- **Location:** Line 2171
- **Current:** "代价：收敛速度从 $\sqrt{n}$ 降至 $n^{1/3}$（详见 Frame 76）。"
- **Problem:** Fragile if frames are renumbered.
- **Proposed:** "（详见后文立方根速率定理）" or use `\hyperref`+`\label`.
- **Category:** Quality
- **Severity:** Major

### Major 11: Inconsistent rate notation $n^{-2/5}$ vs $n^{2/5}$
- **Location:** Multiple lines: 81, 548, 687, 690, 692, 778, 1909, 2565, 2604, 2757, 3909, 3947
- **Problem:** Sometimes $n^{-2/5}$ (error magnitude), sometimes $n^{2/5}$ (rate). Mixed in the same context.
- **Proposed:** Standardize: $n^{-2/5}$ for error magnitude $|\hat\beta-\beta|$; $n^{2/5}$ for rate (in $\sqrt{n}$-style). Same applies to $n^{-1/3}$ vs $n^{1/3}$, $n^{-1/2}$ vs $\sqrt{n}$.
- **Category:** Consistency
- **Severity:** Major

### Major 12 (additional): Unused appendix C.3 (proof-c3)
- **Location:** Lines 4175–4199
- **Problem:** Appendix proof "高阶核降偏证明" exists but no `\hyperlink{proof-c3}` in body references it.
- **Proposed:** Either add a body reference (Frame 14 or 47, where high-order kernels are mentioned) OR remove this orphaned proof.
- **Category:** Consistency
- **Severity:** Major

---

## Minor Issues

### Minor 1: "Part 5b-7" inconsistent
- **Location:** Line 1892
- **Current:** "下一阶段 (Parts 5b-7)"
- **Problem:** "5b" label appears nowhere else in the document.
- **Proposed:** "Parts 6-7" or "Part 5 onward".
- **Category:** Consistency
- **Severity:** Minor

### Minor 2: "奥义" overly informal
- **Location:** Line 1070
- **Current:** "**关键奥义：**"
- **Proposed:** "**关键洞察：**" or "**核心机制：**"
- **Category:** Quality
- **Severity:** Minor

### Minor 3: "颠覆性想法" overly informal
- **Location:** Lines 1923, 2114
- **Current:** "颠覆性想法"
- **Proposed:** "核心思想" / "核心创新"
- **Category:** Quality
- **Severity:** Minor

### Minor 4: "两个奇迹" overly informal
- **Location:** Line 411
- **Current:** "**两个奇迹同时发生：**"
- **Proposed:** "**两个有利结果同时出现：**" or "**两点同时实现：**"
- **Category:** Quality
- **Severity:** Minor

### Minor 5: English mid-Chinese in MROZ table
- **Location:** Frame 114, line 3525
- **Current:** "Lewbel (with V=age)"
- **Proposed:** "Lewbel（取 $V=$ 年龄）"
- **Category:** Consistency
- **Severity:** Minor

### Minor 6: "rlaplace::mrc" likely fictitious
- **Location:** Frame 68, line 2053
- **Current:** "**R 实现**：\texttt{rlaplace::mrc} 或自定义代码"
- **Problem:** No CRAN package "rlaplace" provides MRC.
- **Proposed:** "**R 实现**：通常需自定义；可参考 Cavanagh \& Sherman (1998) 提供的代码"
- **Category:** Quality
- **Severity:** Minor

### Minor 7: Overflow-prone wide tables
- **Location:** Frames 91 (line 2786), 122 (line 3791, 8 cols), 126 (line 3937), 36 (line 1082)
- **Problem:** Multiple `\scriptsize` tables with many columns may overflow 169 widescreen.
- **Proposed:** Wrap with `\resizebox{\textwidth}{!}{...}` or reduce to `\tiny`. Frame 122 (8 method columns + variable name) is particularly tight.
- **Category:** Overflow
- **Severity:** Minor

### Minor 8: Heteroskedasticity claim about KS/Ichimura over-stated
- **Location:** Frame 72, lines 2190, 2192
- **Current:** "Klein-Spady & 不一致：$G$ 形态依赖 $X$, 违反单指数"; "Ichimura & 不一致：同 KS 原因"
- **Problem:** KS/Ichimura are inconsistent only when heteroskedasticity *breaks the single-index structure*. If $\sigma$ depends only on $X'\beta$, KS still applies.
- **Proposed:** "KS 与 Ichimura 在 $\sigma(X)$ 不仅依赖于 $X'\beta$ 时不一致（破坏单指数）"
- **Category:** Math / Quality
- **Severity:** Minor

### Minor 9: Curly quotes consistency check
- **Location:** Multiple lines (218, 282, 298, 305, 393, 627, 805, etc.)
- **Note:** Spot-check shows consistent use of Chinese curly quotes "..." for emphasis. No straight ASCII quotes found in spot checks.
- **Severity:** Minor (no action needed)

### Minor 10: Frame title hard-codes "二元 $Y$"
- **Location:** Various Klein-Spady frames
- **Note:** "二元 $Y$" repeated in multiple places without standardization. Minor stylistic issue.
- **Severity:** Minor (no action needed)

---

## Files Reviewed

- `Slides/LectureS3_BinaryChoice_Semiparametric.tex` (4642 lines, 147 main + 17 appendix frames)

## Recommended Action

**Critical 1-5 should be addressed before any public release**, particularly:
- Critical 1 (Manski rate explanation) and Critical 2 (scale-invariance math) — these are mathematical errors visible to any econometrician
- Critical 5 (citation style split) — easy mechanical fix

**Major 1-12 should be addressed before commit/PR.**

**Minor issues can be deferred** but ideally addressed in a polish pass.

Per protocol: this report does NOT modify the source file. Apply fixes after user review.
