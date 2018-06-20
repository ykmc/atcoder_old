S = input()

L = len(S)
chk = False
ans1,ans2 = 0,0

# 連続する2文字が同じである
for i in range(1,L):
    if S[i]==S[i-1]:
        chk = True
        ans1,ans2 = i,i+1
        break

# 連続する3文字の1,3が同じ
# ならば3文字部分文字列において過半数獲得
if not chk:
    for i in range(2,L):
        if S[i]==S[i-2]:
            chk = True
            ans1,ans2 = i-1,i+1
            break

if chk:
    print(ans1,ans2)
else:
    print(-1,-1)

