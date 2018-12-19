N,T = map(int,input().split())

Ans = 9999
for i in range(N):
    c,t = map(int,input().split())
    if t<=T:
        Ans = min(Ans,c)

print(Ans if Ans != 9999 else "TLE")
