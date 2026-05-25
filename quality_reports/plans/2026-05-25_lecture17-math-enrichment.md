# Plan: Lecture 17 — Mathematical Content Enrichment

**Status:** APPROVED (clarified via AskUserQuestion 2026-05-25)
**File:** `Slides/Lecture17_LDV_SampleSelection.tex`

## Directive (from user)

- **Do NOT change the slide sequence.** The current section order already follows
  Wooldridge Ch. 17 (intro → §17-1 → §17-2 → §17-3 → §17-4 → §17-5 → §17-6 → synthesis).
- **Enrich the math within slides**, drawn faithfully from Chapter 17, so the deck
  maps onto the textbook for student reading.
- **Priority topics named by user:** (1) build up the fractional response model +
  the explicit fractional-logit functional form; (2) develop the inverse Mills ratio.

## Edits (sequence preserved; ~+3 net slides, 49 → ~52)

1. **Fractional Response (§17-2):** split the single "Fractional Outcomes" slide into
   two —
   - (a) *Building the model*: bounded conditional mean E(y|x)∈[0,1]; the LPM-style
     defect of a linear mean; fractional logit E(y|x)=Λ(β₀+xβ)=exp/[1+exp];
     fractional probit Φ(β₀+xβ); "same form, but a mean not a probability."
   - (b) *QMLE estimation*: reuse the Bernoulli quasi-log-likelihood for y∈[0,1];
     consistency needs only correct mean; robust SEs mandatory; APE with g=Λ(1−Λ).

2. **MLE (§17-1b):** add a new "Score Equations" slide — general FOC
   Σ[(yᵢ−G)g/(G(1−G))]xᵢ=0 and the logit collapse Σ(yᵢ−Λ)xᵢ=0 (OLS-normal-equation
   analogy; fitted probs average to ȳ).

3. **Inverse Mills ratio (§17-4a):** add a dedicated "Truncated-Normal Lemma" slide —
   E[z|z>c]=φ(c)/[1−Φ(c)], E[z|z>−c]=φ(c)/Φ(c)≡λ(c); properties (λ>0, decreasing,
   λ'(c)=−λ(c)[c+λ(c)]); flag it reappears in Tobit AND Heckit.

4. **Tobit partial effects (§17-4a):** rewrite to *derive* E[y|y>0,x]=xβ+σλ(xβ/σ)
   and E[y|x]=Φ(xβ/σ)xβ+σφ(xβ/σ) via the lemma; show ∂E[y|x]/∂xⱼ=βⱼΦ(xβ/σ).

5. **Heckit omitted-variable slide (§17-6b):** rewrite to *derive*
   E[y|z,s=1]=xβ+ρλ(zγ) from E(u|v)=ρv (joint normality) + the same lemma.

## Verification
- 3-pass XeLaTeX (TEXINPUTS=../Preambles). Check 0 errors, 0 undefined cites,
  no overfull vbox, page count.
- No Quarto sync (no .qmd for Lecture 17).
