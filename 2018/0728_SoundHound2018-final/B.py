N,K = map(int,input().split())
B = []
for i in range(N):
    B.append(int(input()))

# i番目までの答え
dp1 = [0]*(N+1)
# i-K番目までの答えのうちの最大値
dp2 = [0]*(N+1)

for i in range(N):
    # i+1番目を使う : i番目までの答えにi+1番目を加える
    # i+1番目を使わない : i+1-K番目までの最大値
    if i+1 >= K:
        dp1[i+1] = max(dp1[i] + B[i], dp2[i+1-K])
    # K個未満のため、使うしかない
    else:
        dp1[i+1] = dp1[i] + B[i]
    # i+1番目を使わない場合の計算用に
    dp2[i+1] = max(dp2[i], dp1[i+1])

print(dp1[N])