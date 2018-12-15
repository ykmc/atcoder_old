H,W,N = map(int,input().split())
XY = []
ans = W
for i in range(N):
    x,y = map(int,input().split())
    XY.append((x,y))

XY.sort()

d = 0
for xy in XY:
    x,y = xy[0],xy[1]
    if x == y+d:
        d += 1
    elif x > y+d:
        ans = min(ans, x-1)

h = 1
ans2 = H
for xy in XY:
    x,y = xy[0],xy[1]
    if x > h:
        ans2 = max(ans2,H)
    else:
        ans2 = min(ans2,y-1)

print(ans,ans2)