N,M = map(int,input().split())
P = list(map(int,input().split()))
XY = [tuple(map(int,input().split())) for _ in range(M)]

# Union-Find(1-indexed)
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def check(self, x, y):
        return self.find(x) == self.find(y)

# 交換可能な頂点でグルーピング
A = UnionFind(N)
for (x,y) in XY:
    A.unite(x,y)

# 頂点の数字(P[i]) と頂点番号(i+1) が同じグループかどうか
ans = 0
for i in range(N):
    if A.check(i+1,P[i]):
        ans += 1

print(ans)