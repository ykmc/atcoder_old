H,W,A,B = map(int,input().split())

def init_fact(n,mod):
    fact,finv,inv = [1]*n,[1]*n,[1]*n
    for i in range(2,n):
        fact[i] = (fact[i-1]*i) % mod
        inv[i]  = mod - inv[mod%i] * (mod//i)%mod
        finv[i] = finv[i-1] * inv[i] % mod
    return (fact,finv,inv)

def nCr(n,r,mod,fact,finv):
    if n<r:
        return 0
    else:
        return fact[n] * (finv[r] * finv[n-r] % mod) % mod

modulo = 10**9+7
fact,finv,inv = init_fact(200000,modulo)

ans = 0
for i in range(H-A):
    ans += nCr(i+B-1,i,modulo,fact,finv) * nCr(H-i-1+W-B-1,W-B-1,modulo,fact,finv)
    ans %= modulo

print(ans)