N,X = map(int,input().split())
A = list(map(int,input().split()))

bX = "{0:0b}".format(X)
bX = bX[::-1]
Ans = 0
for i,b in enumerate(bX):
    if b=="1":
        Ans += A[i]
print(Ans)