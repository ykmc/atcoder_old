N,X = map(int,input().split())
A = list(map(int,input().split()))

from collections import Counter

for i in range(N):
    A[i] -= X

A0 = A[0]
ans = []
ans2 = []
for i in range(1,int(abs(A0)**.5)+1):
    if A0%i==0 and i not in ans:
        ans.append(i)

ans2 = ans.copy()
for a in ans:
    if abs(A0//a) not in ans:
        ans2.append(abs(A0//a))

Ans = 1
for a in ans2:
    for i in range(N):
        if A[i]%a==0:
            continue
        else:
            break
    else:
        Ans = max(Ans,a)

print(Ans)