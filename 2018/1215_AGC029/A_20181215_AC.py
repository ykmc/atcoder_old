S = input()[::-1]
ans = 0
tmp = 0
bcnt = 0
N = len(S)
for i in range(N):
    if S[i]=="W":
        tmp += 1
    else:
        ans += tmp
        bcnt += 1
        tmp = i+1-bcnt

print(ans)
