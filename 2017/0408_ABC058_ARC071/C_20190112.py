N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)

ans = []
chars = "abcdefghijklmnopqrstuvwxyz"
for c in chars:
    cnt = 999
    for i in range(N):
        cnt = min(cnt, S[i].count(c))
    for i in range(cnt):
        ans.append(c)

print("".join(ans))
