N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

import sys
D,total1,total2,cnt1,cnt2 = [],0,0,0,0
for i in range(N):
    if A[i] == B[i]:
        continue
    elif A[i] > B[i]:
        D.append(A[i]-B[i])
    else:
        total1 += B[i]-A[i]
        cnt1 += 1

D.sort(reverse=True)

if total1==0:
    print(0)
    sys.exit()
else:
    for d in D:
        total2 += d
        cnt2 += 1
        if total2 >= total1:
            print(cnt1+cnt2)
            sys.exit()

print(-1)