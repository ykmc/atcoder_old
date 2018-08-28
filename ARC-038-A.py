N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)

Ans = 0
for i in range(N):
    if i%2==0:
        Ans += A[i]

print(Ans)
