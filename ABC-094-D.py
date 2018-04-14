N = int(input())
A = list(map(int,input().split()))
maxA = max(A)
half = maxA/2
t = 10000000000
for i in range(N):
    if A[i] != maxA and abs(A[i]-half) < abs(t-half):
        t = A[i]
print(maxA,t)