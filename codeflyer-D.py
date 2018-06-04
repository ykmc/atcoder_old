H,W = map(int,input().split())
N,M = map(int,input().split())
A = []
for _ in range(N):
    A.append(input())

# 座標圧縮
cH = min(H, N*2+1)
cW = min(W, M*2+1)
X = [[0 for _ in range(cW)] for _ in range(cH)]

# ハンコの移動距離
dh = cH - N
dw = cW - M

# いもす法 : 準備
for i in range(N):
    for j in range(M):
        if A[i][j] == "#":
            X[i][j] += 1
            if i+dh+1 < cH:
                X[i+dh+1][j] += -1
            if j+dw+1 < cW:
                X[i][j+dw+1] += -1
            if i+dh+1 < cH and j+dw+1 < cW:
                X[i+dh+1][j+dw+1] += 1

# いもす法 : 横に累積
for i in range(cH):
    tmp = 0
    for j in range(cW):
        tmp += X[i][j]
        X[i][j] = tmp
# いもす法 : 縦に累積
for j in range(cW):
    tmp = 0
    for i in range(cH):
        tmp += X[i][j]
        X[i][j] = tmp

# いもす法 : 集計
Ans = 0
for i in range(cH):
    for j in range(cW):
        if X[i][j] > 0:
            # 座標圧縮の展開
            if cH == N*2+1 and i==N and cW == M*2+1 and j==M:
                Ans += (H-2*N)*(W-2*M)
            elif cH == N*2+1 and i==N:
                Ans += H-2*N
            elif cW == M*2+1 and j==M:
                Ans += W-2*M
            else:
                Ans += 1

print(Ans)

# 課題
# - いもす法を使う時、はみ出る部分は多次元リストに組み込まない方が良いか？
#    - 今回は組み込まずにやった、集計時に混乱しそうだったので
# - 準備の(1,-1,-1,1)を設定するところ、もっと簡単に書けないか？
#    - これでも動くけど。。。
# - 座標圧縮の展開はもっと簡単に書けないか？
#    - これでも動くけど。。。