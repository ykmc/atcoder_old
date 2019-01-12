N,M = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
modulo = 10**9+7

x,y = 0,0
for i in range(N):
    x += X[i]*i - X[i]*(N-i-1)
for i in range(M):
    y += Y[i]*i - Y[i]*(M-i-1)

print(x*y%modulo)