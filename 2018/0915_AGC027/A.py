N,X = map(int,input().split())
A = list(map(int,input().split()))

ans = 0

sumA = sum(A)
A.sort()

if sumA == X:
    ans = N
elif sumA < X:
    ans = N-1
else:
    for i in range(N):
        if A[i] <= X:
            X -= A[i]
            ans += 1
        else:
            break

print(ans)
