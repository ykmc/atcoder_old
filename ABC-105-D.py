from collections import Counter
N,M = map(int,input().split())
A = list(map(int,input().split()))

S = [0]*(N+1)
for i in range(N):
    S[i+1] = (S[i]+A[i]) % M

C = Counter(S)

Ans = 0
for v in C.values():
    if v != 1:
        Ans += v*(v-1)//2

print(Ans)