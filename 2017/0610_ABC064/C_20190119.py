N = int(input())
A = list(map(int,input().split()))

Ans = 0
Cnt = [0]*9
for i in range(N):
    if A[i]>3200:
        A[i] = 3200
    Cnt[A[i]//400] += 1

for i in range(8):
    if Cnt[i]>0:
        Ans += 1

# 最低1色は必要
# 自由色が選択可能なのは8色だけではない
print(max(1,Ans), Ans+Cnt[8])