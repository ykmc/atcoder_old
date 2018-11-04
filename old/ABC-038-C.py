N = int(input())
A = list(map(int,input().split()))

Ans,prev,Li,Ri = 0,1,0,0
# 右端がN未満なら順次伸ばす
while Ri < N:
    # 条件を満たすなら答えを更新
    if A[Ri] > prev:
        Ans += Ri-Li+1
    # 条件を満たさないなら左端を調整
    else:
        # 条件を満たすまで左端を縮める
        Li = Ri
        Ans += 1
    prev = A[Ri]
    Ri += 1
print(Ans)