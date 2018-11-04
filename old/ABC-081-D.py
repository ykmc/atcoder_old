N = int(input())
A = list(map(int,input().split()))

maxA,minA = max(A),min(A)
maxAi,minAi = -1,-1
sign = ""
M = []

for i in range(N):
    if A[i] == maxA:
        maxAi = i
        break
for i in range(N):
    if A[i] == minA:
        minAi = i
        break

if abs(maxA) >= abs(minA):
    A = list(map(lambda x: x+maxA, A))
    sign = "+"
else:
    A = list(map(lambda x: x+minA, A))
    sign = "-"

if sign == "+":
    for i in range(N):
        if i != maxAi:
            M.append((maxAi,i))
    M.append((maxAi,maxAi))
    for i in range(N-1):
        M.append((i,i+1))
elif sign == "-":
    for i in range(N):
        if i != minAi:
            M.append((minAi,i))
    M.append((minAi,minAi))
    for i in range(N-1):
        M.append((N-i-1,N-i-2))

L = len(M)
print(L)
for i in range(L):
    x,y = M[i]
    print(x+1,y+1)
