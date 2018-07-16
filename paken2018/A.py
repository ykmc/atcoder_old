C1,A = input().split()
C2,B = input().split()

A,B = int(A),int(B)

if C1=="W":
    A = -A
if C2=="W":
    B = -B

print(abs(A-B)//15)
