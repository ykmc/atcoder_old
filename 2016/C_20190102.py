N,A = map(int,input().split())
X = [0]+list(map(int,input().split()))

# dp[n][k][s] : n枚目までからk枚選んで合計をsにする場合の数
dp = [[[0 for _ in range(2501)] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for n in range(1,N+1):
    for k in range(n+1):
        for s in range(50*k+1):
            if s<X[n]:
                dp[n][k][s] = dp[n-1][k][s]
            elif k>=1 and s>=X[n]:
                dp[n][k][s] = dp[n-1][k][s] + dp[n-1][k-1][s-X[n]]

Ans = 0
for i in range(1,N+1):
    Ans += dp[N][i][i*A]

print(Ans)