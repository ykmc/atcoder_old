from collections import Counter
s,t = [],[]

N = int(input())
for i in range(N):
    s.append(input())

M = int(input())
for i in range(M):
    t.append(input())

sd = Counter(s)
td = Counter(t)
sd.subtract(td)

print(sd.most_common(1)[0][1])
