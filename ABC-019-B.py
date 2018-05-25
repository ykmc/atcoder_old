S = input()
Ans,n = S[0],1
for i in range(1,len(S)):
    if S[i-1] == S[i]:
        n += 1
    else:
        Ans += str(n)
        Ans += S[i]
        n = 1
else:
    Ans += str(n)
print(Ans)
