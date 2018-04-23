N = int(input())
A = list(map(int,input().split()))
odd,n4 = 0,0
for i in range(N):
    if A[i]%2 == 1:
        odd += 1
    else:
        if A[i]%4 == 0:
            n4 += 1
if odd+n4==N and odd-n4==1:
    print("Yes")
else:
    print("Yes" if n4 >= odd else "No")
