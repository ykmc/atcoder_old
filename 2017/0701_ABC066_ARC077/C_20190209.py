N = int(input())
A = list(map(int,input().split()))

if N%2==0:
    ans1 = A[1::2][::-1]
    ans2 = A[0::2]
else:
    ans1 = A[0::2][::-1]
    ans2 = A[1::2]

print(" ".join(map(str,ans1))," ".join(map(str,ans2)))