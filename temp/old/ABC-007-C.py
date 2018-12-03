R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
A = [["" for _ in range(C)] for _ in range(R)]
for i in range(R):
    s = input()
    for j in range(C):
        A[i][j] = s[j]

A[sy-1][sx-1] = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(L):
    while L:
        l = L.pop(0)
        y,x = l
        for i in range(4):
            #範囲に入っている
            yi = y+dy[i]
            xi = x+dx[i]
            if 0 <= yi < R and 0<= xi < C:
                # 壁ではない
                if A[yi][xi] != "#":
                    # 未判定なら+1
                    if A[yi][xi] == ".":
                        A[yi][xi] = A[y][x]+1
                        L.append((yi,xi))

bfs([(sy-1,sx-1)])
print(A[gy-1][gx-1])
