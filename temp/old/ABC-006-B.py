n = int(input())
a1,a2,a3 = 0,0,1
if n>3:
    for i in range(3,n):
        a1,a2,a3 = a2,a3,(a1+a2+a3)%10007
    print(a3)
elif n==3:
    print(1)
else:
    print(0)