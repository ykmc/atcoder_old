N = int(input())
A = list(map(int,input().split()))

Ans = 0
for i in range(N):
    a = A[i]
    while a%2 == 0:
        a = a//2
        Ans += 1

print(Ans)