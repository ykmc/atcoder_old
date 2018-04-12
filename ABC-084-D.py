N = 100001
A,B = [True]*N,[0]*N
A[0],A[1] = False,False
for i in range(2,N):
    if A[i]:
        for j in range(i*2,N,i):
            A[j] = False
c=0
for i in range(3,N):
    if A[i] and A[(i+1)//2]:
        c += 1
    B[i] = c
Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    print(B[r]-B[l-1])