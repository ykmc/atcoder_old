from collections import Counter

N = int(input())
A = list(map(int,input().split()))

S = [0]*N
S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1]+A[i]

S.append(0)

C = Counter(S).most_common()

Ans = 0
for k,v in C:
    if v >= 2:
        Ans += v*(v-1)//2

print(Ans)
