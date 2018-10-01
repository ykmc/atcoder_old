from collections import Counter
N = int(input())
A = list(map(int,input().split()))

C = Counter(A).most_common()
p = 0
for k,v in C:
    if v==1 and k==0 and N%2==1:
        continue
    elif v==2:
        p += 1
        continue
    else:
        p = 0
        break
if N==1 and A==[0]:
    print(1)
else:
    print(p if p==0 else (2**p)%(10**9+7))