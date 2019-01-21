N = int(input())
S = [input() for _ in range(N)]

from itertools import combinations
c = list(combinations([i for i in range(5)],3))

cnt = [0]*6
for i in range(N):
    cnt["MARCH".find(S[i][0])] += 1

ans = 0
for (i,j,k) in c:
    ans += cnt[i]*cnt[j]*cnt[k]

print(ans)