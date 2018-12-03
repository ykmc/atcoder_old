N = int(input())
P = []
for i in range(N):
    P.append(int(input()))

d = [0]*(N+1)
for p in P:
    d[p] = d[p-1]+1

print(N-max(d))