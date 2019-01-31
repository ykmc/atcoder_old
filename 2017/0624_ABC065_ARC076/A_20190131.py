X,A,B = map(int,input().split())

Ans = "dangerous"
if A-B>=0:
    Ans = "delicious"
elif B-A <= X:
    Ans = "safe"

print(Ans)