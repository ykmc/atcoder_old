A = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    A[i][0],A[i][1],A[i][2],A[i][3] = map(int,input().split())

dd = [(1,0),(-1,0),(0,1),(0,-1)]
Ans = "GAMEOVER"

for i in range(4):
    for j in range(4):
        for d in dd:
            dx,dy = d
            if 0<=i+dx<4 and 0<=j+dy<4 and A[i][j]==A[i+dx][j+dy]:
                Ans = "CONTINUE"

print(Ans)