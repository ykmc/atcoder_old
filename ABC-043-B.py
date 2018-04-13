S = input()
T = ""
for w in S:
    if w == "B" and T != "":
        T=T[:-1]
    elif w != "B":
        T += w
print(T)