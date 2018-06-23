import sys
sys.setrecursionlimit(1000000)

N = int(input())
X = [[] for _ in range(N)]

for i in range(N-1):
    a,b,c = map(int,input().split())
    X[a-1].append((b-1,c))
    X[b-1].append((a-1,c))

cost = [-1]*N
def calc(i,c):
    # 指定の頂点までのコストを代入
    cost[i] = c
    # 頂点から移動できる頂点があれば
    for ni,nc in X[i]:
        # 初期状態のままなら計算
        if cost[ni] == -1:
            calc(ni,c+nc)

Q,K = map(int,input().split())
# 事前計算
calc(K-1,0)

for i in range(Q):
    x,y = map(int,input().split())
    print(cost[x-1]+cost[y-1])

