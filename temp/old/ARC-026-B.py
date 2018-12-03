from math import ceil
N = int(input())

M = ceil(N**.5)
A = []
for i in range(1,M+1):
    if N/i == N//i:
        if i not in A:
            A.append(i)
        if N//i not in A:
            A.append(N//i)

sumA = sum(A)
N2 = N*2
Ans = ""
if sumA==N2:
    Ans = "Perfect"
elif sumA > N2:
    Ans = "Abundant"
else:
    Ans = "Deficient"

print(Ans)