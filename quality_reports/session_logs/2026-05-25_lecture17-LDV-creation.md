# Session Log: 2026-05-25 -- Lecture 17 Creation (LDV & Sample Selection)

**Status:** COMPLETED

## Objective

Create a Beamer lecture from Wooldridge Ch. 17 (Limited Dependent Variable Models
and Sample Selection Corrections) following the `create-lecture` workflow. English
regular-sequence lecture (Ch. 17 source PDF, 51 pages).

## Changes Made

| File | Change | Reason | Quality Score |
|------|--------|--------|---|
| `Slides/Lecture17_LDV_SampleSelection.tex` | New 49-slide deck | Lecture creation | ~90/100 |

## Increment: Math Enrichment (same day, post-creation)

User directive: keep the slide sequence unchanged, but enrich the math within slides
faithfully to Ch. 17. Named priorities: build up the fractional response model + the
explicit fractional-logit functional form; develop the inverse Mills ratio. Plan:
`quality_reports/plans/2026-05-25_lecture17-math-enrichment.md`.

- Split Fractional Response into 2 slides: model construction (bounded mean,
  fractional logit $\Lambda(\beta_0+\mathbf{x}\beta)=\exp/[1+\exp]$, fractional probit)
  + QMLE estimation (Bernoulli quasi-LL, consistency, robust SEs, APE).
- Added a Score Equations slide (general FOC + logit collapse to $\sum(y_i-\Lambda)x_i=0$).
- Added a dedicated Inverse Mills Ratio lemma slide (truncated-normal lemma, properties).
- Rewrote Tobit partial-effects slide to *derive* $E[y|y>0]=x\beta+\sigma\lambda$ via the lemma.
- Rewrote Heckit slide to *derive* $E[y|z,s=1]=x\beta+\rho\lambda(z\gamma)$ via the lemma.
- Sequence unchanged. 49 → 52 pages. 3-pass XeLaTeX exit 0; 0 errors, 0 undefined
  citations, no overfull vbox/hbox. New slides visually verified in PDF.
| `Bibliography_base.bib` | +9 Ch.17 refs (Tobin, Heckman'76/'79, Papke–Wooldridge, Hausman–Wise, Santos Silva–Tenreyro, Evans–Schwab, Mroz, Chen–Roth) | Citations | — |
| `.claude/rules/econometrics-knowledge-base.md` | +Section 8 (Lecture 17 notation, anti-patterns, model table); +row 17 in progression | Knowledge base sync | — |
| `CLAUDE.md` | +Lecture 17 row in regular-lectures table | Project state | — |

## Design Decisions

| Decision | Alternatives Considered | Rationale |
|----------|------------------------|-----------|
| 5-Act structure (LDV zoo → binary/fractional → Poisson/Tobit → censored/truncated → selection/Heckit) | Single linear walk | Mirrors Ch.17 sections; clean conceptual pivots |
| Thread MROZ throughout (inlf/hours/log(wage)) | Separate dataset per topic | One running application; answers 3 Socratic questions |
| Replaced `examplebox` with plain centered table on the 401(k) frame | Keep examplebox + shrink | `examplebox` (tcolorbox enhanced skin) under `[shrink]` at the height boundary throws a spurious "Missing $ inserted"; plain table avoids it |
| Use `[shrink=8–12]` on dense table/box frames | Cut content aggressively | Matches house style (Lecture07 uses shrink); 85% font is documented for dense regression slides |

## Incremental Work Log

- Read full Ch.17 PDF (51pp), header.tex macros, Lecture07 style, bibliography.
- Drafted all 8 sections + synthesis + bridge in one pass.
- Iterated compilation: fixed (1) comma/`%`/`$` in `examplebox` titles breaking
  pgfkeys parser, (2) overfull vbox on ~27 frames via content trims + shrink,
  (3) persistent "Missing $" on the 401(k) examplebox-under-shrink frame.

## Learnings & Corrections

- [LEARN:beamer] `tcolorbox` titled environments (examplebox/definitionbox) re-parse
  the title for keys: bare commas, `%`, or unbraced specials in the title trigger
  "I do not know the key /tcb/..." errors. Keep titles comma-free (use em-dashes) or
  brace specials.
- [LEARN:beamer] An `examplebox` (tcolorbox `enhanced` skin) inside a `[shrink]` frame
  whose natural height sits at/just over the frame boundary emits a spurious
  "Missing $ inserted" at `\end{frame}` even though the source math is balanced. Fix:
  drop the box wrapper (plain centered table) or ensure the frame fits without shrink.
- [LEARN:beamer] `\shrink=N` is a *minimum*; beamer shrinks by as much as needed and
  warns "shrunk by X% instead of N%". A growing X across edits signals runaway
  content height, not a syntax issue.

## Verification Results

| Check | Result | Status |
|-------|--------|--------|
| 3-pass XeLaTeX + bibtex | exit 0 all passes | PASS |
| Compilation errors (`^!`) | 0 | PASS |
| Undefined citations | 0 (7 refs resolved via aer.bst) | PASS |
| Overfull vbox | 0 | PASS |
| Overfull hbox > 10pt | 0 (one 1.48pt, negligible) | PASS |
| Output | 49 pages, 261 KB | PASS |
| Visual spot-check | pp. 11–13, 17–19, 23 render cleanly | PASS |

## Open Questions / Blockers

- [ ] 6 table/figure frames shrink 13–15% (acceptable for dense slides; could split
      for 95+ excellence).
- [ ] Minor TikZ: "cross ≈ 11.5" label on the probit-vs-LPM figure lightly touches
      the LPM line.

## Next Steps

- [ ] (Optional) Run `/devils-advocate` and `/visual-audit` for a formal review pass.
- [ ] (Optional) Translate to Quarto when that workflow is scheduled.
