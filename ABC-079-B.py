N = int(input())
L = [0]*87
L[0],L[1] = 2,1
for i in range(2,87):
    L[i] = L[i-1] + L[i-2]
print(L[N])
