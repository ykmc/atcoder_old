A,B = map(int,input().split())

Ans = 0
while abs(B-A)>=10:
    Ans += 1
    if A > B:
        A -= 10
    else:
        A += 10

D = [0,1,2,3,2,1,2,3,3,2]

print(Ans+D[abs(B-A)])

