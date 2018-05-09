N = int(input())
T = list(map(int,input().split()))
M = int(input())
P,X = [],[]
for i in range(M):
    p,x = map(int,input().split())
    P.append(p-1)
    X.append(x)
sumT = sum(T)
for i in range(M):
    print(sumT + X[i] - T[P[i]])