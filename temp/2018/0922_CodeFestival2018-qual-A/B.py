N,M,A,B = map(int,input().split())
L,R = [],[]
for i in range(M):
    l,r = map(int,input().split())
    L.append(l-1)
    R.append(r-1)

X = [B]*N
for i in range(M):
    for j in range(L[i],R[i]+1):
        X[j] = A

print(sum(X))