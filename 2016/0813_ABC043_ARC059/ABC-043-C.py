N = int(input())
A = list(map(int,input().split()))
S = 100000000
for i in range(-100,101):
    T = 0
    for j in range(N):
        T += (A[j] - i)**2
    if S > T:
        S = T
print(S)