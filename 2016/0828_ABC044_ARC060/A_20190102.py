N = int(input())
K = int(input())
X = int(input())
Y = int(input())

print(X*min(N,K)+Y*max(0,N-K))