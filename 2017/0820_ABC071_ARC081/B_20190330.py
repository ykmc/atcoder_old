S = input()

Ans = "None"
for i in range(26):
    if chr(i+97) not in S:
        Ans = chr(i+97)
        break

print(Ans)