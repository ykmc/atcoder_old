S = input()
chars = "abcdefghijklmnopqrstuvwxyz"
if len(S) < 26:
    for c in chars:
        if c not in S:
            Ans = S+c
            break
else:
    if S == chars[::-1]:
        Ans = -1
    else:
        for i in range(25):
            if S[25-i] > S[25-i-1]:
                break
        for j in range(25): # index out of rangeにならない？大丈夫？
            if chr(ord(S[25-i-1])+1+j) not in S[0:25-i-1]:
                break
        Ans = S[0:25-i-1]+chr(ord(S[25-i-1])+1+j)
print(Ans)