N,M = map(int,input().split())
A,B,C,D = [],[],[],[]
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
for i in range(M):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)

Ans = []
for i in range(N):
    d = 10**9
    for j in range(M):
        if d > abs(A[i]-C[j])+abs(B[i]-D[j]):
            d = abs(A[i]-C[j])+abs(B[i]-D[j])
            ans = j
    Ans.append(ans)

# 0-indexedなので出力時に+1
for ans in Ans:
    print(ans+1)