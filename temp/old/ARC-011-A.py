m,n,N = map(int,input().split())

Ans = N
res = 0
i = 0
while True:
    if N//m >= 1:
        res += N%m
        N = N//m*n
        Ans += N
    else:
        N += res
        res = 0
        if N < m:
            break

print(Ans)