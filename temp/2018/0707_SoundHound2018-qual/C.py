N,M,D = map(int,input().split())

Ans = 0
if D==0:
    Ans = (M-1)/N
else:
    Ans = 2*(M-1)*(N-D)/(N**2)

print(Ans)