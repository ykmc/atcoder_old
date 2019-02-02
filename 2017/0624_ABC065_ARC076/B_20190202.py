N = int(input())
A = [int(input()) for _ in range(N)]

ans = -1
p = 0
for i in range(N):
    if A[p]==2:
        ans = i+1
        break
    else:
        p = A[p]-1

print(ans)


