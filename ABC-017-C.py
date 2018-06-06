N,M = map(int,input().split())
A = [0 for _ in range(M+2)]
total = 0
for i in range(N):
    l,r,s = map(int,input().split())
    A[l] += s
    A[r+1] -= s
    total += s

for i in range(M+1):
    A[i+1] += A[i]

A = A[1:M+1]
print(total - min(A))