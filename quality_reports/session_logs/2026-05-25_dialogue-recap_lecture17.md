# Dialogue Recap — Lecture 17 (LDV & Sample Selection)

**Date:** 2026-05-25
**Purpose:** A reusable record of this working session — what was asked, what was
decided, the key econometrics Q&A, and the exact commands — so it can be repeated
next time.

---

## 1. What was requested (in order)

1. "Make slides based on Chapter 17.pdf" (Wooldridge Ch. 17: Limited Dependent
   Variable Models & Sample Selection Corrections).
2. "The sequence of slides should be based on chapter 17. Explain the content
   mathematically."
   - Clarified via questions → **keep the slide sequence unchanged**; enrich the
     math *inside* slides, faithful to the textbook. Named priorities:
     **fractional response model + explicit fractional-logit form**, and the
     **inverse Mills ratio**.
3. Conceptual questions (answers in §3 below).
4. "Save the work" → committed + pushed to a branch (see §4).

## 2. What was built / changed

- `Slides/Lecture17_LDV_SampleSelection.tex` — 52-slide deck (was 49 at creation).
  Math enrichments, sequence unchanged:
  - Fractional response split into 2 slides: model construction (bounded mean,
    fractional logit `E(y|x)=Λ(β₀+xβ)=exp(β₀+xβ)/[1+exp(β₀+xβ)]`, fractional probit)
    + Bernoulli QMLE.
  - New "Score Equations" slide (general FOC; logit collapse `Σ(yᵢ−Λ(xᵢβ))xᵢ=0`).
  - New "Inverse Mills Ratio: Truncated-Normal Lemma" slide.
  - Rewrote Tobit partial-effects slide to *derive* `E[y|y>0]=xβ+σλ(xβ/σ)` and
    `∂E[y|x]/∂xⱼ=βⱼΦ(xβ/σ)`.
  - Rewrote Heckit slide to *derive* `E[y|z,s=1]=xβ+ρλ(zγ)`.
- Supporting: `Bibliography_base.bib` (Ch.17 refs), `.claude/rules/econometrics-knowledge-base.md`
  (§8), `CLAUDE.md` (lecture row), plan + session logs.

## 3. Key econometrics Q&A (the reusable teaching content)

### Q: Why can `E(y|x)` be written as `G(xβ)` for a fractional model? Is `∫ y f(y|x) dy = G`?
- `∫ y f(y|x) dy` is just the **definition** of `E(y|x)`. Setting it equal to
  `G(xβ)` is a **modeling assumption on the mean only** — not derived from a
  distribution.
- Justification: `y∈[0,1] ⇒ E(y|x)∈[0,1]`. A CDF `G:ℝ→(0,1)` keeps the mean in
  bounds; a linear `xβ` would not (the LPM defect).
- Binary case is the special case where `E(y|x)=P(y=1|x)` is an identity (mean =
  probability); fractional case has no such identity — we only restrict the mean.
- Deep reason it's legitimate: the Bernoulli quasi-log-likelihood is in the
  **linear exponential family**, and LEF-QMLE is **consistent whenever the mean
  is correctly specified**, regardless of the true distribution (Papke–Wooldridge
  1996). Price: Bernoulli variance is wrong ⇒ use **robust SEs**.

### Q: In the Bernoulli quasi-LL, can y = 1/3 and (1−y) = 2/3?
- Yes. For fractional `y`, both log-terms survive:
  `ℓᵢ = (1/3)·log G + (2/3)·log(1−G)` — a weighted average, weights summing to 1.
- A true Bernoulli RV cannot equal 1/3 ⇒ this is not the log of any real density
  ⇒ hence **quasi**-likelihood.
- Still works because `y` enters the **score only through the residual**
  `yᵢ − G(xᵢβ)`; consistency needs only `E[yᵢ−G(xᵢβ)|xᵢ]=0 ⇔ E(yᵢ|xᵢ)=G(xᵢβ)`.
- Example: 401(k) `prate=0.85` ⇒ contributes `0.85·log G + 0.15·log(1−G)`.

### Inverse Mills ratio (the object that recurs in Tobit AND Heckit)
- Truncated-normal lemma: `z~N(0,1) ⇒ E[z|z>c]=φ(c)/[1−Φ(c)]`,
  and `E[z|z>−c]=φ(c)/Φ(c) ≡ λ(c)`.
- Properties: `λ(c)>0`, strictly decreasing, `λ'(c)=−λ(c)[c+λ(c)]∈(−1,0)`.
- Used in Tobit `E[y|y>0,x]=xβ+σλ(xβ/σ)` and Heckit `E[y|z,s=1]=xβ+ρλ(zγ)`.

## 4. Workflow / commands (repeat next time)

```bash
# Compile (Windows MiKTeX, 3-pass XeLaTeX + bibtex)
cd "c:/Users/58219/my-project - 2/Slides"
export TEXINPUTS="c:/Users/58219/my-project - 2/Preambles;;"
xelatex -interaction=nonstopmode Lecture17_LDV_SampleSelection.tex
bibtex   Lecture17_LDV_SampleSelection
xelatex -interaction=nonstopmode Lecture17_LDV_SampleSelection.tex
xelatex -interaction=nonstopmode Lecture17_LDV_SampleSelection.tex

# Verify
pdfinfo Lecture17_LDV_SampleSelection.pdf | grep -i pages
grep "^!"  Lecture17_LDV_SampleSelection.log     # errors
grep -i "undefined" Lecture17_LDV_SampleSelection.log
grep "Overfull" Lecture17_LDV_SampleSelection.log
```

- Skills used: `create-lecture` (initial deck), `commit` (save).
- `gh` CLI is **not installed** here → PRs can't be created from the CLI; either
  install `gh`, or open a PR from the link Git prints on push.

## 5. Git state at session end (TODO for next time)

- Work committed `a6e775b`, pushed to branch `lecture17-ldv-sample-selection` on origin. ✅
- Local `main` has a merge commit on the OLD base; `origin/main` advanced 4 upstream
  template commits (pedrohcgs PRs #34/#35) → **diverged**. Push to main was rejected
  (correctly). Not reconciled (user said stop).
- **To finish next time** (pick one):
  - Reset local main to upstream, then re-merge:
    `git checkout main && git reset --hard origin/main && git merge --no-ff lecture17-ldv-sample-selection && git push origin main`
  - Or rebase the feature branch onto `origin/main` and open a PR (install `gh` first).
  - Decide whether this work belongs on the public template repo at all (see
    `.claude/rules/meta-governance.md`).
