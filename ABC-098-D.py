N = int(input())
A = list(map(int,input().split()))

Ans,xorA,Li,Ri = 0,0,0,0
# 右端がN未満なら順次伸ばす
while Ri < N:
    # 条件を満たすなら答えを更新
    if xorA ^ A[Ri] == xorA + A[Ri]:
        Ans += Ri-Li+1
        xorA ^= A[Ri]
    # 条件を満たさないなら左端を調整
    else:
        # 条件を満たすまで左端を縮める
        while xorA ^ A[Ri] != xorA + A[Ri]:
            xorA ^= A[Li]
            Li += 1
        # 条件の調整(右端追加)と答えの更新
        xorA ^= A[Ri]
        Ans += Ri-Li+1
    Ri += 1
print(Ans)