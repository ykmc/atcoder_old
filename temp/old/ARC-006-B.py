N,L = map(int,input().split())
A = []
for i in range(L):
    A.append(input())
B = input()

S = [i for i in range(N)]
for i in range(L):
    for j in range(N-1):
        if A[i][j*2+1]=="-":
            S[j],S[j+1] = S[j+1],S[j]

for t in range(N):
    if B[t*2]=="o":
        break

print(S[t]+1)