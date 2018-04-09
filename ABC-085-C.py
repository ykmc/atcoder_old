import sys
N,Y = map(int,input().split())
for i in range(N+1):
    for j in range(N-i+1):
        if i*10000 + j*5000 + (N-(i+j))*1000 == Y:
            print(i,j,N-(i+j))
            sys.exit()
print(-1,-1,-1)