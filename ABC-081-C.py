from collections import Counter
N,K = map(int,input().split())
AC = Counter(list(map(int,input().split()))).most_common()[::-1]
C = 0
if len(AC) > K:
    for i in range(len(AC)-K):
        k,v = AC[i]
        C += v
print(C)