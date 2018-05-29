N = int(input())
A = list(map(int,input().split()))

Ans,setA,Li,Ri = 0,set([]),0,0
# 右端がN未満なら順次伸ばす
while Ri < N:
    # 条件を満たすなら答えを更新
    if A[Ri] not in setA:
        setA.add(A[Ri])
        Ans = max(Ans,Ri-Li+1)
    # 条件を満たさないなら左端を調整
    else:
        # 条件を満たすまで左端を縮める
        while A[Ri] in setA:
            setA.remove(A[Li])
            Li += 1
        setA.add(A[Ri])
    Ri += 1
print(Ans)