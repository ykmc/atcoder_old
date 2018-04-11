from collections import Counter
N = int(input())
d = []
for i in range(N):
    d.append(int(input()))
C = Counter(d)
print(len(C))