N = int(input())
A = list(map(int,input().split()))

from collections import Counter
C = Counter(A).most_common()

ans = 0
for (k,v) in C:
    if v<k:
        ans += v
    elif v>k:
        ans += v-k

print(ans)