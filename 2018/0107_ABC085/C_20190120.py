N,Y = map(int,input().split())

import sys
for i in range(N+1):
    for j in range(N+1-i):
        k = N-(i+j)
        if k>=0 and 10000*i+5000*j+1000*k == Y:
            print(i,j,k)
            sys.exit()

print(-1,-1,-1)