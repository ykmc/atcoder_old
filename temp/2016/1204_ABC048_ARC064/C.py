N,X = map(int,input().split())
A = list(map(int,input().split()))

Ans = 0
# 初項が超過している場合を考慮
d = max(0,A[0]-X)
A[0] -= d
Ans += d
# 第2項以降は貪欲に処理
for i in range(1,N):
    d = max(0,A[i]+A[i-1]-X)
    A[i] -= d
    Ans += d

print(Ans)