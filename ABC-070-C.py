# from fractions import gcd (v3.5 or later)
from fractions import gcd # v3.4

N = int(input())
T = []

for i in range(N):
    T.append(int(input()))

Ans = T[0]
for i in range(1,N):
    Ans = Ans*T[i]//gcd(Ans,T[i])

print(Ans)