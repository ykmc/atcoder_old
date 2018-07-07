S = input()
w = int(input())

Ans = ""
while S:
    T,S = S[0:w],S[w:]
    Ans += T[0]

print(Ans)