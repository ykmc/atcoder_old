N = int(input())
A = list(map(int,input().split()))

Ans = 0
ri,tmp = 0,0
for li in range(N):
    while ri < N and tmp&A[ri] == 0:
        tmp |= A[ri]
        ri += 1
    Ans += ri-li
    tmp ^= A[li]

print(Ans)