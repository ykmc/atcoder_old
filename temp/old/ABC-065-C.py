N,M = map(int,input().split())

mod = 10**9+7
Ans = 0

if abs(N-M) == 0:
    t = 1
    for i in range(1,N+1):
        t = (t*i)%mod
    Ans = (2*t*t)%mod
elif abs(N-M) == 1:
    t1,t2 = 1,1
    for i in range(1,N+1):
        t1 = (t1*i)%mod
    for i in range(1,M+1):
        t2 = (t2*i)%mod
    Ans = (t1*t2)%mod

print(Ans)