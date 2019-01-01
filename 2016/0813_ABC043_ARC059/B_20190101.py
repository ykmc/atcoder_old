S = input()

ans = []
for s in S:
    if s in ["0","1"]:
        ans.append(s)
    elif s == "B" and ans != []:
        ans = ans[:-1]

print("".join(ans))