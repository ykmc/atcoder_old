N,M = map(int,input().split())
X = list(map(int,input().split()))

if N >= M:
    print(0)
else:
    X.sort()
    D = []
    for i in range(M-1):
        D.append(X[i+1]-X[i])
    D.sort()
    print(sum(D[0:M-N]))