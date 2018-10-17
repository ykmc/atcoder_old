N = int(input())
MOD = 10**9+7
Ans = 1
for i in range(1,N+1):
    Ans = Ans*i % MOD
print(Ans)
