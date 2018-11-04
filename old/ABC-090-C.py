N,M = map(int,input().split())

N,M = min(N,M),max(N,M)
Ans = 0
if N==1 and M==1:
    Ans = 1
elif N==1:
    Ans = M-2
elif N==2:
    Ans = 0
else:
    Ans = (N-2)*(M-2)

print(Ans)