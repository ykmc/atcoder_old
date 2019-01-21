S = int(input())
A = set([])
while S not in A:
    A.add(S)
    if S%2==0:
        S //= 2
    else:
        S = S*3+1

print(len(A)+1)
