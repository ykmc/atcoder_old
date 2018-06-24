N = int(input())
C = [int(input()) for _ in range(N)]

# i番目のコインを割り切ることができるコインの種類数
R = [0]*N
for i in range(N):
    for c in C:
        if C[i]%c== 0:
            R[i] += 1
    #自分自身では当然割り切れるので -1して調整
    R[i] -= 1

Ans = 0
## R[i]の偶奇で場合わけ
for i in range(N):
    # R[i]が奇数 → 自分自身を含めた順列で、自分より左に約数が奇数個・偶数個あるのは等確率
    if R[i]%2 == 1:
        Ans += 0.5
    # R[i]が偶数 → 自分自身を含めた順列で、自分より左に約数が偶数個ある確率は・・・
    else:
        Ans += (R[i]/2+1)/(R[i]+1)

# 雑な考察
# 0 -> 1
# 2 -> 2/3, xoo:OK oxo:NG oox:OK
# 4 -> 3/5, xoooo:OK oxooo:NG ooxoo:OK oooxo:NG oooox:OK
# 6 -> 4/7
# ...
# k -> (k/2+1)/(k+1)

print(Ans)