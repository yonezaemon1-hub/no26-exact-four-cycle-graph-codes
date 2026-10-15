# No.26: Exact value at six vertices — independent proof candidate

Date: 2026-10-15. Status: **internal mathematical verification PASS; external AI audit not yet performed on the new upper-bound proof; publication pending**.

## Result

For the graph-code problem forbidding pairs of labelled graphs whose symmetric difference is **exactly** the four edges of a four-cycle,

\[
\boxed{D_{C_4}(6)=6144=64\cdot96.}
\]

The lower bound 6144 is achieved by the attached 96-word seed, translated to all 64 cosets, as independently checked for every one of 18,871,296 unordered word pairs. This note proves the matching **upper bound** with a finite positive-definite Fourier certificate.

## Reduction to 512 vertices

Identify an edge set of K_6 with a binary vector in V=F_2^{15}. Let F be the 45 vectors of the three distinct 4-cycles on each of the 15 four-vertex subsets. Their span S has dimension 9 (computed by exact GF(2) elimination); therefore V has 64 cosets of S, all mutually disconnected with respect to forbidden differences. Every coset is isomorphic to the Cayley conflict graph on S with generating set F. Consequently

\[
D_{C_4}(6)=64\,\alpha(\operatorname{Cay}(S,F)).
\]

The recorded seed96 witnesses alpha >=96, so only alpha <=96 is needed.

## Positive-definite kernel certificate

Let T be the 10 edge sets of **two vertex-disjoint triangles** partitioning the six vertices. Each member of T is in S, and T is disjoint from F.

Define K:S->Q by

\[
K(x)=96\mathbf1_{x=0}-1+\frac{32}{3}\mathbf1_{x\in F}-\frac{32}{5}\mathbf1_{x\in T}.
\]

Thus K(0)=95; for every nonzero allowed difference x outside F, K(x)=-1 except for the 10 members of T, where K(x)=-37/5. Therefore K(x)<=-1 for all admissible nonzero differences.

Write the character group of S as \hat S. For chi in \hat S let

\[
a(\chi)=\sum_{f\in F}\chi(f),\qquad b(\chi)=\sum_{t\in T}\chi(t).
\]

For the trivial character, \hat K(1)=96-512+(32/3)45-(32/5)10=0. For a nontrivial character, using sum_{x in S}chi(x)=0,

\[
\hat K(\chi)=96+\frac{32}{3}a(\chi)-\frac{32}{5}b(\chi)
=\frac{32}{15}\left(45+5a(\chi)-3b(\chi)\right).
\]

The following joint character spectrum is **exact**; multiplicities sum to 512. The final column is nonnegative in every row; on the trivial character it is not the applicable Fourier eigenvalue, which is 0 as separately calculated.

| a = sum_F chi | b = sum_T chi | Number of characters | 45+5a-3b |
|---:|---:|---:|---:|
| -15 | -10 | 6 | 0 |
| -7 | -2 | 90 | 16 |
| -3 | 2 | 180 | 24 |
| -3 | 10 | 15 | 0 |
| 1 | -2 | 90 | 56 |
| 5 | 2 | 45 | 64 |
| 9 | -10 | 10 | 120 |
| 9 | -2 | 60 | 96 |
| 21 | 2 | 15 | 144 |
| 45 | 10 | 1 (trivial) | 240 |

Thus all Fourier coefficients of K are nonnegative. Fourier inversion yields, for every A subset S,

\[
\sum_{u,v\in A}K(u+v)
=\frac{1}{512}\sum_{\chi\in\hat S}\hat K(\chi)\left|\sum_{u\in A}\chi(u)\right|^2\ge0.
\]

For an F-admissible A of size M, the diagonal contributes 95M and each off-diagonal term is <=-1. Hence

\[
0\le\sum_{u,v\in A}K(u+v)\le95M-M(M-1)=M(96-M).
\]

If M>0 this forces M<=96. The seed attains 96, and the 64 cosets give exactly 6144 globally. **QED (subject to external rechecking of the new spectrum and proof).**

## Independent validation

1. `No26_n6_Exact_Optimality_Verifier_20261015.py`: constructs S; partitions all 512 elements into 10 graph-automorphism orbits; validates an independent 7-character nonnegative dual certificate by integer arithmetic; tests seed96 and every unordered pair in the 6144-word expanded code.
2. `No26_n6_Independent_Spectral_Check_20261015.py`: independently builds F and T in the **15-dimensional ambient edge space**; evaluates all 32768 ambient parity characters; checks that the table multiplicities are 64 times those of restrictions to S; verifies each integer spectral factor is nonnegative. No SciPy or floating-point optimization is used in either verification.

## Scope and limitations

- The claimed exact value is finite **n=6 only**, under the **exact-copy C4** forbidden-difference definition. Do not conflate it with forbidding every difference that *contains* a C4.
- This closes the previous internal mathematical question whether the 6144 lower bound could be optimal. It does not establish publication priority or novelty.
- The previous component upper estimate 116 is superseded by the verifiable upper bound 96.
- No specialist review is requested. The new proof has not yet undergone Claude's separate independent audit.
