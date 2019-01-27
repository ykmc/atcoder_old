N = int(input())
A = [0] + list(map(int,input().split())) + [0]

total = 0
for i in range(N+1):
    total += abs(A[i+1]-A[i])

for i in range(N):
    print(total - abs(A[i+1]-A[i]) - abs(A[i+2]-A[i+1]) + abs(A[i+2]-A[i]))