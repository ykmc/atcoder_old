S = input()

Ans = "NO"
L = len(S)
for i in range(7):
    if S[0:i]+S[L-7+i:L]=="keyence":
        Ans = "YES"
        break

print(Ans)