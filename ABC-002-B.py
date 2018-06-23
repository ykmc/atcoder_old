W = input()

Ans = ""
for w in W:
    if w not in "aiueo":
        Ans += w

print(Ans)