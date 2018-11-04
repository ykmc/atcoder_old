import math
N,H = map(int,input().split())
A,B,C,D,E = map(int,input().split())

Ans = A*N

for i1 in range(N+1):
    i2 = max(0, -(H +i1*B -(N-i1)*E)//(D+E) +1)
    if i1+i2<=N:
        Ans = min(Ans, A*i1+C*i2)

print(Ans)