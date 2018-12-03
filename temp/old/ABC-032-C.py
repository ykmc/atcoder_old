N,K = map(int,input().split())
S = [int(input()) for _ in range(N)]

# 0 を含むなら答えはN
if 0 in S:
    print(N)
# 0 を含まないなら...
else:
    Ans,prod,Li,Ri = 0,1,0,0
    # 右端がN未満なら順次伸ばす
    while Ri < N:
        # 積を作る
        prod *= S[Ri]
        # 条件を満たすなら答えを更新
        if prod <= K:
            Ans = max(Ans, Ri-Li+1)
        # 条件を満たさないなら左端を調整
        else:
            # 条件を満たすまで左端を縮める
            while prod > K:
                prod //= S[Li]
                Li += 1
                # 左端が右端を追い越したらループ抜ける
                # 直後に右端を伸ばすので不整合は起きない
                if Li > Ri:
                    break
        Ri += 1
    print(Ans)