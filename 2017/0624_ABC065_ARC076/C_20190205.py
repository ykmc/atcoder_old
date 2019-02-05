M,N = map(int,input().split())

ans = 1
modulo = 10**9+7
if N==M:
    for i in range(N):
        ans *= (i+1)
        ans %= modulo
        ans *= (i+1)
        ans %= modulo
    ans *= 2
    ans %= modulo
else:
    A,B = max(M,N),min(N,M)
    if A-B==1:
        for i in range(N):
            ans *= (i+1)
            ans %= modulo
        for i in range(M):
            ans *= (i+1)
            ans %= modulo
    else:
        ans = 0

print(ans)