N = int(input())
S = [int(input()) for _ in range(N)]

r = []
ans = 0
for i in range(N):
    ans += S[i]
    if S[i]%10!=0:
        r.append(S[i])

r.sort()
if ans%10==0:
    if len(r)>0:
        ans -= r[0]
    else:
        ans = 0

print(ans)

