N = int(input())
RP,BP = [],[]
for i in range(N):
    a,b = map(int,input().split())
    RP.append((a,b))
for i in range(N):
    c,d = map(int,input().split())
    BP.append((c,d))

Ans = 0
# 青い点をx座標で昇順ソートし、順番にみる
BP.sort()
for bp in BP:
    bx,by = bp
    # 赤い点を全探索、条件を満たすペアをリストアップする
    R_yxi = []
    for i in range(len(RP)):
        rx,ry = RP[i]
        if rx < bx and ry < by:
            R_yxi.append((ry,rx,i))
    # 条件を満たすペアが存在する場合、その中でy座標が最大のものとペアにする
    if len(R_yxi) > 0:
        R_yxi.sort(reverse=True)
        rx,ry,i = R_yxi.pop(0)
        RP.pop(i)
        Ans += 1

print(Ans)