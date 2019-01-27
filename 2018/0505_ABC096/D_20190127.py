N = int(input())

A = [True]*100000
A[0],A[1]=False,False
for i in range(2,100000):
    if A[i]:
        j = 2
        while i*j<100000:
            A[i*j] = False
            j += 1
P = []
for i in range(100000):
    if A[i] and i%5==1:
        P.append(i)

print(" ".join(map(str,P[:N])))