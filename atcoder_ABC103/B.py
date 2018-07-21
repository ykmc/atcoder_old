S = input()
T = input()

lenS = len(S)
Ans = "No"
for i in range(lenS):
    if S==T:
        Ans = "Yes"
        break
    else:
        S = S[lenS-1:]+S[:lenS-1]

print(Ans)