N,M = map(int,input().split())
P = list(map(int,input().split()))
X,Y = [],[]
for i in range(M):
    x,y = map(int,input().split())
    X.append(x-1)
    Y.append(y-1)
T = [-1]*N
group = 0
for i in range(M):
    if T[X[i]] == -1 and T[Y[i]] == -1:
        T[X[i]] = group
        T[Y[i]] = group
        group += 1
    elif T[X[i]] != -1 and T[Y[i]] != -1:
        minG = min(T[X[i]],T[Y[i]])
        maxG = max(T[X[i]],T[Y[i]])
        for i in range(N):
            if T[i] == maxG:
                T[i] = minG
    else:
        if T[X[i]] == -1 and T[Y[i]] != -1:
            T[X[i]] = T[Y[i]]
        if T[Y[i]] == -1 and T[X[i]] != -1:
            T[Y[i]] = T[X[i]]
uniqueT = list(set(T))
uniqueT.sort()
ansT = [[] for _ in range(len(uniqueT))]
ansP = [[] for _ in range(len(uniqueT))]
for i in range(len(uniqueT)):
    if i != -1:
        for j in range(N):
            if T[j] == uniqueT[i]:
                ansT[i].append(j)
                ansP[i].append(P[j]-1)
Ans = 0
for i in range(len(uniqueT)):
    Ans += len(list(set(ansT[i]) & set(ansP[i])))
for i in range(N):
    if T[i] == -1 and P[i]-1 == i:
        Ans += 1
print(Ans)
