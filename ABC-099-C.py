N = int(input())

dp = [0]*(N+100001)
for i in range(99999):
    dp[i] = 10**10

for i in range(100000,N+100001):
    dp[i] = min(dp[i-1] + 1,
                dp[i-6] + 1,
                dp[i-9] + 1,
                dp[i-36] +1,
                dp[i-81] + 1,
                dp[i-216] + 1,
                dp[i-729] + 1,
                dp[i-1296] + 1,
                dp[i-6561] + 1,
                dp[i-7776] + 1,
                dp[i-46656] + 1,
                dp[i-59049] + 1)

print(dp[N+99999])