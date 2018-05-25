N,M = map(int,input().split())
A,B,C,D,Ans = [],[],[],[],[]
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
for _ in range(M):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)
for i in range(N):
    d,t = 10**10,-1
    for j in range(M):
        if d > abs(A[i]-C[j])+abs(B[i]-D[j]):
            d = abs(A[i]-C[j])+abs(B[i]-D[j])
            t = j
    Ans.append(t)
for i in range(N):
    print(Ans[i]+1)
