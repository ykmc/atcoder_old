S = input()
mod = 10**9+7

N = len(S)
A1,A2,C1,C2 = [1]*N,[1]*N,[1]*N,[1]*N
a,aa = 0,0
c,cc = 0,0
for i in range(1,N):
    if S[i-1]=="A":
        a += 1
    elif S[i-1]=="?":
        aa += 1
    A1[i],A2[i] = a,aa
for i in range(1,N):
    if S[N-1-i+1]=="C":
        c += 1
    elif S[N-1-i+1]=="?":
        cc += 1
    C1[N-1-i] = c
    C2[N-1-i] = cc

Ans = 0
for i in range(1,N-1):
    if S[i] in ("B","?"):
        ta,tc = 0,0
        if A2[i]==0:
            ta = A1[i]
        else:
            ta = pow(3,A2[i],mod)*A1[i] + pow(3,A2[i]-1,mod)*A2[i]
        if C2[i]==0:
            tc = C1[i]
        else:
            tc = pow(3,C2[i],mod)*C1[i] + pow(3,C2[i]-1,mod)*C2[i]
        Ans += ta*tc
        Ans %= mod

print(Ans)
