import sys
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

Ans = 0
if A[0]>0:
    print(-1)
else:
    for i in range(N-1):
        d = A[N-1-i]-A[N-2-i]
        if d>1:
            print(-1)
            sys.exit()
        elif d<=0:
            Ans += A[N-1-i]
        elif d==1:
            Ans += 1
    print(Ans)
    
