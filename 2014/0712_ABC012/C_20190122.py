N = int(input())
d = 45**2-N
for i in range(1,10):
    if d%i==0 and 1<=i<=9 and 1<=d//i<=9:
        print(i, "x", d//i)