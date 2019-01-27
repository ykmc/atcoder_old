X = int(input())
A = [False]*1001
A[1] = True
for i in range(2,1001):
    j = 2
    while i**j < 1001:
        A[i**j] = True
        j += 1

ans = 1
for i in range(X,-1,-1):
    if A[i]:
        ans = i
        break

print(ans)