# Lecture08_Specification — Proofreading Report

**File:** `Slides/Lecture08_Specification.tex`
**Date:** 2026-05-06
**Total findings:** 14
**Pages:** 61 | Compilation: 0 errors, 5 cosmetic overflow warnings (<10pt)

## Summary

| Category | Count | Severity |
|---|---|---|
| Content/Fidelity | 3 | 1 critical, 2 major |
| Consistency | 4 | 0 critical, 1 major, 3 minor |
| Grammar | 2 | 0 critical, 0 major, 2 minor |
| Quality | 3 | 0 critical, 1 major, 2 minor |
| Typo | 1 | 0 critical, 1 major, 0 minor |
| Overflow | 1 | 0 critical, 0 major, 1 minor |
| **Total** | **14** | **1 critical, 5 major, 8 minor** |

---

## Critical (1)

### Critical 1: Equation tags out of order (CEV section)
- **Lines:** 810, 816, 834
- **Current:**
  - L810: `\Cov(x_1, e_1) = 0. \tag{9.29}`
  - L816: `\Cov(x_1^*, e_1) = 0. \tag{9.31}`
  - L834: `y = \beta_0 + \beta_1 x_1 + (u - \beta_1 e_1). \tag{9.30}`
- **Problem:** Tags appear out of order (9.29 → 9.31 → 9.30). Confusing for students cross-referencing Wooldridge.
- **Proposed:** Renumber so tags ascend; verify against Wooldridge 8e.
- **Category:** Content / Consistency

---

## Major (5)

### Major 1: Possible SE transcription error in Example 9.1
- **Line:** 150
- **Current:** `$ptime86$ & $-0.041$ (0.009) & $0.287$ (0.004) \\`
- **Problem:** SE `0.004` for $ptime86$ in quadratic spec implies $t \approx 71$ — implausible. Inconsistent with neighboring SEs.
- **Proposed:** Verify against Wooldridge Table 9.1; likely should be `(0.094)` or similar.
- **Category:** Content / Typo

### Major 2: Orphan "Example 9.9 redux"
- **Line:** 1243
- **Current:** `\textbf{Example 9.9 redux:}`
- **Problem:** No Example 9.9 ever introduced (deck has 9.1, 9.2, 9.3, 9.4, 9.5, 9.7, 9.8, 9.10).
- **Proposed:** Either introduce 9.9 explicitly with proper frame label, or rename to `\textbf{Example 9.8 in logs:}` (this re-uses RDCHEM data from 9.8).
- **Category:** Consistency / Content

### Major 3: Variable names in math mode without `\mathit`/`\textit`
- **Lines:** Throughout (~20+ instances): 73, 77, 92, 223, 228, 365, 536, 767, 918, 1083, 1209, 1245, etc.
- **Problem:** Multi-character variable names like `educ`, `exper`, `wage`, `narr86`, `ptime86`, `inc86`, `lotsize`, `sqrft`, `bdrms`, `colGPA`, `rdintens`, `profmarg`, `infmort`, `pcinc`, `physic`, `popul` typed in default math mode render each letter as separate variables (`e·d·u·c` visually) rather than as single names.
- **Proposed:** Wrap in `\textit{}` or `\mathit{}` (e.g., `\mathit{educ}`). Apply consistently to match Wooldridge's typography.
- **Category:** Consistency / Quality

### Major 4: "$\hat\sigma$" mislabeled in regression tables
- **Lines:** 1135, 1143
- **Current:** `with $\hat\sigma$'s 0.586, 0.000044, 0.0462`
- **Problem:** These are coefficient standard errors, not the regression standard error $\hat\sigma$ (which is the residual standard error of the equation, a single scalar). Notation registry violation.
- **Proposed:** Replace with `with standard errors 0.586, 0.000044, 0.0462` or `with $\text{se}(\hat\beta_j)$'s ...`.
- **Category:** Consistency

### Major 5: Informal language ("don't" / "doesn't" / "we'll")
- **Lines:** 340, 454, 531, 607, 1200, 1499
- **Current:** `Rejecting A doesn't validate B`; `(we don't observe $\delta_3$)`; `Sometimes we don't even have...`; `Don't include...`; `Don't just delete`; `Tools we'll add later`
- **Proposed:** Replace contractions with `does not`, `do not`, `we will`. Academic slides avoid contractions.
- **Category:** Quality

---

## Minor (8)

### Minor 1: Examples skip 9.6 and 9.9
- **Lines:** 763 (Ex. 9.5) → 914 (Ex. 9.7)
- **Note:** Sequential expectation broken. If following Wooldridge exactly (skipping uncovered examples), add a brief note. Otherwise, renumber.
- **Category:** Consistency

### Minor 2: Inconsistent dash in regression tables
- **Lines:** 149, 150, 153, 477, 562, 564
- **Current:** Uses `---` (em-dash) for "no value" cells, where elsewhere `---` is used in prose.
- **Proposed:** Use `--` (en-dash) for empty cells; reserve `---` for prose.
- **Category:** Consistency

### Minor 3: Missing article — "Initial linear model overlooked"
- **Line:** 165
- **Current:** `Initial linear model overlooked important nonlinearities.`
- **Proposed:** `The initial linear model overlooked important nonlinearities.`
- **Category:** Grammar

### Minor 4: "putting $abil$ in the error causes"
- **Line:** 368
- **Current:** `putting $abil$ in the error causes`
- **Proposed:** `putting $abil$ into the error term causes`
- **Category:** Grammar / Quality

### Minor 5: "average tax rate as a substitute"
- **Line:** 714
- **Current:** `Researchers often use \textbf{average tax rate} as a substitute — measurement error.`
- **Proposed:** `Researchers often use the \textbf{average tax rate} as a substitute, introducing measurement error.`
- **Category:** Grammar

### Minor 6: Frame already at `[shrink=30]` (Two Polar Cases)
- **Lines:** 792–823
- **Note:** Heavy `shrink=30` indicates content already too big for the frame. Consider splitting into two frames for legibility rather than relying on aggressive shrink.
- **Category:** Overflow

### Minor 7: Unicode `✓`/`✗` in LAD tabular
- **Lines:** 1383–1390
- **Note:** Literal `✓`/`✗` rendered via XeLaTeX; works but not portable.
- **Proposed:** Use `\checkmark` and `$\times$` for safer typesetting.
- **Category:** Consistency

### Minor 8: Frame numbering note
- The deck uses Wooldridge's example numbering (9.1, 9.2, ..., 9.10). This is fine for textbook fidelity but creates the orphan "9.9 redux" problem (see Major 2).
- **Category:** Consistency

---

## Files Reviewed

- `Slides/Lecture08_Specification.tex` (61 PDF pages, ~1500 lines)

## Recommended Action

**Critical (Critical 1):** Fix equation tag ordering — students will be confused.

**Major:** Address SE transcription (Major 1), orphan example (Major 2), `\mathit{}` typography (Major 3), `\hat\sigma` mislabeling (Major 4), informal contractions (Major 5).

**Minor:** Defer or batch with stylistic polish pass.

Per protocol: this report does NOT modify the source file. Apply fixes after user review.
