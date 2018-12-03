S = input()
T = input()
lenS,lenT = len(S),len(T)
n,Ans = 10000,"UNRESTORABLE"
if lenS >= lenT:
    for i in range(lenS-lenT,-1,-1):
        check = True
        for j in range(lenT):
            if S[i+j] != "?" and S[i+j] != T[j]:
                check = False
                break
        if check:
            n = i
            break
    if n < 10000:
        Ans = ""
        for i in range(lenS):
            if i >= n and i < n+lenT:
                Ans += T[i-n]
            elif S[i] == "?":
                Ans += "a"
            else:
                Ans += S[i]
print(Ans)           
            