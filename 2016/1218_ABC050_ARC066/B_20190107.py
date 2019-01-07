N  =int(input())
T  =list(map(int,input().split()))
M  =int(input())
P,X = [],[]
for i in range(M):
    p,x = map(int,input().split())
    P.append(p)
    X.append(x)

total = sum(T)
for i in range(M):
    print(total -  T[P[i]-1] + X[i])