N = int(input())
P = [int(input()) for _ in range(N)]

maxP = max(P)
sumP = 0
for i in range(N):
    sumP += P[i]

print(sumP-maxP//2)
