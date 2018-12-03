L,H = map(int,input().split())
N = int(input())

A = []
for i in range(N):
    A.append(int(input()))

for i in range(N):
    if L <= A[i] <= H:
        print(0)
    elif A[i] > H:
        print(-1)
    elif A[i] < L:
        print(L-A[i])