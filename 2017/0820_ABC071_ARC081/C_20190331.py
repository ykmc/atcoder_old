N = int(input())
A = list(map(int,input().split()))

from collections import Counter

# 2本以上ある棒のみ集計
C = Counter(A).most_common()
D = []
for (k,v) in C:
    if v>=2:
        D.append((k,v))

D.sort()

# 一番長い棒が4本あれば正方形(も長方形のうち)
if len(D)>=1 and D[-1][1]>=4:
    print(D[-1][0]**2)
elif len(D)>=2:
    print(D[-1][0]*D[-2][0])
else:
    print(0)