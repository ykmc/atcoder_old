N,M = map(int,input().split())
adjM = [[] for _ in range(N)]
for i in range(M):
    a,b,t = map(int,input().split())
    adjM[a-1].append((b-1,t))
    adjM[b-1].append((a-1,t))

# ---------- ---------- ---------- ---------- ---------- ----------
# dijkstra's algorithm
# ---------- ---------- ---------- ---------- ---------- ----------
import heapq
INF = float("inf")
# main
def dijkstra(nodenum, start, adjList):
    cost = [INF]*nodeNum
    cost[startNode] = 0
    hq = [(0,start)]
    heapq.heapify(hq)
    while hq:
        hc, hv = heapq.heappop(hq)
        for to, c in adjList[hv]:
            if hc + c >= cost[to]:
                continue
            cost[to] = hc + c
            heapq.heappush(hq, (cost[to],to))
    return cost

nodeNum   = N
adjList   = adjM

Ans = INF
for i in range(N):
    startNode = i
    cost = dijkstra(nodeNum, startNode, adjList)
    Ans = min(Ans, max(cost))

print(Ans)