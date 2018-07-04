N = int(input())
X,Y = [],[]
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

Ans = 0
for i in range(N):
    for j in range(N):
        Ans = max(Ans,(X[i]-X[j])**2+(Y[i]-Y[j])**2)

print(Ans**0.5)