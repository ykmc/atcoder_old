N = int(input())
S = []
Ans = []
for i in range(N):
    S.append(input())
for i in range(N):
    l = ""
    for j in range(N):
        l += S[N-j-1][i]
    Ans.append(l)
for i in range(N):
    print(Ans[i])


