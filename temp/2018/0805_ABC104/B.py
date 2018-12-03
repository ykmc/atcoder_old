S = input()

Ans = "WA"
if S[0]=="A" and S[2:-1].count("C")==1:
    cnt = 0
    for s in S[1::]:
        if s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cnt += 1
    if cnt == 1:
        Ans = "AC"

print(Ans)