N = int(input())
A = list(map(int,input().split()))

A.sort()
ans = 1
mod = 10**9+7

if len(A)%2==0:
    for i in range(N//2):
        if A[i*2] == A[i*2+1] == i*2+1:
            ans *= 2
            ans %= mod
        else:
            ans = 0
            break
else:
    for i in range((N-1)//2):
        if A[i*2+1] == A[i*2+2] == (i+1)*2:
            ans *= 2
            ans %= mod
        else:
            ans = 0
            break
    if A[0]!=0:
        ans = 0

print(ans)