N,Q = map(int,input().split())
A = [0]*(N+1)
for i in range(Q):
    L,R,T = map(int,input().split())
    A[L:R+1] = [T]*(R-L+1)
for i in range(1,N+1):
    print(A[i])