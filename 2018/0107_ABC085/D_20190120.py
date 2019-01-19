N,H = map(int,input().split())
A,B = [],[]
maxA,maxAi = -1,-1
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    if maxA < a:
        maxA = a
        maxAi = i

T = []
for i in range(N):
    if B[i] >= maxA:
        T.append(B[i])

import sys
atk = 0
T.sort(reverse=True)
for t in T:
    H -= t
    atk += 1
    if H <= 0:
        print(atk)
        sys.exit()

print(atk + (H-1)//maxA + 1)



