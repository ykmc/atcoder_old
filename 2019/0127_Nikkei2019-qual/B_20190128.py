N = int(input())
A = input()
B = input()
C = input()

ans = 0
for i in range(N):
    if A[i]==B[i]==C[i]:
        continue
    elif A[i]==B[i] or B[i]==C[i] or C[i]==A[i]:
        ans += 1
    else:
        ans += 2

print(ans)