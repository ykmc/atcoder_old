from math import ceil
N = int(input())

Ans = 0
for i in range(1,N+1,2):
    d = []
    limit = ceil(N**.5)
    for j in range(1,limit):
        if i//j == i/j:
            if j not in d:
                d.append(j)
            if i//j not in d:
                d.append(i//j)
    if len(d)==8 and i%2==1:
        Ans += 1

print(Ans)


