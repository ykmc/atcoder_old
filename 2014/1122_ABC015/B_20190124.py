N = int(input())
A = list(map(int,input().split()))

cnt,total = 0,0
for i in range(N):
    if A[i]>0:
        cnt += 1
        total += A[i]

from math import ceil
print(ceil(total/cnt))