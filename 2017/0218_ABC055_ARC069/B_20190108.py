N = int(input())

ans,modulo = 1,10**9+7
for i in range(1,N+1):
    ans *= i
    ans %= modulo

print(ans)
