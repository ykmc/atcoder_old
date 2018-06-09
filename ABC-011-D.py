import math
N,D = map(int,input().split())
X,Y = map(int,input().split())

def nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

Ans = 0
# ジャンプ幅で割り切れる場合のみ考える
if X%D == 0 and Y%D == 0:
    # 圧縮
    X,Y = abs(X//D),abs(Y//D)
    D = 1
    # x軸方向にdx回、y軸方向にdy回移動する。を全探索
    for dx in range(N+1):
        dy = N - dx
        # 各軸ごとに到達可能か判定
        if X > dx or Y > dy:
            continue
        # 各軸ごとに到達に必要な回数移動後の残移動回数が偶数か判定
        # (偶数でなければ不可能)
        if (dx-X)%2 == 1 or (dy-Y)%2 ==1:
            continue
        ## まともに計算すると死ぬので、分母は均等割で計算させる(これでも間に合わないならどうすれば？)
        # x軸方向
        #pX = nCr(dx, (dx-X)//2) / (4**dx)
        pX = nCr(dx, (dx-X)//2) / (2**N)
        # y軸方向
        #pY = nCr(dy, (dy-Y)//2) / (4**dy)
        pY = nCr(dy, (dy-Y)//2) / (2**N)
        # x軸y軸
        Ans += pX * pY * nCr(N,dx)

print(Ans)
