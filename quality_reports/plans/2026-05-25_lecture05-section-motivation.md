# Plan: Lecture 05 — Add Motivation & Setup per Section (Wooldridge Ch. 6)

**Status:** APPROVED (user: "continue to do" — same pattern as Lecture 08)
**File:** `Slides/Lecture05_FurtherIssues.tex`

## Findings
- Deck already covers every Ch. 6 subsection (confirmed vs. learning objectives 6.1–6.9):
  §6-1 scaling + beta coef; §6-2a logs; §6-2b/c quadratics/interactions; §6-2d APE/
  centering; §6-3 adj R²/nonnested/over-controlling/variance reduction; §6-4 prediction
  CIs/intervals/residuals/log(y). **No omitted subsection.**
- Gap: no per-section "Motivation & Setup" opener — each section dives into content.

## Edits — add one signpost frame at the start of each of the 6 Ch. 6 sections
(Motivation box = the problem; Setup box = framework/notation + roadmap.)

| § | Section (deck) | Inserted before |
|---|----------------|-----------------|
| 6-1 | Data Scaling and Beta Coefficients | "Effects of Rescaling the Dependent Variable" |
| 6-2a | Logarithmic Functional Forms | "Review: Four Functional Forms" |
| 6-2b/c | Quadratic Models and Interactions | "Models with Quadratics" |
| 6-2d | Average Partial Effects and Centering | "Average Partial Effects (APE)" |
| 6-3 | Adjusted R² and Model Selection | "Adjusted R-Squared: Definition" |
| 6-4 | Prediction and Residual Analysis | "Confidence Intervals for Predictions" |

(Bootstrap section already opens with "The Bootstrap: Motivation"; not a Ch.6 section — leave it.)

## Constraints
- No \pause. Reuse highlightbox (Motivation) + keybox (Setup). Use existing macros
  (\Rsq, \aRsq, \E); avoid \APE (not defined here) — write \text{APE}; use \text{SST}.
- No Quarto sync (no .qmd for L05).

## Verify
3-pass XeLaTeX (TEXINPUTS=../Preambles); 0 errors, 0 undefined, check overflow; page count.
