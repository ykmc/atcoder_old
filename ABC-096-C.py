H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(input())
Ans = "Yes"
for i in range(H):
    for j in range(W):
        check = ""
        if j-1 >= 0:
            check += S[i][j-1]
        if j+1 <= W-1:
            check += S[i][j+1]
        if i-1 >= 0:
            check += S[i-1][j]
        if i+1 <= H-1:
            check += S[i+1][j]
        if S[i][j]=="#" and "#" not in check:
            Ans = "No"
print(Ans)