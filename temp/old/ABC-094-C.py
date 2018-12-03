N = int(input())
X = list(map(int,input().split()))
XS = sorted(X)
h = N//2
l,r = XS[h-1],XS[h]
for i in range(N):
    if X[i] <= l:
        print(r)
    else:
        print(l)