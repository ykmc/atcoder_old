X,Y,W = input().split()
X,Y = int(X)-1,int(Y)-1
C = [input() for _ in range(9)]

D = {"U":(0,-1),"D":(0,1),"R":(1,0),"L":(-1,0),"RU":(1,-1),"LU":(-1,-1),"RD":(1,1),"LD":(-1,1)}

Ans = ""
dx,dy = D[W]
for _ in range(4):
    Ans += C[Y][X]
    if not 0<= X+dx <=8:
        dx *= -1
    if not 0<= Y+dy <=8:
        dy *= -1
    X += dx
    Y += dy

print(Ans)

