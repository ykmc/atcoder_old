from collections import Counter
W = input()

Ans = "Yes"

C = Counter(W).items()
for c in C:
    _x,cnt = c
    if cnt%2 != 0:
        Ans = "No"
        break

print(Ans)

