# Plan: LectureS3_BinaryChoice_Semiparametric.tex

**Status:** APPROVED — UPDATED 2026-05-06 to Option B (PSS + Han MRC + Lewbel added)
**Date:** 2026-04-27 (initial), 2026-05-06 (revised)
**Target file:** `Slides/LectureS3_BinaryChoice_Semiparametric.tex`
**Language:** Simplified Chinese (math LaTeX, English keywords on first occurrence)
**Style template:** LectureS1/LectureS2 conventions
**Target size:** ~112 main + ~15 appendix = ~127 slides, ~6,800 lines

## Approved structure (12 parts + appendix)

| Part | Slides | Topic | Source |
|---|---|---|---|
| 1. 半参数方法的动因 | 10 | Motivation, three-way comparison | Class 5 §1, Hansen Ch.25 |
| 2. 部分线性模型（简介） | 5 | Robinson 1988 brief bridge | Class 5 §2 |
| 3. 单指标模型：定义与识别 | 10 | SIM, location/scale normalization | Class 5 §3.3, Hansen, Li-Racine |
| 4. Ichimura (1993) 半参数最小二乘 | 18 | Full theoretical treatment | Ichimura 1993, Class 5 §3.3 |
| 5. Klein-Spady (1993) 半参数 MLE | 14 | Likelihood + efficiency bound | KS 1993, Newey 1990 |
| 6. Manski (1975) 最大得分 | 12 | Median restriction, cube-root | Manski 1975/1985, Kim-Pollard |
| 7. Horowitz (1992) 平滑最大得分 | 10 | n^{2/5}, Edgeworth | Horowitz 1992 |
| 8. 检验与诊断 | 8 | Hausman, link-function | various |
| 9. 其他半参数模型（简介） | 3 | Additive, varying-coef, multi-index | Class 5 §3.1-3.2 |
| 10. 倾向得分与 IPW 应用 | 6 | Propensity score AS binary choice | Class 6 §2 |
| 11. 实证应用：MROZ | 10 | Five-method comparison | Wooldridge MROZ |
| 12. 总结 | 6 | Comparison tables, decision tree | — |
| **Appendix** | **15** | Theoretical proofs | various |

## Key decisions

- PLM trimmed 14→5 (not binary choice; conceptual bridge only)
- Other models trimmed 6→3 (same reason)
- RDD excluded (belongs in Lecture16)
- IPW kept at 6 (propensity score IS binary choice)
- Appendix kept at 15 proofs (Robinson PLM proofs combined)
- MROZ dataset for empirical
- Citations inline per S1/S2 (`\citep{ichimura1993}`)
- More theoretical depth — slides readable standalone

## Implementation in 5 chunks

| Chunk | Lines | Frames |
|---|---|---|
| 1 | ~1100 | Preamble + TOC + Parts 1-3 (frames 1-25) |
| 2 | ~1500 | Part 4 Ichimura (frames 26-43) |
| 3 | ~1400 | Parts 5-6 Klein-Spady + Manski (frames 44-69) |
| 4 | ~1400 | Parts 7-10 Horowitz + tests + extensions + IPW (frames 70-95) |
| 5 | ~1400 | Parts 11-12 + Appendix 15 proofs (frames 96-127) |

## Bibliography additions (~12 entries)

Robinson 1988, Ichimura 1993, Klein-Spady 1993, Manski 1975, Manski 1985, Kim-Pollard 1990, Horowitz 1992, Newey 1990, Newey-Powell 2003, Powell-Stock-Stoker 1989, Hirano-Imbens-Ridder 2003, Severini-Staniswalis 1994.

## Verification gates

1. 3-pass XeLaTeX compiles with zero errors
2. No `\pause` / overlay commands
3. CJK rendering with Microsoft YaHei + `\XeTeXlinebreaklocale "zh"`
4. All 15 `\hyperlink{proof-cN}` ↔ `\hypertarget{proof-cN}` pairs match
5. Notation registry consistency (header.tex macros)
6. All cited papers resolve in `Bibliography_base.bib`
7. MROZ R code compiles and produces the comparison table

## Critical reference files

- `Slides/LectureS2_BinaryChoice_Nonparametric.tex` — preamble pattern, vspace conventions
- `Slides/LectureS1_BinaryChoice_Parametric.tex` — citation conventions, environment usage
- `Preambles/header.tex` — custom environments
- `Bibliography_base.bib` — needs ~12 new entries
