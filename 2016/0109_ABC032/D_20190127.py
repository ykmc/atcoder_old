N,W = map(int,input().split())
VW = [tuple(map(int,input().split())) for _ in range(N)]

maxV,maxW = 0,0
for (v,w) in VW:
    maxV = max(maxV,v)
    maxW = max(maxW,w)

ans = 0
# i) 30個まで
if N<=30:
    # 半分全列挙
    A,B = VW[:N//2],VW[N//2:]
    lenA,lenB = len(A),len(B)
    AA,BB = [],[]
    for i in range(2**lenA):
        bits = bin(2**lenA+i)[3:]
        v = sum([v for (v,w),bit in zip(A,bits) if bit=="1"])
        w = sum([w for (v,w),bit in zip(A,bits) if bit=="1"])
        AA.append((w,v))
    for i in range(2**lenB):
        bits = bin(2**lenB+i)[3:]
        v = sum([v for (v,w),bit in zip(B,bits) if bit=="1"])
        w = sum([w for (v,w),bit in zip(B,bits) if bit=="1"])
        BB.append((w,v))
    # 重さでソートし、自明に不要な要素を除く(重さが増えてるのに価値が下がっている組)
    AA.sort()
    BB.sort()
    AAA = []
    BBB = []
    temp = -1
    for (w,v) in AA:
        if v>temp:
            temp = v
            AAA.append((w,v))
    temp = -1
    for (w,v) in BB:
        if v>temp:
            temp = v
            BBB.append((w,v))
    # A群 + B群 の最適な組み合わせを二分探索で求める
    from bisect import bisect_right
    for (aw,av) in AAA:
        if aw<=W:
            bw,bv = BBB[bisect_right(BBB,(W-aw,float("inf")))-1]
            ans = max(ans,av+bv)

# ii) 重さが1000以下のとき
elif maxW <= 1000:
    # dp[i] : 重さiでの最大価値
    dp = [0]*(W+1)
    for (v,w) in VW:
        for i in reversed(range(W+1)):
            if i-w>=0:
                dp[i] = max(dp[i], dp[i-w]+v)
    ans = dp[W]

# iii) 価値が1000以下
elif maxV <= 1000:
    # dp[i] : 価値iを達成する最小の重さ
    dp = [9999999999999999]*(N*maxV+1)
    dp[0] = 0
    for (v,w) in VW:
        for i in reversed(range(N*maxV+1)):
            if i-v>=0:
                dp[i] = min(dp[i], dp[i-v]+w)
    for i in range(N*maxV+1):
        if dp[i]<=W:
            ans = max(ans,i)

print(ans)

