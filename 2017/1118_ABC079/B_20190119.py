N = int(input())

dp = [0]*87
dp[0],dp[1] = 2,1

for i in range(2,87):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N])