S = input()

# 逆順にする
S = S[::-1]

# 黒石より右にある白石の数だけ操作可能
ans = 0
white = 0
for i in range(len(S)):
    if S[i]=="B":
        ans += white
    else:
        white += 1

print(ans)