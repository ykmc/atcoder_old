S = input()
L = len(S)
A = len(S)
for i in range(1,L):
    if S[i] != S[i-1] and A > max(i,L-i):
        A = max(i,L-i)
print(A)