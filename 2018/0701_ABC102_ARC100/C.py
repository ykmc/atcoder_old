N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    A[i] -= i

A.sort()

Ans = 0
mi = len(A)//2 # 中央値のindex
for i in range(N):
    Ans += abs(A[i]-A[mi])

print(Ans)
