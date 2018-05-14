N,M = map(int,input().split())
P = list(map(int,input().split()))

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

uf = UnionFind(N)

for _ in range(M):
    x,y = map(int,input().split())
    uf.unite(x,y)

Ans = 0
for i,p in enumerate(P,1):
    if uf.check(i,p):
        Ans += 1

print(Ans)