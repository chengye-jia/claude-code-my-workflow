# Econometrics Knowledge Base — Intermediate Econometrics (SUFE)
# Textbook: Wooldridge, Introductory Econometrics, 8th edition

<!-- Path: .claude/rules/econometrics-knowledge-base.md -->
<!-- Purpose: Single source of truth for notation, conventions, and content
     across all 16 lectures. Claude reads this before every review task.
     Update this file as lectures are created. -->

---

## 1. Standard Notation Registry

All lectures must use these conventions. Report any deviation as a MINOR issue.

### Greek Letters

| Symbol | LaTeX macro | Meaning |
|--------|-------------|---------|
| $\beta_0$ | `\beta_0` | Intercept |
| $\beta_j$ | `\beta_j` | Slope on $x_j$ |
| $\hat{\beta}_j$ | `\bhat_j` or `\hat{\beta}_j` | OLS estimator of $\beta_j$ |
| $\varepsilon$ | `\eps` | Population error term |
| $\hat{\varepsilon}$ or $\hat{u}$ | `\epsh` or `\uh` | OLS residual |
| $\sigma^2$ | `\sigma^2` | Error variance |
| $\hat{\sigma}^2$ | `\hat{\sigma}^2` | Estimated error variance |
| $\rho$ | `\rho` | Autocorrelation coefficient (AR(1)) |
| $\lambda$ | `\lambda` | Generalized least squares transform / eigenvalue |

### Operators and Functions

| Symbol | LaTeX macro | Meaning |
|--------|-------------|---------|
| $\mathbb{E}[X]$ | `\E[X]` | Expectation of X |
| $\mathbb{E}[Y|X]$ | `\E[Y|X]` | Conditional expectation |
| $\text{Var}(X)$ | `\Var(X)` | Variance |
| $\text{Cov}(X,Y)$ | `\Cov(X,Y)` | Covariance |
| $\text{Corr}(X,Y)$ | `\Corr(X,Y)` | Correlation |
| $\text{plim}$ | `\plim` | Probability limit |
| $\text{se}(\hat\beta)$ | `\se(\bhat)` | Standard error |
| $\text{Avar}(\hat\beta)$ | `\avar(\bhat)` | Asymptotic variance |

### Convergence

| Symbol | LaTeX macro | Meaning |
|--------|-------------|---------|
| $\overset{p}{\to}$ | `\pto` | Convergence in probability |
| $\overset{d}{\to}$ | `\dto` | Convergence in distribution |
| $\overset{\text{iid}}{\sim}$ | `\iid` | i.i.d. distributed |
| $\overset{a}{\sim}$ | `\asim` | Approximately distributed |

### Matrix Notation (used in matrix form lectures)

| Symbol | LaTeX macro | Meaning |
|--------|-------------|---------|
| $\mathbf{X}$ | `\Xb` | $n \times (k+1)$ design matrix |
| $\mathbf{y}$ | `\yb` | $n \times 1$ outcome vector |
| $\boldsymbol{\beta}$ | `\betab` | $(k+1) \times 1$ parameter vector |
| $\boldsymbol{\varepsilon}$ | `\epsb` | $n \times 1$ error vector |

### Econometric Estimator Abbreviations

| Symbol | LaTeX macro | Meaning |
|--------|-------------|---------|
| $\text{OLS}$ | `\OLS` | Ordinary Least Squares |
| $\text{IV}$ | `\IV` | Instrumental Variables |
| $\text{2SLS}$ | `\TSLS` | Two-Stage Least Squares |
| $\text{GMM}$ | `\GMM` | Generalized Method of Moments |
| $\text{FE}$ | `\FE` | Fixed Effects |
| $\text{RE}$ | `\RE` | Random Effects |
| $\text{DiD}$ | `\DID` | Difference-in-Differences |
| $\text{RD}$ | `\RD` | Regression Discontinuity |

### Goodness-of-Fit

| Symbol | LaTeX macro | Meaning |
|--------|-------------|---------|
| $\text{SSR}$ | `\SSR` | Sum of Squared Residuals |
| $\text{SSE}$ | `\SSE` | Explained Sum of Squares |
| $\text{SST}$ | `\SST` | Total Sum of Squares ($= \text{SSE} + \text{SSR}$) |
| $R^2$ | `\Rsq` | R-squared |
| $\bar{R}^2$ | `\aRsq` | Adjusted R-squared |

---

## 2. Wooldridge MLR Assumption Reference

Use these exact names and numbering in every lecture that invokes OLS properties.

| Assumption | Name | Content |
|------------|------|---------|
| **MLR.1** | Linearity in parameters | $y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u$ |
| **MLR.2** | Random sampling | $\{(x_i, y_i): i=1,\ldots,n\}$ is a random sample from the population model |
| **MLR.3** | No perfect collinearity | No exact linear relationship among regressors; $\mathbf{X}$ has full column rank |
| **MLR.4** | Zero conditional mean | $\mathbb{E}[u \mid x_1, \ldots, x_k] = 0$ |
| **MLR.5** | Homoskedasticity | $\text{Var}(u \mid x_1, \ldots, x_k) = \sigma^2$ |
| **MLR.6** | Normality of errors | $u \mid x_1,\ldots,x_k \sim \mathcal{N}(0, \sigma^2)$ |

**What each set implies:**
- MLR.1–4 → OLS is **unbiased** and **consistent**
- MLR.1–5 → OLS is **BLUE** (Gauss-Markov theorem); exact variance formula holds
- MLR.1–6 → **Exact** $t$ and $F$ distributions hold in finite samples
- MLR.1–4 + large $n$ → **Asymptotic normality** of OLS (MLR.5 not needed with robust SEs)

---

## 3. Lecture Progression

Track what has been introduced in each lecture. Update as slides are created.

| Lecture | Topic | Key Concepts Introduced | Key Assumptions Used |
|---------|-------|------------------------|---------------------|
| 1 | Simple Regression | SRF, PRF, $\hat\beta_0$, $\hat\beta_1$, $R^2$, SSR, SST | MLR.1–4 (simple case) |
| 2 | Multiple Regression: Estimation | Multiple regressors, partialling out, FWL, omitted variable bias | MLR.1–4 |
| 3 | Multiple Regression: Inference | $t$-test, $F$-test, confidence intervals, $p$-value | MLR.1–6 |
| 4 | OLS Asymptotics | Consistency, asymptotic normality, large-sample $t$ and $F$ | MLR.1–4 (+ weak conditions) |
| 5 | Further Issues in OLS | Scaling, functional forms (log, quadratic, interaction), $\Delta\hat{y}$ | MLR.1–4 |
| 6 | Qualitative Variables | Binary, categorical, interaction with dummy | MLR.1–4 |
| 7 | Heteroskedasticity | Definition, consequences for OLS, robust SEs, WLS, FGLS | MLR.1–4 (MLR.5 violated) |
| 8 | Specification & Data Issues | RESET, omitted variables, proxy variables, measurement error, missing data | MLR.1–4 |
| 9 | Basic Time Series OLS | Stationary TS, AR(1), static models, FDL models | TS.1–5 (Wooldridge Ch. 10) |
| 10 | Further Time Series Issues | Trends, seasonality, spurious regression, cointegration | TS assumptions |
| 11 | Serial Correlation & TS Heteroskedasticity | Breusch-Godfrey test, Cochrane-Orcutt, ARCH/GARCH | TS.1–5 (TS.5 relaxed) |
| 12 | Pooling Cross Sections & DiD | Repeated cross sections, natural experiments, DiD, parallel trends | MLR.1–4 + parallel trends |
| 13 | Advanced Panel Data | Unobserved effects, FE, RE, Hausman test, first differences | Strict exogeneity for FE |
| 14 | Instrumental Variables / 2SLS | Endogeneity, IV assumptions, 2SLS, weak instruments, over-identification | IV relevance + exogeneity |
| 15 | Limited Dependent Variables | Linear probability model, probit, logit, tobit, APE, PEA | MLR.1–4 (nonlinear) |
| 16 | Advanced Causal Inference | RD, DID extensions, synthetic control, matching overview (Ch. 19) | Design-based identification |
| 17 | LDV & Sample Selection (Ch. 17) | Logit/probit, APE/PEA, fractional logit (QMLE), Poisson/exponential mean, Tobit (corner solution), inverse Mills ratio, censored & truncated regression, Heckit | MLE/QMLE; latent normal/logistic; selection exogeneity |

---

## 4. R Package Registry

Use these packages for the corresponding estimators. Never use a non-standard approach when a canonical package exists.

| Method | Package | Function | Notes |
|--------|---------|----------|-------|
| OLS | base R | `lm()` | Always use `summary(model, robust=FALSE)` — default SEs |
| Robust SEs | `sandwich` + `lmtest` | `vcovHC(model, type="HC1")` + `coeftest()` | HC1 is Stata-default (HC1 = HC/(n-k-1)*n) |
| HAC SEs (TS) | `sandwich` | `vcovHAC(model)` or `NeweyWest(model)` | Use for time series with serial correlation |
| IV / 2SLS | `AER` | `ivreg(y ~ x | z)` | Do NOT do manual 2SLS — gives wrong SEs |
| Panel FE | `plm` | `plm(y ~ x, model="within")` | Add `effect="twoways"` for two-way FE |
| Panel RE | `plm` | `plm(y ~ x, model="random")` | Hausman test via `phtest()` |
| First differences | `plm` | `plm(y ~ x, model="fd")` | |
| Probit | base R | `glm(y ~ x, family=binomial(link="probit"))` | |
| Logit | base R | `glm(y ~ x, family=binomial(link="logit"))` | |
| Tobit | `AER` | `tobit(y ~ x, left=0)` | |
| Cluster SEs | `sandwich` | `vcovCL(model, cluster=~id)` | For panel/DiD |
| Weak instrument test | base R | `summary(first_stage)$fstatistic` | Rule of thumb: F > 10 |

---

## 5. Common Anti-Patterns

These are mistakes students (and slides) commonly make. Flag them during review.

### Econometric Anti-Patterns

| Anti-pattern | Correct approach |
|---|---|
| "OLS is unbiased because we minimize SSR" | Unbiasedness requires MLR.1–4 (algebraic minimization just gives FOC) |
| "High $R^2$ means the model is good" | $R^2$ measures fit, not causal validity or out-of-sample performance |
| "$\hat\beta$ is the causal effect of $x$" | Only if MLR.4 holds — requires explicit argument |
| "The coefficient is significant" | Always state: significant at what level? Against what null? |
| "Robust SEs fix endogeneity" | Robust SEs fix MLR.5 violation only; endogeneity violates MLR.4 |
| "IV always solves endogeneity" | IV requires BOTH relevance AND exogeneity of instrument |
| "FE controls for all confounders" | FE controls for time-invariant confounders only; time-varying OVB remains |
| "Probit coefficient = marginal effect" | Probit coefficients are NOT marginal effects; compute APE or PEA |
| "We clustered SEs, so we're fine" | Clustering addresses within-cluster correlation but not treatment assignment |

### Notation Anti-Patterns

| Don't use | Use instead | Reason |
|---|---|---|
| $E[y]$ | $\mathbb{E}[y]$ or `\E[y]` | `\E` macro defined in header.tex |
| $Var(u)$ | $\text{Var}(u)$ or `\Var(u)` | Use operator form |
| $\hat{\beta}$ for multiple $\beta$s | $\hat{\beta}_j$ | Always subscript when $k>1$ |
| $u$ and $\varepsilon$ interchangeably | Pick one per lecture and stick to it | Consistency |
| "plim $\hat\beta = \beta$" | $\hat\beta \overset{p}{\to} \beta$ | Standard notation |

---

## 6. Design Principles for This Course

**Slides should:**
- State the Wooldridge assumption (MLR.1–6 or TS.1–5) before claiming a property
- Motivate with an economic question before giving econometrics
- Show at least one real data example per major estimator (from Wooldridge datasets)
- Display regression output in LaTeX tabular form (not raw R console output)
- Separate "what it is" (definition box) from "why it matters" (key box) from "the result" (highlight box)

**Slides should NOT:**
- Use `\pause` or overlay commands (per `no-pause-beamer.md` rule)
- Claim causal interpretation without stating the identification assumption
- Show more than one major concept per slide
- Use R console output screenshots (typeset it properly)

---

## 7. Binary Choice Model Notation (Special Topics LectureS1–S3)

All special topics lectures use simplified Chinese text. Math notation follows this registry.

### Link Functions

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| $\Phi(z)$ | `\Phi(z)` | Standard normal CDF — probit link |
| $\phi(z)$ | `\phi(z)` | Standard normal PDF |
| $\Lambda(z)$ | `\Lambda(z)` | Logistic CDF: $\frac{e^z}{1+e^z}$ — logit link |
| $\lambda(z)$ | `\lambda(z)` | Logistic PDF: $\Lambda(z)[1-\Lambda(z)]$ |
| $G(z)$, $g(z)$ | `G(z)`, `g(z)` | Generic link CDF and density (lecture-level notation) |
| $F_\varepsilon(z)$ | `F_\varepsilon(z)` | CDF of error term $\varepsilon_i$ (general model) |

### Marginal Effects

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| $\text{APE}_j$ | `\text{APE}_j` | Average Partial Effect of $x_j$: $\frac{1}{n}\sum_i g(x_i\hat\beta)\hat\beta_j$ |
| $\text{PEA}_j$ | `\text{PEA}_j` | Partial Effect at the Mean: $g(\bar x\hat\beta)\hat\beta_j$ |

### Log-Likelihood and MLE

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| $\ell(\beta)$ | `\ell(\beta)` | Log-likelihood: $\sum_i[y_i\ln G(x_i\beta)+(1-y_i)\ln(1-G(x_i\beta))]$ |
| $\mathcal{I}(\beta)$ | `\mathcal{I}(\beta)` | Fisher information matrix |
| $\hat\beta_{\text{MLE}}$ | `\hat\beta_{\text{MLE}}` | MLE estimator |
| $\tilde\rho^2$ | `\tilde\rho^2` | McFadden pseudo-$R^2$: $1 - \ell_u/\ell_r$ |

### Semiparametric Notation (LectureS3)

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| $E[Y|X=x] = G(x'\beta)$ | — | Single-index model |
| $\hat G_{-i}(x'\beta)$ | — | Leave-one-out kernel estimator of $G$ at index value $x'\beta$ |

### Binary Choice Anti-Patterns

| Anti-pattern | Correct approach |
|---|---|
| "Probit系数 = 边际效应" | Wrong: $\partial P/\partial x_j = \phi(x_i\hat\beta)\hat\beta_j$ varies by observation |
| "Logit系数 = 对数优势比" | Only linear index; exponentiate for odds ratio: $\exp(\hat\beta_j)$ |
| "Pseudo-$R^2$ = $R^2$" | Not comparable; McFadden's $\tilde\rho^2 \in [0,1]$, 0.2–0.4 is "good" |
| "半参数估计量的收敛速度是 $\sqrt{n}$" | Only $\hat\beta$; $\hat G$ converges slower (nonparametric rate) |
| "最大得分估计量渐近正态" | Wrong: cube-root $n$ rate, non-normal limit (Kim–Pollard 1990) |
| "固定效应Probit一致" | Wrong for fixed $T$: incidental parameters problem → inconsistent |
| "忽略异质性只影响效率" | Wrong: omitted $\alpha_i$ in probit/logit causes inconsistency |

### Binary Choice: What Each Estimator Assumes

| Estimator | Distribution of $\varepsilon$ | Convergence rate of $\hat\beta$ | Notes |
|-----------|-------------------------------|--------------------------------|-------|
| Probit | $\mathcal{N}(0,1)$ | $\sqrt{n}$ | MLE; efficient under correct spec |
| Logit | Logistic | $\sqrt{n}$ | MLE; efficient under correct spec |
| LPM (OLS) | Uniform (implicit) | $\sqrt{n}$ | Consistent for APE under MLR.1–4 |
| Ichimura (1993) | Unknown (symmetric) | $\sqrt{n}$ | SLS; two-step |
| Klein–Spady (1993) | Unknown | $\sqrt{n}$ | Semiparametric efficient |
| Manski (1975) | Unknown | $n^{1/3}$ | Non-normal limit; no scale norm. |
| Horowitz (1992) | Unknown (smooth) | $n^{2/5}$ | Smoothed max score |

---

## 8. Limited Dependent Variables & Sample Selection (Lecture 17, English, Wooldridge Ch. 17)

English regular-sequence lecture. Math notation follows this registry; shares link-function
notation with §7 (binary choice) but extends to corner solutions, counts, and selection.

### New Notation (Lecture 17)

| Symbol | LaTeX (lecture-local macros) | Meaning |
|--------|------------------------------|---------|
| $\mathbf{x}\boldsymbol{\beta}$ | `\xbeta` | Linear index $\beta_1 x_1 + \cdots + \beta_k x_k$ |
| $\mathbf{x}_i\boldsymbol{\beta}$ | `\xib` | Index for observation $i$ |
| $\bar{\mathbf{x}}$ | `\xbar` | Vector of regressor means (for PEA) |
| $\text{APE}_j$ | `\APE` | Average Partial Effect: $[n^{-1}\sum_i g(\hat\beta_0+\xib)]\hat\beta_j$ |
| $\text{PEA}_j$ | `\PEA` | Partial Effect at the Average: $g(\hat\beta_0+\bar{\mathbf{x}}\hat\beta)\hat\beta_j$ |
| $y^{*}$ | `y^{*}` | Latent variable (probit/logit/Tobit/censored) |
| $\lambda(c)=\phi(c)/\Phi(c)$ | `\lambda(c)` | Inverse Mills ratio (Tobit cond.\ mean & Heckit) |
| $w_i=\min(y_i,c_i)$ | — | Censored observation; $c_i$ = censoring threshold |
| $s=\mathbf{1}[\mathbf{z}\boldsymbol\gamma+v\ge0]$ | — | Selection indicator; $\mathbf{z}$ = selection regressors |
| $\hat\lambda_i$ | `\hat\lambda` | Estimated inverse Mills ratio (Heckit second stage) |
| $\rho$ | `\rho` | $\Corr(u,v)$ in selection model; $\rho=0 \Rightarrow$ no selection bias |

**Note:** `\xbeta`, `\xib`, `\xbar`, `\APE`, `\PEA` are defined in the Lecture 17 preamble block,
NOT in `Preambles/header.tex`. If reused elsewhere, redefine locally or promote to header.

### Lecture 17 Anti-Patterns

| Anti-pattern | Correct approach |
|---|---|
| "Probit/logit coefficient = marginal effect" | Effect is $g(\xbeta)\hat\beta_j$; report APE (preferred) or PEA |
| "Compare raw Tobit and OLS coefficients" | Scale Tobit by $\Phi(\xbeta/\sigma)$ first; APE $=\beta_j\Phi(\xbeta/\sigma)$ |
| "$\sigma$ in Tobit is an ancillary nuisance" | $\sigma$ enters the partial effects directly — economically meaningful |
| "Tobit = censored regression" | Tobit models corner-solution *behavior*; censored reg fixes a *data* defect |
| "Use $\log(1+y)$ for nonneg.\ $y$" | Not scale-invariant; use exponential mean + Poisson QMLE (Chen–Roth 2024) |
| "Poisson requires $y$ to be a count with Var = mean" | Poisson QMLE consistent if *mean* correct; inflate SEs for overdispersion |
| "OLS on a selected sample is always biased" | Only if selection is *endogenous* (on $y$ or $u$); exogenous selection is fine |
| "Heckit works with $\mathbf{z}=\mathbf{x}$" | Need an exclusion restriction: a $z$ affecting selection but not the outcome |
| "Significant $\hat\lambda$ irrelevant" | $t$ on $\hat\lambda$ is the test for selection bias ($H_0:\rho=0$) |

### Lecture 17: What Each Model Handles

| Model | Outcome type | Estimation | Effect tool |
|-------|--------------|------------|-------------|
| Logit / Probit | Binary $\{0,1\}$ | MLE | APE / PEA |
| Fractional logit | Fractional $[0,1]$ | QMLE (robust SE) | APE |
| Poisson / exponential mean | Count / nonneg.\ $y\ge0$ | QMLE (robust SE) | $100\beta_j\approx\%\Delta\E(y)$ |
| Tobit | Corner solution $y\ge0$ | MLE ($\beta,\sigma$) | APE $=\beta_j\Phi(\xbeta/\sigma)$ |
| Censored normal reg. | Top-coded / duration | MLE | $\beta_j$ as in linear model |
| Truncated normal reg. | Sub-population excluded | MLE | $\beta_j$ as in linear model |
| Heckit (two-step) | Incidental truncation | Probit + OLS w/ $\hat\lambda$ | inverse Mills + $t$-test on $\rho$ |

### Lecture 17 Running Application & Datasets

- **MROZ** ($n=753$ married women): threaded throughout — $inlf$ (binary, logit/probit),
  $hours$ (corner solution, Tobit), $\log(wage)$ (selection, Heckit).
- **401(k)** ($prate$, $n=4{,}075$): fractional logit (Papke–Wooldridge 1996).
- **CRIME1** ($narr86$): Poisson regression for arrest counts.
- **RECID** ($durat$, 62% censored): censored normal regression / duration.
