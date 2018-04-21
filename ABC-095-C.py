A,B,C,X,Y = map(int,input().split())
Ans = 0
Z = min(X,Y)
if A+B >= C*2:
    Ans = min(C*Z*2 + A*(X-Z) + B*(Y-Z), C*max(X,Y)*2)
else:
    Ans = A*X + B*Y
print(Ans)
