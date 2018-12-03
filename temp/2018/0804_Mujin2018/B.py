A = int(input())
S = input()

Ans = "No"
for s in S:
    if A == 0:
        Ans = "Yes"
    if s == "+":
        A += 1
    else:
        A -= 1
    if A == 0:
        Ans = "Yes"

print(Ans)