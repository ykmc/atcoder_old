N,T = map(int,input().split())
A = []
for i in range(N):
    A.append(int(input()))
Ans = T
for i in range(N-1):
    Ans += min(T,A[i+1]-A[i])
print(Ans)