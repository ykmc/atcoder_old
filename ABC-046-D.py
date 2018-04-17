cp,score = 0,0
for s in input():
    if s == "g":
        if cp > 0:
            score += 1
            cp -= 1
        else:
            cp += 1
    elif s == "p":
        if cp > 0:
            cp -= 1
        else:
            score -= 1
            cp += 1
print(score)