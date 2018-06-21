H,W = map(int,input().split())

Ans = H*W
if H%3==0 or W%3==0:
    Ans = 0
elif H%2==0 and W%2==0:
    Ans = min(H//2,W//2)
else:
    # 全探索するしかない？
    for i in range(1,H):
        t = W//2
        Ans = min(Ans, max(W*i,(H-i)*t,(H-i)*(W-t))-min(W*i,(H-i)*t,(H-i)*(W-t)))
        t = (H-i)//2
        Ans = min(Ans, max(W*i,W*t,W*(H-i-t))-min(W*i,W*t,W*(H-i-t)))
    H,W = W,H
    for i in range(1,H):
        t = W//2
        Ans = min(Ans, max(W*i,(H-i)*t,(H-i)*(W-t))-min(W*i,(H-i)*t,(H-i)*(W-t)))
        t = (H-i)//2
        Ans = min(Ans, max(W*i,W*t,W*(H-i-t))-min(W*i,W*t,W*(H-i-t)))

print(Ans)