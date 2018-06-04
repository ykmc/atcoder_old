N,A,B,K = map(int,input().split())
MOD = 998244353

# 拡張ユークリッド互除法
# ax + by = gcd(a,b)の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# 組み合わせを全部メモ化
C = [0]*(N+1)
C[0] = C[N] = 1
for k in range(1,N//2+1):
    v = C[k-1]*(N-k+1)*modinv(k,MOD)
    v %= MOD
    C[k] = C[N-k] = v

Ans = 0
A,B = max(A,B),min(A,B)
for ai in range(N+1):
    bi = (K-A*ai)//B
    if 0<= bi <=N and A*ai + B*bi == K:
        Ans += C[ai] * C[bi]
        Ans %= MOD

print(Ans)