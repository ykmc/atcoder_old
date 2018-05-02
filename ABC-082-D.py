S = input()+"T"
X,Y = map(int,input().split())
dX0,dX,dY,dr,dc = 0,[],[],"x",0
for s in S:
    if s == "F":
        dc += 1
    elif s == "T":
        if dr == "x":
            dr = "y"
            dX.append(dc)
        else:
            dr = "x"
            dY.append(dc)
        dc = 0
dX0,dX = dX[0],dX[1:]

canX,canY = [dX0],[0]
for dx in dX:
    t = []
    for cx in canX:
        t.append(cx+dx)
        t.append(cx-dx)
    canX = list(set(t))

for dy in dY:
    t = []
    for cy in canY:
        t.append(cy+dy)
        t.append(cy-dy)
    canY = list(set(t))

print("Yes" if X in canX and Y in canY else "No")