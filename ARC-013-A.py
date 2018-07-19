N,M,L = map(int,input().split())
P,Q,R = map(int,input().split())

from itertools import permutations
A = list(permutations([P,Q,R]))

Ans = 0
for a in A:
    n,m,l = a
    Ans = max(Ans, (N//n) * (M//m) * (L//l))

print(Ans)
