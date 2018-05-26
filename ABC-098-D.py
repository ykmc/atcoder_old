N = int(input())
A = list(map(int,input().split()))

Ans = 0
j,tmp = 0,0
for i in range(N):
    while j < N and tmp&A[j] == 0:
        tmp |= A[j]
        j += 1
    Ans += j-i
    tmp ^= A[i]

print(Ans)