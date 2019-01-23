N,T = map(int,input().split())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(1,N):
    if A[i]-A[i-1]<=T:
        ans += A[i]-A[i-1]
    else:
        ans += T
ans += T

print(ans)
