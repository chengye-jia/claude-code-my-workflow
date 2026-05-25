# Plan: Lecture 08 — Add Motivation & Setup per Section

**Status:** APPROVED (direct user request)
**File:** `Slides/Lecture08_Specification.tex` (Wooldridge Ch. 9, 6 sections)

## Directive
"Revise slides — the motivation and setup for each section should be added."

## Approach
Insert one consistent **"<Topic>: Motivation & Setup"** signpost frame at the start
of each of the 6 sections. Each frame = a *Motivation* box (the economic/econometric
problem) + a *Setup* box (framework/notation + a 2–3 step roadmap of the section).
Keep roadmap-focused where a detailed motivation slide already follows, to avoid
duplicating equations / box fatigue.

| § | Section | Inserted before frame | Notes |
|---|---------|----------------------|-------|
| 9-1 | Functional Form Misspec. | "...: Definition" (after "Where We Are") | data ok, form wrong; F-test/RESET/nonnested roadmap |
| 9-2 | Proxy Variables | "Omitted Variables: A Bigger Problem" | OVB from unobservable; proxy strategy roadmap (no eq dup) |
| 9-3 | Random Slopes | "The Random Slopes Model" | heterogeneous slopes; α=E(a),β=E(b)=APE; when OLS works |
| 9-4 | Measurement Error | "Measurement Error: The Issue" | error in y vs x; CEV → attenuation preview |
| 9-5 | Missing/Nonrandom/Outliers | "Missing Data (§9-5a)" | 3-topic section; common test = is selection related to u? |
| 9-6 | LAD | "Least Absolute Deviations (LAD)" | OLS squared-loss fragility; absolute loss → cond. median |

## Constraints
- No `\pause`/overlays. Reuse existing boxes (highlightbox/keybox), `\mathit{}` for
  multichar var names, registry notation (\E, \Cov, \Var).
- No Quarto sync (no .qmd for L08).

## Verify
3-pass XeLaTeX (TEXINPUTS=../Preambles); 0 errors, 0 undefined cites, check overflow;
page count 61 → ~67.
