W,H,N = map(int,input().split())
X1,X2,Y1,Y2 = 0,W,0,H
for i in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        X1 = max(x,X1)
    elif a == 2:
        X2 = min(x,X2)
    elif a == 3:
        Y1 = max(y,Y1)
    elif a == 4:
        Y2 = min(y,Y2)
print(max(0,(X2-X1))*max(0,(Y2-Y1)))