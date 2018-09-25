H,W,A,B = map(int,input().split())
MOD = 10**9+7

fact = [1]*200001
t = 1
for i in range(1,200001):
    t = (t*i)%MOD
    fact[i] = t

def ncr(n,r):
    return (fact[n] * pow(fact[r],MOD-2,MOD) % MOD) * pow(fact[n-r],MOD-2,MOD) % MOD

Ans = 0
for i in range(H-A):
    Ans += ncr(i+B-1,i)*ncr(W-B+H-i-2,W-B-1)

print(Ans%MOD)