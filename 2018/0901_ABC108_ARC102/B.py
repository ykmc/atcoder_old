x1,y1,x2,y2 = map(int,input().split())

dx,dy = x2-x1,y2-y1
x3,y3 = x2-dy,y2+dx
x4,y4 = x1-dy,y1+dx
print(x3,y3,x4,y4)