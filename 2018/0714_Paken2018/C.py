N,P = map(int,input().split())
A = list(map(int,input().split()))

Ans = ":("
li,ri = 0,0
t = 1

for li in range(N):
    while ri < N and t*A[ri] <= P:
        t *= A[ri]
        ri += 1
        if t==P:
            print("Yay!")
            exit()
    t //= A[li]

print(":(")