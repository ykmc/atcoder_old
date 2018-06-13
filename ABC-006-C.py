N,M = map(int,input().split())

d = M - N*3
if d == 0:
    print(0,N,0)
elif -N <= d < 0:
    print(-d,N+d,0)
elif 0 < d <= N:
    print(0,N-d,d)
else:
    print(-1,-1,-1)