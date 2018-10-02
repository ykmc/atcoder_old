N = int(input())
S = input()
Ans,t = 0,0
for s in S:
    if s == "I":
        t += 1
    else:
        t -= 1
    Ans = max(Ans,t)
print(Ans)