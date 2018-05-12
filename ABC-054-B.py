import sys
N,M = map(int,input().split())
A,B = [],[]
for i in range(N):
    A.append(input())
for i in range(M):
    B.append(input())
for i in range(N-M+1):
    for j in range(N-M+1):
        check = True
        for di in range(M):
            for dj in range(M):
                if A[i+di][j+dj] != B[di][dj]:
                    check = False
        if check:
            print("Yes")
            sys.exit()
else:
    print("No")
