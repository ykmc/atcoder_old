from collections import Counter
S = input()
T = input()

cntS = Counter(S).most_common()
cntT = Counter(T).most_common()

Ans = "Yes"
if len(cntS)==len(cntT):
    for i in range(len(cntT)):
        if cntS[i][1] != cntT[i][1]:
            Ans = "No"
else:
    Ans = "No"

print(Ans)