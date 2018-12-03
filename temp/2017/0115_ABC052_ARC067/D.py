N,A,B = map(int,input().split())
X = list(map(int,input().split()))

Ans = 0
for i in range(1,N):
    if (X[i]-X[i-1])*A >= B:
        Ans += B
    else:
        Ans += (X[i]-X[i-1])*A

print(Ans)