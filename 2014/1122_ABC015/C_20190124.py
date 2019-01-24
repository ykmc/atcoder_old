N,K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]

def dfs(n,value):
    if n==N:
        return value==0
    for i in range(K):
        if dfs(n+1,value^T[n][i]):
            return True

if dfs(0,0):
    print("Found")
else:
    print("Nothing")