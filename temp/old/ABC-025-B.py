N,A,B = map(int,input().split())
Ans = 0
for i in range(N):
    s,d = input().split()
    d = int(d)
    sign = 1
    if s == "West":
        sign = -1
    if d < A:
        Ans += A*sign
    elif d > B:
        Ans += B*sign
    else:
        Ans += d*sign

if Ans == 0:
    print(0)
else:
    Dir = "East" if Ans > 0 else "West"
    print(Dir,abs(Ans))