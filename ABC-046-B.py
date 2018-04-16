N,K = map(int,input().split())
Ans = K
for i in range(1,N):
    Ans *= (K-1)
print(Ans)