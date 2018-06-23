N,K = map(int,input().split())
A = list(map(int,input().split()))
N2 = N-K
d = K-1
print((N2-1)//d +2)