N = int(input())
A = list(map(int,input().split()))

Ans = 0
for i in range(N):
    Ans += A[i]-1

print(Ans)