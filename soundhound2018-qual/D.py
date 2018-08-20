N,M,S,T = map(int,input().split())
yX = [[] for _ in range(N)]
sX = [[] for _ in range(N)]
for i in range(M):
    u,v,a,b = map(int,input().split())
    yX[u-1].append((v-1,a))
    yX[v-1].append((u-1,a))
    sX[u-1].append((v-1,b))
    sX[v-1].append((u-1,b))

# 0-indexed
S,T = S-1,T-1

# ---------- ---------- ---------- ---------- ---------- ----------
# dijkstra's algorithm
# ---------- ---------- ---------- ---------- ---------- ----------
import heapq
INF = float("inf")
# main
def dijkstra(start, adjList, cost):
    hq = [(0,start)]
    heapq.heapify(hq)
    while hq:
        hc, hv = heapq.heappop(hq)
        for to, c in adjList[hv]:
            if hc + c >= cost[to]:
                continue
            cost[to] = hc + c
            heapq.heappush(hq, (cost[to],to))

# 頂点数,開始頂点,隣接リスト (v,cost)
dN,start,dM = N,S,yX
# コスト
cost1 = [INF]*dN
cost1[start] = 0
# 実行
dijkstra(start, dM, cost1)



# 頂点数,開始頂点,隣接リスト (v,cost)
dN,start,dM = N,T,sX
# コスト
cost2 = [INF]*dN
cost2[start] = 0
# 実行
dijkstra(start, dM, cost2)

Ans = [INF]
for i in reversed(range(N)):
    Ans.append(min(Ans[-1], cost1[i]+cost2[i]))

for ans in reversed(Ans[1:]):
    print(10**15 - ans)
