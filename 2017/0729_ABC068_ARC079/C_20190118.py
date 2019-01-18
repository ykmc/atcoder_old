N,M = map(int,input().split())
A = [set() for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    A[a-1].add(b-1)
    A[b-1].add(a-1)

print("POSSIBLE" if A[0] & A[N-1] != set() else "IMPOSSIBLE")
