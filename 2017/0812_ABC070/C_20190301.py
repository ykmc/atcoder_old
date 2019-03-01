def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

N = int(input())
T = [int(input()) for _ in range(N)]

Ans = T[0]
for i in range(1,N):
    Ans //= gcd(Ans,T[i])
    Ans *= T[i]

print(Ans)