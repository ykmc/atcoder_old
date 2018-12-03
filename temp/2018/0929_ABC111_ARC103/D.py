N = int(input())
X,Y = [],[]
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

# パリティが同一かチェック
p = set()
for i in range(N):
    p.add((X[i]+Y[i])%2)

# もし0,1の2種類あるなら不可能
if len(p)>1:
    print(-1)
    exit()

# パリティが0の場合 → X座標を-1して 1の場合に帰着する(あとでX+1する)
if 0 in p:
    for i in range(N):
        X[i] -= 1

# アームを準備
D = []
for i in range(35):
    D.append(2**i)
D.sort(reverse=True)

Ans = []
# 順番に計算
for i in range(N):
    x,y = X[i],Y[i]
    x0,y0 = 0,0
    ans = ""
    for d in D:
        tx,ty = x-x0,y-y0
        if ty<tx and ty>-tx:
            ans += "R"
            x0 += d
        elif ty<tx and ty<-tx:
            ans += "D"
            y0 -= d
        elif ty>tx and ty<-tx:
            ans += "L"
            x0 -= d
        else:
            ans += "U"
            y0 += d
    Ans.append(ans)

# パリティが0の場合 → 1のアームを追加、最後にRで調整
if 0 in p:
    D.append(1)
    print(len(D))
    print(" ".join(map(str,D)))
    for ans in Ans:
        print(ans + "R")
else:
    print(len(D))
    print(" ".join(map(str,D)))
    for ans in Ans:
        print(ans)



