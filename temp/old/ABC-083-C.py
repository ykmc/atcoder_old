X,Y = map(int,input().split())
A,L = X,0
while A <= Y:
    L += 1
    A *= 2
print(L)