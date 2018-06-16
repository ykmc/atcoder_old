N,M = map(int,input().split())
X,Y,Z = [],[],[]
for i in range(N):
    x,y,z = map(int,input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

Sign = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
Ans = []

for sign in Sign:
    T = []
    for i in range(N):
        T.append(X[i]*sign[0] + Y[i]*sign[1] + Z[i]*sign[2])
    T.sort(reverse=True)
    ans = 0
    for i in range(M):
        ans += T[i]
    Ans.append(ans)

print(max(Ans))


