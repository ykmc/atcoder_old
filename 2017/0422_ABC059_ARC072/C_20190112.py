N = int(input())
A = list(map(int,input().split()))

ans1,ans2 = 0,0
res = 0
for i in range(N):
    res += A[i]
    if i%2==1:
        if res >= 0:
            ans1 += res+1
            res = -1
    else:
        if res <= 0:
            ans1 -= res-1
            res = 1

res = 0
for i in range(N):
    res += A[i]
    if i%2==1:
        if res <= 0:
            ans2 -= res-1
            res = 1
    else:
        if res >= 0:
            ans2 += res+1
            res = -1

print(min(ans1,ans2))
