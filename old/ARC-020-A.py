A,B = map(int,input().split())

Ans = "Ant"

if abs(A)==abs(B):
    Ans = "Draw"
elif abs(A)>abs(B):
    Ans = "Bug"

print(Ans)