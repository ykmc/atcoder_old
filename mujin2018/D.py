import sys
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())

# 判定結果
A = [[None for _ in range(1001)] for _ in range(1001)]
# チェック済み
C = [[None for _ in range(1001)] for _ in range(1001)]

def rev(n):
    return int(str(n)[::-1])

def solve(x,y):
    if x==0 or y==0:
        return False
    if A[x][y] is not None:
        return A[x][y]
    if C[x][y]==True:
        return True
    C[x][y] = True
    xx,yy = x,y
    if x<y:
        xx = rev(x)
    else:
        yy = rev(y)
    if xx<yy:
        yy = yy-xx
    else:
        xx = xx-yy
    A[x][y] = solve(xx,yy)
    return A[x][y]

Ans = 0
for n in range(N+1):
    for m in range(M+1):
        if solve(n,m):
            Ans += 1

print(Ans)
