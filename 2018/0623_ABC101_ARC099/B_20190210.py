N = int(input())

S,N2 = 0,N
while N2 >= 1:
    S += N2%10
    N2 //= 10

print("Yes" if N%S==0 else "No")