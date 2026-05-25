# CLAUDE.MD -- Intermediate Econometrics + Special Topics (SUFE)

**Project:** Intermediate Econometrics + Special Topics: Binary Choice Models
**Institution:** Shandong University of Finance and Economics (山东财经大学)
**Textbook:** Wooldridge, *Introductory Econometrics*, 8th edition
**Special Topics Sources:** Hansen PhD notes (Ch.5), Hansen Econometrics (Ch.25), Li & Racine (2007), Horowitz (2009), 高级计量经济学及STATA应用
**Branch:** main
**Language:** Special topics lectures (LectureS1–S3) are entirely in **simplified Chinese**; regular lectures (Lecture01–16) are in English.

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile/render and confirm output at the end of every task
- **Single source of truth** -- Beamer `.tex` is authoritative; Quarto `.qmd` derives from it
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md

---

## Folder Structure

```
my-project/
├── CLAUDE.MD                    # This file
├── .claude/                     # Rules, skills, agents, hooks
├── Bibliography_base.bib        # Centralized bibliography
├── Figures/                     # Figures and images
├── Preambles/header.tex         # LaTeX preamble (load with TEXINPUTS=../Preambles:)
├── Slides/                      # Beamer .tex files (authoritative source)
├── Quarto/                      # RevealJS .qmd files + sufe-clean.scss theme
├── docs/                        # GitHub Pages (auto-generated)
├── scripts/                     # Utility scripts + R code
├── quality_reports/             # Plans, session logs, merge reports
├── explorations/                # Research sandbox (see rules)
├── templates/                   # Session log, quality report templates
└── master_supporting_docs/      # Papers, textbook, existing slides
```

---

## Commands

```bash
# LaTeX (3-pass, XeLaTeX only) — Windows MiKTeX
cd "c:/Users/58219/my-project - 2/Slides"
TEXINPUTS="c:/Users/58219/my-project - 2/Preambles;;" xelatex -interaction=nonstopmode file.tex
BIBINPUTS="..:$BIBINPUTS" bibtex file
TEXINPUTS="c:/Users/58219/my-project - 2/Preambles;;" xelatex -interaction=nonstopmode file.tex
TEXINPUTS="c:/Users/58219/my-project - 2/Preambles;;" xelatex -interaction=nonstopmode file.tex

# Deploy Quarto to GitHub Pages
./scripts/sync_to_docs.sh LectureN

# Quality score
python scripts/quality_score.py Quarto/file.qmd
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Commit | Good enough to save |
| 90 | PR | Ready for deployment |
| 95 | Excellence | Aspirational |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/compile-latex [file]` | 3-pass XeLaTeX + bibtex |
| `/deploy [LectureN]` | Render Quarto + sync to docs/ |
| `/extract-tikz [LectureN]` | TikZ → PDF → SVG |
| `/proofread [file]` | Grammar/typo/overflow review |
| `/visual-audit [file]` | Slide layout audit |
| `/pedagogy-review [file]` | Narrative, notation, pacing review |
| `/review-r [file]` | R code quality review |
| `/qa-quarto [LectureN]` | Adversarial Quarto vs Beamer QA |
| `/slide-excellence [file]` | Combined multi-agent review |
| `/translate-to-quarto [file]` | Beamer → Quarto translation |
| `/validate-bib` | Cross-reference citations |
| `/devils-advocate` | Challenge slide design |
| `/create-lecture` | Full lecture creation |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |
| `/interview-me [topic]` | Interactive research interview |
| `/review-paper [file]` | Manuscript review |
| `/data-analysis [dataset]` | End-to-end R analysis |
| `/learn [skill-name]` | Extract discovery into persistent skill |
| `/context-status` | Show session health + context usage |
| `/deep-audit` | Repository-wide consistency audit |

---

## Beamer Custom Environments

Defined in `Preambles/header.tex`. Quarto equivalents use CSS classes from `sufe-clean.scss`.

| Environment            | Effect                         | Use Case                                |
|------------------------|--------------------------------|-----------------------------------------|
| `keybox`               | Gold left-border box           | Key definitions, stated assumptions     |
| `highlightbox`         | Yellow left-border box         | Important theorems, main results        |
| `definitionbox{Title}` | Blue titled full-border box    | Formal definitions (OLS, IV, GMM, etc.) |
| `examplebox{Title}`    | Light background titled box    | Empirical examples, data applications   |
| `assumptionbox`        | Gold full-border box           | Numbered assumptions (MLR.1–MLR.6)      |

## Quarto CSS Classes

From `Quarto/sufe-clean.scss` — use as `::: {.classname}` div blocks.

| Class           | Effect                    | Use Case                              |
|-----------------|---------------------------|---------------------------------------|
| `.keybox`       | Gold left-border          | Key definitions, stated assumptions   |
| `.highlightbox` | Yellow left-border        | Important theorems, main results      |
| `.methodbox`    | Blue left-border          | Estimators, formal definitions        |
| `.assumptionbox`| Gold full-border          | Numbered assumptions (MLR.1–MLR.6)    |
| `.resultbox`    | Gold background           | Main propositions, key results        |
| `.eqbox`        | Light blue background     | Key equations to highlight            |
| `.smaller`      | 85% font size             | Dense regression output slides        |
| `.compact`      | Tight paragraph spacing   | Dense content slides                  |
| `.positive`     | Green bold text           | Identified / satisfied / good         |
| `.negative`     | Red bold text             | Violated / biased / problematic       |
| `.hi`           | Bold blue text            | Inline emphasis (blue)                |
| `.hi-gold`      | Bold gold text            | Inline emphasis (gold)                |

---

## Current Project State

### Regular Lectures (English, Wooldridge sequence)

| # | Beamer file | Quarto | Topic (Wooldridge 8th ed.) |
|---|-------------|--------|---------------------------|
| 1  | `Lecture01_SimpleOLS.tex` ✓       | --  | Simple Regression Model (40 slides, compiled) |
| 2  | `Lecture02_MultipleOLS.tex`       | --  | Multiple Regression: Estimation |
| 3  | `Lecture03_Inference.tex`         | --  | Multiple Regression: Inference |
| 4  | `Lecture04_Asymptotics.tex`       | --  | OLS Asymptotics |
| 5  | `Lecture05_FurtherIssues.tex`     | --  | Further Issues in OLS |
| 6  | `Lecture06_QualitativeData.tex`   | --  | Qualitative Variables |
| 7  | `Lecture07_Heteroskedasticity.tex`| --  | Heteroskedasticity |
| 8  | `Lecture08_Specification.tex`     | --  | Specification & Data Issues |
| 9  | `Lecture09_TimeSeriesBasic.tex`   | --  | Basic Time Series OLS |
| 10 | `Lecture10_TimeSeriesFurther.tex` | --  | Further Time Series Issues |
| 11 | `Lecture11_SerialCorrelation.tex` | --  | Serial Correlation & Heteroskedasticity in TS |
| 12 | `Lecture12_PooledCross.tex`       | --  | Pooling Cross Sections & Diff-in-Diff |
| 13 | `Lecture13_Panel.tex`             | --  | Advanced Panel Data Methods |
| 14 | `Lecture14_IV.tex`                | --  | Instrumental Variables / 2SLS |
| 15 | `Lecture15_LDV.tex`               | --  | Limited Dependent Variables |
| 16 | `Lecture16_CausalInference.tex`   | --  | Advanced Methods for Causal Inference (Ch. 19) |
| 17 | `Lecture17_LDV_SampleSelection.tex` ✓ | -- | Limited Dependent Variables & Sample Selection (Ch. 17): logit/probit, APE/PEA, fractional logit, Poisson, Tobit, censored/truncated reg., Heckit (49 slides, compiled) |

### Special Topics: Binary Choice Models (全中文, Graduate Level)

Content language: **Simplified Chinese**. Math notation: LaTeX (unchanged).
Sources: Hansen PhD notes Ch.5, Hansen Econometrics Ch.25, 高级计量经济学及STATA应用, Li & Racine (2007), Horowitz (2009).

| # | Beamer file | Quarto | Topic |
|---|-------------|--------|-------|
| S1 | `LectureS1_BinaryChoice_Parametric.tex`     | -- | 参数方法：LPM、Probit、Logit、边际效应、IV Probit、遗漏异质性 (~135 slides) |
| S2 | `LectureS2_BinaryChoice_Nonparametric.tex`  | -- | 非参数方法：核估计、条件概率、混合数据核、规格检验 (~95 slides) |
| S3 | `LectureS3_BinaryChoice_Semiparametric.tex` | -- | 半参数方法：单指标模型、Ichimura、Klein-Spady、最大得分估计量 (~100 slides) |
