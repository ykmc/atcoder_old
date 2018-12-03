A,B,C,D = map(int,input().split())
L,R,S = A+B,C+D,"Balanced"
if L>R:
    S = "Left"
elif L<R:
    S = "Right"
print(S)
