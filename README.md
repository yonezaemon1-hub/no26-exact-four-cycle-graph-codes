# No.26 — Finite Nonlinear Separations for Exact Four-Cycle Graph Codes

**Author:** Ryutaro Yonezu — Yonezu Research Lab  
**Release candidate:** 15 October 2026, manuscript v1.4  
**Status:** independent computational cross-check PASS; unrefereed preprint; historical priority/newness INCONCLUSIVE.

## Results

For labelled graphs on n vertices, pairs whose symmetric difference is **exactly** the edge set of one four-cycle are excluded (not all differences containing a C4):

- For every n >= 4, the largest linear code has size `2^(binom(n,2) - ceil(log2(n)))`.
- At n = 5, the exact unrestricted optimum is **192**, compared with the linear optimum **128**.
- At n = 6, the exact unrestricted optimum is **6144**, compared with the linear optimum **4096**. A finite Fourier-positive kernel proves the upper bound, and an explicit 96-word witness translated over 64 cosets attains it.

## Contents

- `archive_v1.4/No26_N_C4_short_note_REVISED_v1_4_20261015.pdf` — four-page paper.
- `archive_v1.4/No26_N_C4_short_note_REVISED_v1_4_20261015.tex` — TeX source.
- `archive_v1.4/No26_n6_Exact_Optimality_Verifier_v1_4_20261015.py` — witness/pairwise check and integer certificate.
- `archive_v1.4/No26_n6_Independent_Spectral_Check_20261015.py` — independent Fourier spectrum check.
- `archive_v1.4/no26_n6_improved_witness_6144.json` — 96-element seed and 64 coset representatives.
- `archive_v1.4/No26_n6_Exact_v1_4_SHA256_20261015.txt` — checksums of all nine other original files.
- `No26_n6_Exact_Proof_Bundle_v1_4_20261015.zip` — unchanged, audited v1.4 bundle.

The accompanying proof memo (`No26_n6_Exact_Optimality_Proof_20261015.md`) records a **pre-audit stage**, including an outdated line that external recomputation was pending. The authoritative v1.4 paper and publication gate describe the completed independent computational cross-check. The mathematical proof in that memo is unchanged. The distinction is noted here instead of silently modifying evidence or invalidating the v1.4 SHA-256 manifest.

## Reproducibility

Requires Python 3.12 standard library only. After extracting this package:

```bash
python archive_v1.4/No26_n6_Exact_Optimality_Verifier_v1_4_20261015.py
python archive_v1.4/No26_n6_Independent_Spectral_Check_20261015.py
```

The first script searches for the witness JSON beside itself; it can run from an unrelated working directory. It checks 18,871,296 unordered pairs and finds zero prohibited differences.

## Prior art and citation

To the best of the author's knowledge, these particular finite values and the all-n linear formula were not found in the literature examined. **This is not a priority or first-discovery claim.** Historical novelty remains open. Readers knowing earlier or overlapping work may write to **yonezaemon1+research@gmail.com**.

**Citation:** Ryutaro Yonezu, *Finite Nonlinear Separations for Exact Four-Cycle Graph Codes*, Yonezu Research Lab, unrefereed preprint v1.4 (2026). **DOI:** [10.5281/zenodo.23386988](https://doi.org/10.5281/zenodo.23386988).

**Rights:** © 2026 Ryutaro Yonezu. All rights reserved. No permission is granted for reproduction, redistribution, modification, or commercial reuse without prior written permission, except as permitted by applicable law. This repository grants no separate reuse license.
