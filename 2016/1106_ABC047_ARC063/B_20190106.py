W,H,N = map(int,input().split())
X,Y,A = [],[],[]
for i in range(N):
    x,y,a = map(int,input().split())
    X.append(x)
    Y.append(y)
    A.append(a)
x0,x1,y0,y1 = 0,W,0,H
for i in range(N):
    if A[i]==1:
        x0 = max(x0,X[i])
    elif A[i]==2:
        x1 = min(x1,X[i])
    elif A[i]==3:
        y0 = max(y0,Y[i])
    else:
        y1 = min(y1,Y[i])

print(max(0,(x1-x0))*max(0,(y1-y0)))