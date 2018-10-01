N = int(input())
S = list(map(int,input().split()))
A = list(map(int,input().split()))

Ans = 0
for i in range(N):
    Ans = max(Ans, S[i]*A[i])

print(Ans)