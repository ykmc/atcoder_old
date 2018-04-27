H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

M = [[0 for _ in range(W)] for _ in range(H)]
C = []
for i in range(len(A)):
    C += [str(i+1)]*A[i]

k = 0
for i in range(H):
    for j in range(W):
        if i%2==0:
            M[i][j] = C[k]
        else:
            M[i][W-1-j] = C[k]
        k += 1

for i in range(H):
    print(" ".join(M[i]))