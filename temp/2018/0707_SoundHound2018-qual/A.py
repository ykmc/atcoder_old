A,B = map(int,input().split())

Ans = ""
if A+B == 15:
    Ans = "+"
elif A*B == 15:
    Ans = "*"
else:
    Ans = "x"

print(Ans)