#!/usr/bin/env python3
"""Independent, basis-free 15-bit Walsh spectrum proof for n=6 C4-code bound.
Enumerates all 2^15 linear characters of edge space; each restriction to
9-dimensional C4 span appears 64 times. Standard library only.
"""
from collections import Counter
from itertools import combinations
import json

N=6
edges=list(combinations(range(N),2))
index={e:i for i,e in enumerate(edges)}
def mask(edges):return sum(1<<index[e] for e in edges)
F=set()
for four in combinations(range(N),4):
 for pairs in [((four[0],four[1]),(four[2],four[3])),((four[0],four[2]),(four[1],four[3])),((four[0],four[3]),(four[1],four[2]))]:
  missing=set(pairs)
  F.add(mask(e for e in combinations(four,2) if e not in missing))
T=set()
for tri in combinations(range(N),3):
 if 0 not in tri:continue  # count each split once
 other=tuple(v for v in range(N) if v not in tri)
 T.add(mask(list(combinations(tri,2))+list(combinations(other,2))))
assert len(F)==45 and len(T)==10 and not F&T
# Independently check rank and inclusion T subset S with bit-elimination.
pivots={}
for f in sorted(F):
 x=f
 while x:
  b=x.bit_length()-1
  if b in pivots:x^=pivots[b]
  else:pivots[b]=x;break
assert len(pivots)==9
for t in T:
 x=t
 while x:
  b=x.bit_length()-1
  if b in pivots:x^=pivots[b]
  else:break
 assert x==0

frequencies=Counter()
for k in range(1<<15):
 f=sum(1 if (k&v).bit_count()%2==0 else -1 for v in F)
 t=sum(1 if (k&v).bit_count()%2==0 else -1 for v in T)
 frequencies[(f,t)]+=1
assert sum(frequencies.values())==32768
assert all(m%64==0 for m in frequencies.values())
classes=sorted((f,t,m//64,45+5*f-3*t) for (f,t),m in frequencies.items())
assert classes==[
  (-15,-10,6,0),(-7,-2,90,16),(-3,2,180,24),(-3,10,15,0),
  (1,-2,90,56),(5,2,45,64),(9,-10,10,120),
  (9,-2,60,96),(21,2,15,144),(45,10,1,240)
],classes
# K(0)=95, K(C4)=29/3, K(two triangles)=-37/5,
# K(other nonzero)=-1. For every restricted character != trivial,
# Fourier K = (32/15)*(45 + 5*lambda_F - 3*lambda_T) >=0.
# For trivial character: Khat=96-512+(32/3)*45-(32/5)*10=0.
assert all(weight>=0 for f,t,m,weight in classes)
assert sum(m for f,t,m,w in classes)==512
print(json.dumps({'status':'PASS','certificate':'exact positive type kernel','classes':[{'lambda_F':f,'lambda_T':t,'multiplicity':m,'weight_factor':w} for f,t,m,w in classes], 'rank':9,'component_independence_upper':96, 'global_upper':6144},indent=2))
