H,W = map(int,input().split())
c,A,s = [],[],0
for i in range(10):
    c.append(list(map(int,input().split())))
for i in range(H):
    A.append(list(map(int,input().split())))
for i in range(10):
    for j in range(10):
        for k in range(10):
            c[j][k] = min(c[j][k], c[j][i]+c[i][k])
for i in range(10):
    for j in range(H):
        s = s + A[j].count(i) * c[i][1]
print(s)