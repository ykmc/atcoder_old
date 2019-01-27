A,B,C,X,Y = map(int,input().split())
Ans = 0
Z = min(X,Y)
if A+B < C*2:
    Ans = A*X+B*Y
else:
    Ans = min(C*2*Z + A*(X-Z) + B*(Y-Z), C*2*max(X,Y))

print(Ans)