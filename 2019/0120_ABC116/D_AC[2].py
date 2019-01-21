N,K = map(int,input().split())
X = []
for i in range(N):
    t,d = map(int,input().split())
    X.append((d,t))

X.sort(reverse=True)

p,v = 0,set([])
pp = []
for i in range(K):
    p += X[i][0]
    if X[i][1] not in v:
        v.add(X[i][1])
    else:
        pp.append((X[i][0],X[i][1]))

Ans = p + len(v)**2
ans = Ans
for i in range(K,N):
    if X[i][1] not in v and len(pp)>0:
        temp = pp[-1]
        pp = pp[:len(pp)-1]
        ans = ans - temp[0] + X[i][0] - len(v)**2 + (len(v)+1)**2
        v.add(X[i][1])
        Ans = max(Ans,ans)

print(Ans)
