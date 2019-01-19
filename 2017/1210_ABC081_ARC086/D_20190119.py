N = int(input())
A = list(map(int,input().split()))

Ans = []
maxA,minA,maxAi,minAi = A[0],A[0],0,0
for i in range(1,N):
    if A[i] > maxA:
        maxA = A[i]
        maxAi = i
    if A[i] < minA:
        minA = A[i]
        minAi = i

if abs(maxA) >= abs(minA):
    for i in range(N):
        if i != maxAi:
            Ans.append((maxAi,i))
    for i in range(N-1):
        Ans.append((i,i+1))
else:
    for i in range(N):
        if i != minAi:
            Ans.append((minAi,i))
    for i in range(N-1):
        Ans.append((N-1-i,N-1-i-1))

print(len(Ans))
for (x,y) in Ans:
    print(x+1,y+1)