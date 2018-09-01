N,K = map(int,input().split())

Ans = 0
if K%2==1:
    Ans = (N//K)**3
else:
    Ans = ((N+K//2)//K)**3 + (N//K)**3 

print(Ans)