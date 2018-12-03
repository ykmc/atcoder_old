S = input()

Ans = "YES"
lenS = len(S)
for i in range(lenS//2):
    if S[i]==S[lenS-1-i] or S[i]=="*" or S[lenS-1-i]=="*":
        continue
    else:
        Ans = "NO"
        break

print(Ans)

