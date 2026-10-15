# No.26 v1.4 — graph codes, exact n=6, publication and reproducibility gate

Date: 15 October 2026  
Status: **Independent computational cross-check PASS / not professionally peer reviewed / historical novelty INCONCLUSIVE / not published**.

## Mathematical results

- All-n linear optimum: `D_C4^linear(n) = 2^(binom(n,2) - ceil(log2(n)))` for `n >= 4` (proof in paper).
- Exact n=5 unrestricted optimum: `D_C4(5)=192`, linear optimum `128`.
- Exact n=6 unrestricted optimum: `D_C4(6)=6144`, linear optimum `4096`.
- The n=6 upper bound is an explicit positive-definite Fourier kernel on the 512-point subspace; the n=6 lower bound is a 96-word seed replicated over 64 cosets.
- A separate independent implementation recomputed the n=6 Fourier spectrum and kernel conditions, in agreement with the proof table; this is **not** professional peer review.

## Reproducibility correction (v1.4)

- `No26_n6_Exact_Optimality_Verifier_v1_4_20261015.py` now finds `no26_n6_improved_witness_6144.json` **relative to the script directory**, rather than using a fixed `/mnt/data` path.
- Optional positional argument `[witness.json]` still overrides the default file path.
- The unmodified spectral verifier uses Python standard library only.
- The strict package-extraction test executes both verifiers with the current working directory **outside** the extracted folder; both PASS.
- Direct verification checks 18,871,296 unordered codeword pairs and reports zero forbidden `C4` differences.

## Author inquiry wording and status edits

- The paper says that, to the best of the author's knowledge, the specified finite results and all-n linear formula were not found in the literature **examined**; it does not claim priority.
- Readers knowing earlier/overlapping results may contact **yonezaemon1+research@gmail.com** (Yonezu Research Lab).
- Title/date line and reproducibility paragraph no longer say the new n=6 proof is awaiting independent recomputation; they now accurately state a separate computational cross-check was completed. **Not peer-reviewed** remains explicit.
- Mathematical claims, proofs, coefficients, spectrum counts, and witness contents are unchanged from v1.3.

## Remaining open matters

- Scholarly novelty and historical priority: **INCONCLUSIVE** (no first-discovery claim).
- Expert review is **not required** by the author's publication policy.
- GitHub and Zenodo: **NOT PUBLISHED**.

## Version control

- v1.1, v1.2 and v1.3 remain unmodified. This v1.4 is a new version, with changed code path resolution and audit wording.
- Manifest `No26_n6_Exact_v1_4_SHA256_20261015.txt` hashes all other nine ZIP entries; SHA256 of the manifest itself and the complete ZIP are external to the manifest to avoid recursion.
