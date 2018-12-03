N,C = map(int,input().split())
X,V = [],[]
for i in range(N):
    x,v = map(int,input().split())
    X.append(x)
    V.append(v)
Ans = 0

# 右回り、左周りの原点基準の移動距離
xR = [0]+X
xL = [0]+list(map(lambda x: C-x,reversed(X)))

# 右回り,左周りで食べた時の累積カロリー
V2 = list(reversed(V))
calR,calL = [0],[0]
for i in range(N):
    calR.append(calR[i]+V[i])
    calL.append(calL[i]+V2[i])

# 移動距離を考慮した獲得カロリー
getR,getL = [],[]
for i in range(N+1):
    getR.append(calR[i]-xR[i])
    getL.append(calL[i]-xL[i])
# 単調増加になるように修正
for i in range(N):
    if getR[i+1] < getR[i]:
        getR[i+1] = getR[i]
    if getL[i+1] < getL[i]:
        getL[i+1] = getL[i]

for i in range(N+1):
    gr = getR[N-i]
    gl = getL[i]
    xr = xR[N-i]
    xl = xL[i]
    # 右回り → 左周り
    Ans = max(Ans, gr, gr-xr+gl)
    # 左周り → 右回り
    Ans = max(Ans, gl, gl-xl+gr)

print(Ans)
