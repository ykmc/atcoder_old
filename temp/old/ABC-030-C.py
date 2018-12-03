from bisect import bisect_left
N = list(map(int,input().split())) # N[0],N[1] = N,M
D = list(map(int,input().split())) # D[0],D[1] = X,Y
T = [[]]*2
T[0] = list(map(int,input().split())) #A
T[1] = list(map(int,input().split())) #B

# 空港の初期値
ap = 0 
# 現在時刻
now = 0
# 往復カウント
Ans = 0

# 最終便に乗れなくなるまでループ
while now <= T[ap][N[ap]-1]:
    i = bisect_left(T[ap], now)
    now = T[ap][i] + D[ap]
    # 空港を反転
    ap ^= 1
    # 到着空港が A なら往復カウント
    if ap == 0:
        Ans += 1

print(Ans)