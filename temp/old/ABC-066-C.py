N = int(input())
A = list(map(int,input().split()))
if N%2==0:
    B = A[1::2][::-1]+A[0::2]
else:
    B = A[0::2][::-1]+A[1::2]
print(" ".join(map(str,B)))