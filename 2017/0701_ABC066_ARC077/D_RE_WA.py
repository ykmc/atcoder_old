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


from collections import Counter
N = int(input())
A = list(map(int,input().split()))

# 重複している数を調べる
C = Counter(A).most_common()
x = C[0][0]

# 重複している数のindexを調べる
xi = []
for i in range(N):
    if A[i]==x:
        xi.append(i)
h = xi[1]-xi[0]+1
print(xi)

for i in range(1,N+2):
    print(nCr(N+1,i,modulo,fact,finv) - nCr(N+1-h,i-1,modulo,fact,finv))