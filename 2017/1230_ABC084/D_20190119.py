Q = int(input())
LR = [tuple(map(int,input().split())) for _ in range(Q)]

N = 100010
# まずは素数列挙
P = []
A = [True]*N
for i in range(2,N):
    if A[i]:
        P.append(i)
        j = 2
        while i*j < N:
            A[i*j] = False
            j += 1

# 整数iまでの「2017数」を数える
Ans = [0]*N
for p in P:
    if p==2:
        continue
    if (p+1)//2 in P:
        Ans[p] = 1

for i in range(1,N):
    Ans[i] += Ans[i-1]

for (l,r) in LR:
    print(Ans[r] - Ans[l-1])