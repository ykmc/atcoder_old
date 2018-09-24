N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

Ans = "War"
maxX = max(x)
minY = min(y)
for i in range(maxX+1,minY+1):
    if X < i <= Y:
        Ans = "No War"

print(Ans)