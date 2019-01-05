S = input()

cntP = 0
for s in S:
    if s=="p":
        cntP += 1

print(len(S)//2 - cntP)
