N,X = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
if A[0]>X:
    ans = A[0]-X
    A[0] -= ans

for i in range(1,N):
    r = max(0, A[i]+A[i-1]-X)
    ans += r
    A[i] -= r

print(ans)