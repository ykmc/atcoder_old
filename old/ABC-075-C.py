N,M = map(int,input().split())

def dfs(v,a,b):
    visited[v] = True
    for n in E1[v]:
        if not visited[n] and set([v,n]) != set([a,b]):
            dfs(n,a,b)


E1 = [[] for _ in range(N)]
E2 = []
Ans = 0

for i in range(M):
    a,b = map(int,input().split())
    E1[a-1].append(b-1)
    E1[b-1].append(a-1)
    E2.append((a-1,b-1))
for i in range(M):
    visited = [True]+[False]*(N-1)
    a,b = E2[i]
    dfs(0,a,b)
    if visited != [True]*N:
        Ans += 1
print(Ans)