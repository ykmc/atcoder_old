N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(N-1+M)]

A = [[] for _ in range(N)]
P = [0]*N
C = [0]*N
root = -1

for (a,b) in AB:
    # a -> b
    A[a-1].append(b-1)
    C[b-1] += 1

for i in range(N):
    if C[i]==0:
        root = i
P[root] = -1

from collections import deque
que = deque((a,root) for a in A[root])
while que:
    n,par = que.popleft()
    C[n] -= 1
    if C[n]==0:
        P[n] = par
        for i in A[n]:
            que.append((i,n))

for p in P:
    print(p+1)

