S,C,N = map(int,input().split())
X = input()

for x in X:
    if x == "E":
        if C > 1 and C > S:
            x = "C"
        else:
            x = "S" 

    if x == "S":
        S = max(0,S-1)
    elif x == "C":
        C = max(0,C-1)

print(S)
print(C)