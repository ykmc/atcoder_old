W,H = map(int,input().split())

MOD = 10**9+7

fact = [1]*200001
t = 1
for i in range(1,200001):
    t = (t*i)%MOD
    fact[i] = t

def ncr(n,r):
    return (fact[n] * pow(fact[r],MOD-2,MOD) % MOD) * pow(fact[n-r],MOD-2,MOD) % MOD

print(ncr(W+H-2,min(W-1,H-1)))