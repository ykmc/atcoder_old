N,T = map(int,input().split())
A = list(map(int,input().split()))
minP,prof,pc = 10**9+1,0.5,0
for i in range(N):
    minP = min(minP,A[i])
    d = A[i]-minP
    if d > prof:
        prof = d
        pc = 1
    elif d == prof:
        pc += 1
print(pc)