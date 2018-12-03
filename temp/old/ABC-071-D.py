N = int(input())
S1 = input()
S2 = input()
i = 0
T = []
while i < N:
    if S1[i]==S2[i]:
        T.append("C")
    else:
        T.append("R")
        i += 1
    i += 1
Ans = 3 if T[0]=="C" else 6
for i in range(1,len(T)):
    if T[i-1] == "C":
        if T[i] == "C":
            Ans *= 2
        else:
            Ans *= 2
    else:
        if T[i] == "C":
            Ans *= 1
        else:
            Ans *= 3
    Ans %= 10**9+7
print(Ans)