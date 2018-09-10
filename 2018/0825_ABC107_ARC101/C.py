N,K = map(int,input().split())
X = list(map(int,input().split()))

X.sort()
Ans = 10**20
for i in range(N-K+1):
    l = X[i]
    r = X[i+K-1]
    # 0を含む または 同じ符号の場合
    if l*r >= 0:
        ans = max(abs(l),(r))
    # 符号が異なる場合
    else:
        ans = max(abs(l),abs(r)) + min(abs(l),abs(r))*2
    Ans = min(Ans,ans)

print(Ans)