N = int(input())
A = [0]+list(map(int,input().split()))+[0]

cost = 0
for i in range(N+1):
    cost += abs(A[i]-A[i+1])

for i in range(1,N+1):
    print(cost - abs(A[i-1]-A[i]) -abs(A[i]-A[i+1]) + abs(A[i-1]-A[i+1]))
