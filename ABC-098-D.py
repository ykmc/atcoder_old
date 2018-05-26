N = int(input())
A = list(map(int,input().split()))

Ans = 0
j,xorA = 0,0
for i in range(N):
    while j < N and xorA&A[j] == 0:
        xorA |= A[j]
        j += 1
    Ans += j-i
    xorA ^= A[i]

print(Ans)