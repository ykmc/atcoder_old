from math import ceil
from decimal import Decimal

N = int(input())
T,A = [],[]
for i in range(N):
    t,a = map(int,input().split())
    T.append(t)
    A.append(a)

t,a = 1,1
for i in range(N):
    r = Decimal(max(ceil(t/T[i]),ceil(a/A[i])))
    t = r*T[i]
    a = r*A[i]

print(t+a)