N = int(input())
A = list(map(int,input().split()))
S = [A[0]]+[0]*(N-1)
for i in range(1,N):
    S[i] = S[i-1] + A[i]
Ans = 10**10
for i in range(0,N-1):
    Ans = min(Ans,abs(S[N-1]-S[i]*2))
print(Ans)