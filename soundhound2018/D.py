N,M,S,T = map(int,input().split())
A = [[] for _ in range(N)]
B = [[] for _ in range(N)]
for i in range(M):
    u,v,a,b = map(int,input().split())
    A[u-1].append((v-1,a))
    A[v-1].append((u-1,a))
    B[u-1].append((v-1,b))
    B[v-1].append((u-1,b))


# ダイクストラ法のライブラリがないどころか過去1問もこれ使う問題解いてないwwwww
MAX_SIZE = N
MAX_VALUE = 10**20

visited = [False]*MAX_SIZE
cost = [MAX_VALUE]*MAX_SIZE
prev = [None]*MAX_SIZE




# ダイクストラ法でs,tそれぞれから各頂点への最短を、yenとsnuukで求める
# 各頂点で両替する時にどうなるか全探索
# 全探索結果を後ろから見て、自身より後ろにある全要素との最小を取っていく
# (前の両替所は使えないため)





