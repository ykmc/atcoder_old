S = input()[::-1]
T = ["dream"[::-1],"dreamer"[::-1],"erase"[::-1],"eraser"[::-1]]
Ans = "YES"
while len(S) > 0:
    if S[0:5] in T:
        S = S[5:]
        continue
    elif S[0:6] in T:
        S = S[6:]
        continue
    elif S[0:7] in T:
        S = S[7:]
        continue
    else:
        Ans = "NO"
        break
print(Ans)