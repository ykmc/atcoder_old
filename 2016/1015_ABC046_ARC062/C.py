from decimal import * 
from math import ceil
N = int(input())
T,A = 1,1
for i in range(N):
    Ti,Ai = map(int,input().split())
    r = Decimal(max(ceil(T/Ti),ceil(A/Ai)))
    T,A = Ti*r,Ai*r
print(T+A)
