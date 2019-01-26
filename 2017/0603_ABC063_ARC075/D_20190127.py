N,A,B = map(int,input().split())
H = [int(input()) for _ in range(N)]

from math import ceil

ng,ok = 0,10**9+1
while abs(ok-ng)>1:
    mid = (ng+ok)//2
    cnt = 0
    for i in range(N):
        cnt += max(ceil((H[i] - B*mid)/(A-B)) ,0)
    if cnt <= mid:
        ok = mid
    else:
        ng = mid

print(ok)