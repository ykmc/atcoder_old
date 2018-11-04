N,Z,W = map(int,input().split())
A = list(map(int,input().split()))
if N == 1:
    print(abs(A[0]-W))
else:
    print(max(abs(A[N-1]-W),abs(A[N-1]-A[N-2])))