N,T = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
for i in range(1,N):
    if A[i] > A[i-1]+T:
        ans += T
    else:
        ans += A[i]-A[i-1]
ans += T

print(ans)
