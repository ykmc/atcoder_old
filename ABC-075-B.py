H,W = map(int,input().split())

S = []
D = [-1,0,1]

for _ in range(H):
    S.append(input())

Ans = ["" for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w]==".":
            cnt = 0
            for dh in D:
                for dw in D:
                    if h+dh >= 0  and  h+dh < H  and  w+dw >= 0  and  w+dw < W  and  S[h+dh][w+dw] == "#":
                        cnt += 1
            Ans[h] += str(cnt)
        else:
            Ans[h] += "#"

for h in range(H):
    print(Ans[h])

