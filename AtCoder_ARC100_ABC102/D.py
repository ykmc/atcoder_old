N = int(input())
A = list(map(int,input().split()))
from bisect import bisect

# 区間の和を高速に求めたいので累積和
S = [0]*N
S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1]+A[i]

Ans = 10**15
# 真ん中の分割位置を全探索
for i in range(2,N-1):
    # 前半部分,後半部分をそれぞれできるだけ均等になるように分割
    ax = S[i-1]/2
    ai = bisect(S,ax)
    if abs(S[ai-1]-ax) < abs(S[ai]-ax):
        ai -= 1
    bx = (S[N-1]+S[i-1])/2
    bi = bisect(S,bx)
    if abs(S[bi-1]-bx) < abs(S[bi]-bx):
        bi -= 1
    x1,x2,x3,x4 = S[ai],S[i-1]-S[ai],S[bi]-S[i-1],S[N-1]-S[bi]
    # 考慮した組み合わせで最小のものを記録
    Ans = min(Ans,max(x1,x2,x3,x4)-min(x1,x2,x3,x4))

print(Ans)