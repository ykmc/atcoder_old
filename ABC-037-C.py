N,K = map(int,input().split())
A = list(map(int,input().split()))
K = min(K,N-K+1)
Ans = 0
for i in range(N):
    if i < K:
        Ans += A[i]*(i+1)
    elif i < N-K:
        Ans += A[i]*K
    else:
        Ans += A[i]*(N-i)
print(Ans)