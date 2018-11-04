N = int(input())
K = int(input())
X = list(map(int,input().split()))
Ans = 0
for i in range(N):
    Ans += min(X[i]*2,(K-X[i])*2)
print(Ans)
