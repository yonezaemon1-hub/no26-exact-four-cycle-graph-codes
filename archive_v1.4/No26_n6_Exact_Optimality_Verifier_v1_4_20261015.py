#!/usr/bin/env python3
"""Pure Python, integer-only independent certificate for D_{C4}(6)=6144.
No MILP, numpy, external packages, or unverified numerical optimization needed.
Usage: python No26_n6_Exact_Optimality_Verifier_20261015.py [witness.json]
"""
import hashlib
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

N=6
E=list(itertools.combinations(range(N),2))
EI={x:i for i,x in enumerate(E)}

def forbidden_masks():
    values=set()
    for vs in itertools.combinations(range(N),4):
        ev=list(itertools.combinations(vs,2))
        for missing in [((vs[0],vs[1]),(vs[2],vs[3])),
                        ((vs[0],vs[2]),(vs[1],vs[3])),
                        ((vs[0],vs[3]),(vs[1],vs[2]))]:
            values.add(sum(1 << EI[e] for e in ev if e not in missing))
    return sorted(values)

F=forbidden_masks()
assert len(F)==45
pivots={}
for v in F:
    x=v
    while x:
        t=x.bit_length()-1
        if t in pivots:
            x ^= pivots[t]
        else:
            pivots[t]=x
            break
B=list(pivots.values())
assert B==[102,170,306,549,1065,2097,4169,8273,16529]
S=[0]
for b in B:
    S += [x^b for x in S]
assert len(S)==len(set(S))==512
coords={v:i for i,v in enumerate(S)}
assert set(F)<=set(S)

permutation_maps=[]
for p in itertools.permutations(range(N)):
    permutation_maps.append(tuple(EI[tuple(sorted((p[u],p[v])))] for u,v in E))

def permute_mask(x, m):
    y=0
    while x:
        bit=x&-x
        y |= 1 << m[bit.bit_length()-1]
        x-=bit
    return y

missing=set(S)
orbits=[]
while missing:
    x=min(missing)
    orb=sorted({permute_mask(x,m) for m in permutation_maps})
    assert set(orb)<=missing  # orbit closure
    missing.difference_update(orb)
    orbits.append(orb)
orbits.sort(key=lambda orb:(len(orb),orb[0]))
assert [len(orb) for orb in orbits]==[1,6,10,15,15,45,60,90,90,180]
assert orbits[0]==[0] and set(orbits[5])==set(F)

# Seven nontrivial characters of the elementary abelian group S, with
# nonnegative integer coefficients.  These exact values were found by
# solving a linear program; their correctness is independently checked here.
DUAL={1:24,3:12,4:9,5:21,6:5,17:18,37:6}
assert sum(DUAL.values())==95

def character(k,v):
    return 1 if ((k&coords[v]).bit_count()&1)==0 else -1

weighted=[]
for orb in orbits:
    weighted.append(sum(w*sum(character(k,v) for v in orb)
                        for k,w in DUAL.items()))
assert weighted==[95,-6,-74,-15,-15,435,-60,-90,-90,-180],weighted
assert all(weighted[i]<=-len(orb) for i,orb in enumerate(orbits) if i not in (0,5))

# Proof:
# For an independent I in S define h(d) = #{(a,b)in I^2:a^b=d}/|I|.
# h(0)=1, h|F=0. The Fourier transform of h at each k is
# |sum_{a in I} character(k,a)|^2/|I| >= 0.
# Average h over 720 permutations of the six graph vertices.  The averaged
# function is constant t_j on each orbit, without changing |I|.
# Multiply seven Fourier inequalities by the weights DUAL[k] and add:
# 95 -6 t_1 -74 t_2 -15 t_3 -15 t_4 -60 t_6 -90 t_7
# -90 t_8 -180 t_9 >=0.  Since t_j >=0 and all coefficients on the
# left are <= -orbit_size_j, |I| = 1 + sum_j orbit_size_j*t_j <=96.
component_upper=96

path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent / 'no26_n6_improved_witness_6144.json'
raw=path.read_bytes()
w=json.loads(raw)
seed=w['seed96']
reps=w['coset_representatives']
assert len(seed)==96 and len(set(seed))==96
assert set(seed)<=set(S)
assert len(reps)==64 and len(set(reps))==64
# Every forbidden difference lies in S; distinct cosets cannot conflict.
allwords={r^s for r in reps for s in S}
assert len(allwords)==32768
code={r^a for r in reps for a in seed}
assert len(code)==64*96==6144
C=set(code)
for a in C:
    for f in F:
        assert (a^f) not in C

# Also independently check every unordered pair (not merely neighbor lookups).
ordered=sorted(C)
fset=set(F)
pair_count=0
for i,a in enumerate(ordered):
    for b in ordered[i+1:]:
        assert (a^b) not in fset
        pair_count+=1
assert pair_count==18871296
assert component_upper*len(reps)==len(code)
result={
    'claim':'D_C4(6) = 6144 (exact)',
    'status':'PASS',
    'forbidden_masks':len(F),
    'span_rank':len(B),
    'span_size':len(S),
    'coset_count':len(reps),
    'orbit_sizes':[len(o) for o in orbits],
    'orbit_representatives':[o[0] for o in orbits],
    'dual_character_weights':{str(k):v for k,v in DUAL.items()},
    'integer_weighted_character_sums':weighted,
    'component_upper_exact':component_upper,
    'seed_size':len(seed),
    'expanded_code_size':len(C),
    'unordered_pairs_verified':pair_count,
    'conflicts':0,
    'witness_sha256':hashlib.sha256(raw).hexdigest()
}
print(json.dumps(result,indent=2,ensure_ascii=False))
