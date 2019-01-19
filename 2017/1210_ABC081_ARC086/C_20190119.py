N,K = map(int,input().split())
A = list(map(int,input().split()))

from collections import Counter
C = list(Counter(A).most_common())

Ans = 0
for i in range(len(C)-K):
    Ans += C[-1-i][1]

print(Ans)