import sys
sys.setrecursionlimit(500000)
H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(input())

def dfs(h,w,i,c):
    # グループ分け
    V[h][w] = i
    # 上
    if h>0 and V[h-1][w]==0:
        if c=="#" and S[h-1][w]==".":
            dfs(h-1,w,i,".")
        elif c=="." and S[h-1][w]=="#":
            dfs(h-1,w,i,"#")
    # 左
    if w>0 and V[h][w-1]==0:
        if c=="#" and S[h][w-1]==".":
            dfs(h,w-1,i,".")
        elif c=="." and S[h][w-1]=="#":
            dfs(h,w-1,i,"#")
    # 下
    if h<H-1 and V[h+1][w]==0:
        if c=="#" and S[h+1][w]==".":
            dfs(h+1,w,i,".")
        elif c=="." and S[h+1][w]=="#":
            dfs(h+1,w,i,"#")
    # 右
    if w<W-1 and V[h][w+1]==0:
        if c=="#" and S[h][w+1]==".":
            dfs(h,w+1,i,".")
        elif c=="." and S[h][w+1]=="#":
            dfs(h,w+1,i,"#")

V = [[0 for _ in range(W)] for _ in range(H)]
ans = 0
i = 0
for h in range(H):
    for w in range(W):
        if S[h][w]=="#" and V[h][w]==0:
            i += 1
            dfs(h,w,i,"#")

# iグループに分割完了
cnt_b = [0]*i
cnt_w = [0]*i

for h in range(H):
    for w in range(W):
        group = V[h][w]
        if group != 0:
            if S[h][w]=="#":
                cnt_b[group-1] += 1
            else:
                cnt_w[group-1] += 1

ans = 0
for i in range(len(cnt_b)):
    ans += cnt_b[i]*cnt_w[i]

print(ans)
