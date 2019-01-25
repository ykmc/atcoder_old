N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

from collections import Counter
CS = Counter(S).most_common()
CT = Counter(T)

ans = 0
for cs in CS:
    k,v = cs
    ans = max(ans, v-CT[k])

print(ans)
