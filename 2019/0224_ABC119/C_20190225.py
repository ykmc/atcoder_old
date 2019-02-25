N,A,B,C = map(int,input().split())
L = [int(input()) for _ in range(N)]

from itertools import product
ans = float("inf")
for p in product(range(4),repeat=N):
    a = [L[i] for i in range(N) if p[i]==1]
    b = [L[i] for i in range(N) if p[i]==2]
    c = [L[i] for i in range(N) if p[i]==3]

    if a==[] or b==[] or c==[]:
        continue
    
    t = 0
    for x in [a,b,c]:
        if len(x)>=2:
            t += (len(x)-1)*10
    sumA = sum(a)
    sumB = sum(b)
    sumC = sum(c)
    t += abs(A-sumA) + abs(B-sumB) + abs(C-sumC)

    ans = min(ans,t)

print(ans)