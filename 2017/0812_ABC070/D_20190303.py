import sys
sys.setrecursionlimit(1000000)

def dfs(n,p,d):
    visited[n] = True
    dist[n] = d
    for (i,c) in A[n]:
        if i != p and not visited[i]:
            dfs(i,n,d+c)

N = int(input())
A = [[] for _ in range(N)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    A[a-1].append((b-1,c))
    A[b-1].append((a-1,c))
Q,K = map(int,input().split())
B = []
for _ in range(Q):
    x,y = map(int,input().split())
    B.append((x,y))

dist = [-1]*N
visited = [False]*N
dfs(K-1,N,0)

for (x,y) in B:
    print(dist[x-1]+dist[y-1])

