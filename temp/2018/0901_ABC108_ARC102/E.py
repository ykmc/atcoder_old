K,N = map(int,input().split())

MOD = 998244353

fact = [1]*4000
t = 1
for i in range(1,4000):
    t = (t*i)%MOD
    fact[i] = t

factinv = [1]*4000
for i in range(1,4000):
    factinv[i] = pow(fact[i], MOD-2, MOD)

def ncr(n,r):
    if n < 0 or r < 0 or n-r < 0:
        return 0
    return (fact[n] * factinv[r] * factinv[n-r]) % MOD

def nhr(n,r):
    if n == 0 and r == 0:
        return 1
    return ncr(n+r-1, r)

for i in range(2,2*K+1):
    t1,t2 = 0,0
    Ans = 0
    # p : 足して i になる整数の組の数
    np = i//2 - max(i-1-K,0)
    # p組からq組, 片方を使用する場合の数を足し合わせる
    # 偶奇で場合分け
    if i%2==0:
        # 偶数の場合 : 1組だけ同じ数の組があるため特別扱いする
        np -= 1
        for nq in range(np+1):
            # 同じ数の組の数字を全く含まない場合
            t1 = ncr(np,nq)*pow(2, nq, MOD)
            t1 %= MOD
            nr = K-np*2-1
            t2 = nhr(nr+nq,N-nq)
            t2 %= MOD
            Ans = (Ans + t1*t2) % MOD
            # 同じ数の組の数字を1つ含む場合
            t2 = nhr(nr+nq,N-nq-1)
            t2 %= MOD
            Ans = (Ans + t1*t2) % MOD
    else:
        # 奇数の場合 : p組全て互いに異なる数
        for nq in range(np+1):
            t1 = ncr(np,nq)*pow(2, nq, MOD)
            t1 %= MOD
            nr = K-np*2
            t2 = nhr(nr+nq,N-nq)
            t2 %= MOD
            Ans = (Ans + t1*t2) % MOD
    print(Ans%MOD)
