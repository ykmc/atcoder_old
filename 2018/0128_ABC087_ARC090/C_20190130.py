N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Ans = 0
for i in range(N):
    ans = 0
    for j in range(i+1):
        ans += A[j]
    for j in range(i,N):
        ans += B[j]
    Ans = max(Ans,ans)
print(Ans)