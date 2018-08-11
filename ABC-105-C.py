N = int(input())

A,S = [0]*32,[0]*32
A[0],A[1],S[0],S[1] = 1,-2,1,-2
for i in range(2,32):
    A[i] = A[i-1]*(-2)
    S[i] = S[i-2] + A[i]

X = ["0"]*32
t = 0
flg = True
while N != 0:
    if N > 0:
        for i in range(32):
            if S[i] >= N:
                break
    else:
        for i in range(32):
            if S[i] <= N:
                break
    X[i] = "1"
    N -= A[i]

print(int("".join(X)[::-1]))