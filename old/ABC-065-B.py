N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

Ans = -1
j = 0
for i in range(N):
    if A[j] == 2:
        Ans = i+1
        break
    else:
        j = A[j]-1

print(Ans)