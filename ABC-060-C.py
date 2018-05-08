N,T = map(int,input().split())
A = list(map(int,input().split()))
Ans = 0
for i in range(1,N):
    if A[i] > A[i-1]+T:
        Ans += T
    else:
        Ans += A[i] - A[i-1]
else:
    Ans += T
print(Ans)