N = int(input())
S = int(input())

def f(b,n):
    if n//b==0:
        return n
    else:
        return n%b + f(b,n//b)

ans = -1
if S==N:
    ans = N+1
else:
    for b in range(2,int(N**.5)+1):
        if f(b,N)==S:
            ans = b
            break

if ans == -1:
    for i in range(int(N**.5)+1,0,-1):
        b = (N-S)//i + 1
        if b>1:
            if f(b,N)==S:
                ans = b
                break

print(ans)