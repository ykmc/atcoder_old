N,M = map(int,input().split())

if N*2 >= M:
    print(min(N,M//2))
else:
    print(N + (M-N*2)//4)