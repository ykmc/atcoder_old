N,C = map(int,input().split())
A = [[0 for _ in range(C)] for j in range(100001)]
for i in range(N):
    s,t,c = map(int,input().split())
    for j in range(s-1,t):
        A[j][c-1] = 1
R = 0
for i in range(100001):
    sumA = sum(A[i])
    if R < sumA:
        R = sumA
print(R)
