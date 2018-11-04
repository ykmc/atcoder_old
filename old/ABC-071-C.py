from collections import Counter
N = int(input())
A = Counter(list(map(int,input().split()))).most_common()
fA = filter(lambda x: x[1] >= 2, A)
sA = sorted(fA,reverse=True)
if len(sA) < 2:
    print(0)
else:
    print(sA[0][0]**2 if sA[0][1]>=4 else sA[0][0]*sA[1][0])