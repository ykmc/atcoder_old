A,B = map(int,input().split())

Ans = ""
if A==1:
    A=14
if B==1:
    B=14

if A==B:
    Ans = "Draw"
elif A>B:
    Ans = "Alice"
else:
    Ans = "Bob"

print(Ans)