N = int(input())
A,B = [],[]
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

C = []
for i in range(N):
    C.append((B[i]/A[i],i))
C.sort(reverse=True)

Ans = 0
d = 0
for i in range(N):
    c,j = C[i]
    Ans += d*B[j]
    d += A[j]

print(Ans)
