# python3:TLE, PyPy3:AC
N,A = map(int,input().split())
X = [0]+list(map(int,input().split()))

dp = [[[0 for _ in range(2500+1)] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(1,N+1):
    for j in range(0,i+1):
        for k in range(2500+1):
            if j==0 and k==0:
                dp[i][j][k] = 1
            elif k < X[i]:
                dp[i][j][k] = dp[i-1][j][k]
            elif j > 0 and k >= X[i]:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k-X[i]]

if max(X) < A:
    print(0)
else:
    Ans = 0
    for i in range(1,N+1):
        Ans += dp[N][i][A*i]
    print(Ans)