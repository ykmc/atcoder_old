N = int(input())
A = list(map(int,input().split()))

Ans = 10**10
for i in range(-100,101):
    ans = 0
    for j in range(N):
        ans += (A[j]-i)**2
    Ans = min(Ans,ans)

print(Ans)