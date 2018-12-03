A,B = map(int,input().split())
S = input()
X,Y,Z = S[:A],S[A],S[A+1:]
if ("-" not in X) and (A==len(X)) and (Y=="-") and ("-" not in Z) and (B==len(Z)):
    print("Yes")
else:
    print("No") 