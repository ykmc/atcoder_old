N,M = map(int,input().split())

E = [[] for _ in range(N)]
visited = [False]*N
visited_all = [True]*N

def DFS(V):
    if visited == visited_all:
        return 1
    count = 0
    for e in E[V]:
        if not visited[e]:
            visited[e] = True
            count += DFS(e) 
            visited[e] = False
    else:
        return count

for i in range(M):
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

visited[0] = True
print(DFS(0))