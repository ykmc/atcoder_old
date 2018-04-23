N,M = map(int,input().split())
A,B,C,D = [],[],[],[]
for i in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
for i in range(M):
    if A[i] == 1:
        C.append(B[i])
    if B[i] == N:
        D.append(A[i])
print("POSSIBLE" if len(set(C) & set(D)) > 0 else "IMPOSSIBLE")