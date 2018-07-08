N,M,T = map(int,input().split())
A = list(map(int,input().split()))
M1 = [[] for _ in range(N)]
M2 = [[] for _ in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    M1[a-1].append((b-1,c))
    M2[b-1].append((a-1,c))


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

# 頂点iまでの最短距離
# - 頂点数,開始頂点,隣接リスト (v,cost)を設定する
nodeNum   = N
startNode = 0
adjList   = M1
cost1 = dijkstra(nodeNum, startNode, adjList)

# 頂点iからの最短距離
# - 頂点数,開始頂点,隣接リスト (v,cost)を設定する
nodeNum   = N
startNode = 0
adjList   = M2
cost2 = dijkstra(nodeNum, startNode, adjList)

# 滞在する都市を全探索
Ans = 0
for i in range(N):
    Ans = max(Ans, (T - (cost1[i]+cost2[i]))*A[i])

print(Ans)


