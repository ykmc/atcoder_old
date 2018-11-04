N = int(input())
A = list(map(int,input().split()))
dp = [0]*N
dp[0],dp[1] = 0,abs(A[1]-A[0])
for i in range(2,N):
    dp[i] = min(dp[i-1]+abs(A[i-1]-A[i]),dp[i-2]+abs(A[i-2]-A[i]))
print(dp[N-1])