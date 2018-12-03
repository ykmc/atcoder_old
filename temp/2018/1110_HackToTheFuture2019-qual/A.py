import random
import time
import copy

# タイマー開始
start_time = time.time()

# 入力
N,M,L = map(int,input().split())
S = list(input() for _ in range(N))

# ボード生成
B = [["." for _ in range(M)] for _ in range(M)]
for i in range(M):
    B[0][i] = "#"
    B[M-1][i] = "#"
for i in range(1,M-1):
    B[i][0] = "#"
    B[i][M-1] = "#"
B0 = copy.deepcopy(B)

# スコア
Score = [[0 for _ in range(M)] for _ in range(M)]
Score0 = copy.deepcopy(Score)


## マスの種類
# D : 2倍マス、命令を2回実行する
# T : 3倍マス、命令を3回実行する
# L : Lマス、右回転を左回転にする
# R : Rマス、左回転を右回転にする

# とりあえずランダムに
if False:
    A = "DDDDDDDDDDTTTTLLLLRRRR#####" + "."*100
    for i in range(1,M-1):
        for j in range(1,M-1):
            k = random.randint(0,100)
            B[i][j] = A[k]

# スタート地点が壁ではないように
if B[M//2][M//2] == "#":
    B[M//2][M//2] = "."


# スコア計算
if True:
    for i in range(N):
        # 現在位置を初期化
        x,y = M//2,M//2
        dir = 2
        # 右→-1 左→+1
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        # 命令を処理
        for s in S[i]:
            if s == "S":
                tx,ty = x+dx[dir],y+dy[dir]
                if B0[ty][tx] != "#":
                    x,y = tx,ty
            elif s == "R":
                dir = (dir-1)%4
            else:
                dir = (dir+1)%4
        # スコア計算用に格納
        Score0[y][x] += 1

    score_base = 0
    for i in range(1,M-1):
        for j in range(1,M-1):
            if Score0[i][j] == 1:
                score_base += 10
            elif Score0[i][j] == 2:
                score_base += 3
            elif Score0[i][j] == 3:
                score_base += 1



# 出力
for i in range(M):
    print("".join(B[i]))