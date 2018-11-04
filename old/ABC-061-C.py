N,K = map(int,input().split())
Z = []
for i in range(N):
    a,b = map(int,input().split())
    Z.append((a,b))
Z = sorted(Z)
for a,b in Z:
    K -= b
    if K <= 0:
        print(a)
        break