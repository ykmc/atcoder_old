N = int(input())
A = list(map(int,input().split()))

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

ans = A[0]
for i in range(1,N):
    ans = gcd(ans,A[i])

print(ans)
