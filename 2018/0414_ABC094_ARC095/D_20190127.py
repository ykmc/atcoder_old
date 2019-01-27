N = int(input())
A = list(map(int,input().split()))

maxA = max(A)
half = maxA/2
diff = 10**10
ans = 0
for i in range(N):
    if A[i] != maxA and abs(A[i]-half) < diff:
        diff = abs(A[i]-half)
        ans = A[i]

print(maxA, ans)