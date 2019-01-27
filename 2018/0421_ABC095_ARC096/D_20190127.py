N,C = map(int,input().split())
XV = [tuple(map(int,input().split())) for _ in range(N)]


# 順方向,逆方向の累積和
VF,VB = [0]*(N+1),[0]*(N+1)
for i in range(N):
    VF[i+1] += VF[i]+XV[i][1]
for i in range(N):
    VB[N-i-1] += VB[N-i]+XV[N-1-i][1]
# 移動距離を減算
for i in range(N):
    VF[i+1] -= XV[i][0]
for i in range(N):
    VB[N-i-1] -= (C-XV[N-1-i][0])
# 食べに行くと損する場合を除くために単調増加に
for i in range(N):
    if VF[i+1] < VF[i]:
        VF[i+1] = VF[i]
for i in range(N):
    if VB[N-1-i] < VB[N-i]:
        VB[N-1-i] = VB[N-i]

# 順方向,逆方向で全部食べた場合で初期化
ans = 0
ans = max(ans, VF[N], VB[0])

# 反転 : 順方向→逆方向
for i in range(1,N):
    ans = max(ans, VF[i], VF[i]+VB[i]-XV[i-1][0])

# 反転 : 逆方向→順方向
for i in range(1,N):
    ans = max(ans, VB[i], VB[i]+VF[i]-(C-XV[i][0]))

print(ans)