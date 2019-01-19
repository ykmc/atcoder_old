S = input()
X,Y = map(int,input().split())

S = S+"T"
d,cnt = 0,0
pos = [set([0]),set([0])]
init = False
for s in S:
    # 前進
    if s=="F":
        cnt += 1
    # 方向転換
    else:
        # 移動先を全列挙
        if cnt>0:
            temp = set([])
            for p in pos[d]:
                temp.add(p+cnt)
                if init:
                    temp.add(p-cnt)
            pos[d] = temp
        # 方向転換
        d = (d+1)%2
        cnt = 0
        # 初回の方向転換を終えたかどうか
        init = True

print("Yes" if X in pos[0] and Y in pos[1] else "No")