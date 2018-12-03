S = input()
T = input()

Ans = "You will lose"
for s,t in zip(S,T):
    if s == t:
        continue
    elif s == "@":
        if t in "atcoder":
            continue
        else:
            break
    elif t == "@":
        if s in "atcoder":
            continue
        else:
            break
    else:
        break
else:
    Ans = "You can win"


print(Ans)