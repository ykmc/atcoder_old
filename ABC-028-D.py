N,K = map(int,input().split())

K1 = (K-1)*(N-K)*6
K2 = (N-1)*3
K3 = 1
print((K1+K2+K3)/(N**3))