N = int(input())
NG = []
for i in range(3):
    NG.append(int(input()))

inf = float("inf")
dp = [inf]*(N+4)
dp[N] = 0
for i in range(1,N+1):
    dp[N-i] = min(dp[N-i+1] +1 if N-i+1 not in NG else inf,\
                  dp[N-i+2] +1 if N-i+2 not in NG else inf,\
                  dp[N-i+3] +1 if N-i+3 not in NG else inf)
print("YES" if dp[0]<=100 else "NO")