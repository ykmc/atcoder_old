N,M = map(int,input().split())
A = list(map(int,input().split()))

A.sort(reverse=True)

# 各数字に必要なマッチの本数
num  = [0,2,5,5,4,5,6,3,7,6]
# dp : i本のマッチで実現できる最大の桁数
dp = [-1*float("inf")]*(N+1)
# dp初期化 (0本では0桁, 各数字を1つ作る場合は1桁)
dp[0] = 0
for a in A:
    if num[a] <= N:
        dp[num[a]] = 1

for i in range(1,N+1):
    for a in A:
        if i - num[a] >= 0:
            dp[i] = max(dp[i], dp[i-num[a]] + 1)

ans = ""
for i in range(dp[N]):
    for a in A:
        if N-num[a] >= 0 and  dp[N-num[a]] == dp[N]-1:
            ans += str(a)
            N -= num[a]
            break

print(ans)