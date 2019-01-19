N = int(input())
A = list(map(int,input().split()))

Ans = [0]*N
for i in range(N):
    while A[i]%2==0:
        Ans[i] += 1
        A[i] //= 2

print(min(Ans))