N = int(input())
rN = int(N**.5)
Ans = N
for i in range(1,rN+1):
    q,r = N//i,N%i
    Ans = min(Ans,abs(i-q) + r)
print(Ans)