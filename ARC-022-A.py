S = input()

C = ["I","C","T"]
i = 0
Ans = "NO"
for s in S:
    if C[i]==s.upper():
        i += 1
    if i == 3:
        Ans = "YES"
        break

print(Ans)