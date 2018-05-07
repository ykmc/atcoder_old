N = int(input())
G = [[] for _ in range(N)]
visited = [0]*N
visited[0],visited[N-1] = 1,1
visited_all = [1]*N
for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
nextA,nextB = G[0],G[N-1]
scoreA,scoreB = 1,1
while visited != visited_all:
    l = []
    for a in nextA:
        if visited[a] == 0:
            visited[a] = 1
            scoreA += 1
            for x in G[a]:
                l.append(x)
    nextA = l
    l = []
    for b in nextB:
        if visited[b] == 0:
            visited[b] = 1
            scoreB += 1
            for x in G[b]:
                l.append(x)
    nextB = l
print("Fennec" if scoreA > scoreB else "Snuke")
