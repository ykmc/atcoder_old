from collections import defaultdict
N,K,L = map(int,input().split())

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

P,Q = UnionFind(N),UnionFind(N)
for _ in range(K):
    x,y = map(int,input().split())
    P.unite(x,y)
for _ in range(L):
    x,y = map(int,input().split())
    Q.unite(x,y)

D = defaultdict(int)
for i in range(1,N+1):
    D[P.find(i),Q.find(i)] += 1

print(" ".join(map(str,list(D[P.par[i],Q.par[i]] for i in range(1,N+1)))))