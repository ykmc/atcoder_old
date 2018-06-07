N,D,K = map(int,input().split())
L,R,S,T = [],[],[],[]
for i in range(D):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)
for i in range(K):
    s,t = map(int,input().split())
    S.append(s)
    T.append(t)

for i in range(K):
    start = S[i]
    goal = T[i]
    now = start
    # goalが右側
    if start < goal:
        for d in range(D):
            if L[d] <= now <= R[d]:
                now = R[d]
            if goal <= now:
                break
    # goalが左側
    else:
        for d in range(D):
            if L[d] <= now <= R[d]:
                now = L[d]
            if now <= goal:
                break
    # 日数を出力
    print(d+1)

