import sys
N,M = map(int,input().split())
A,B = [],[]
for i in range(N):
    A.append(input())
for i in range(M):
    B.append(input())

for i in range(N-M+1):
    for j in range(N-M+1):
        ans = True
        for ii in range(M):
            for jj in range(M):
                if A[i+ii][j+jj] != B[ii][jj]: 
                    ans = False
        if ans:
            print("Yes")
            sys.exit()

print("No")