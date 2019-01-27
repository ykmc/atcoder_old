H,W = map(int,input().split())
S = [input() for _ in range(H)]

import sys
dd = [(1,0),(-1,0),(0,1),(0,-1)]
for h in range(H):
    for w in range(W):
        if S[h][w]=="#":
            chk = False
            for (dw,dh) in dd:
                if 0<=h+dh<H and 0<=w+dw<W:
                    if S[h+dh][w+dw]=="#":
                        chk = True
                        break
            if not chk:
                print("No")
                sys.exit()

print("Yes")
