from math import ceil
D,G = map(int,input().split())
P,C,A = [],[],[]
for i in range(D):
    p,c = map(int,input().split())
    P.append(p)
    C.append(c)
    A.append((i+1)*100*p+c)

Ans = []
# 全問解答する得点をbit全探索
for i in range(2**D):
    bits = bin(2**D+i)[3:]
    # 全問解いた時の得点と問題数を計算
    total,ans = 0,0
    for i,b in enumerate(bits):
        if b=="1":
            total += A[i]
            ans += P[i]
    # 目標を超えているなら解答候補に追加
    if total >= G:
        Ans.append(ans)
    # 目標を超えていないなら残りのうち一番得点が高い問題を順次解答
    else:
        j = 0 # 問題の前提から0で問題ない
        for i,b in enumerate(bits):
            if b=="0":
                j = i
        # 必要な残得点が問題数で達成可能かどうか
        res =  G - total
        if res/((j+1)*100) <= P[j]:
            ans += ceil(res/((j+1)*100))
            Ans.append(ans)

# 候補のうち最小のものが答え
print(min(Ans))
