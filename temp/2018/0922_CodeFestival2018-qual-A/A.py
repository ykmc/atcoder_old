A = int(input())
B = int(input())
C = int(input())
S = int(input())

AA = [A,A+1]
BB = [B,B+1]
CC = [C,C+1]

Ans = "No"
for a in AA:
    for b in BB:
        for c in CC:
            if a+b+c == S:
                Ans = "Yes"

print(Ans)