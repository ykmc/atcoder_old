N,M = map(int,input().split())

if N<M:
    N,M = M,N

ans = 0
if M==1:
    if N==1:
        ans = 1
    else:
        ans = N-2
elif M==2:
    ans = 0
else:
    ans = (N-2)*(M-2)

print(ans)