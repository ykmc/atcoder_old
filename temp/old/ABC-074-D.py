# TLE on python3
N = int(input())
A,B,Ans = [],[],0
for i in range(N):
    x = list(map(int,input().split()))
    A.append(x.copy()) #PyPy3, A.append(x[:])
    B.append(x.copy()) #PyPy3, B.append(x[:])

for k in range(N):
    for i in range(N):
        for j in range(N):
            B[i][j] = min(B[i][j],B[i][k]+ B[k][j])

if A!=B:
    print(-1)
else:
    for i in range(N):
        for j in range(i+1,N):
            exists = True
            for k in range(N):
                if k not in (i,j) and B[i][j]==B[i][k]+B[k][j]:
                    exists = False                    
            if exists:
                Ans += B[i][j]
    print(Ans)

