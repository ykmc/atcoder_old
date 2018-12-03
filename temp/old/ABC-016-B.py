A,B,C = map(int,input().split())

n = 0
if A+B == C:
    n += 1
if A-B == C:
    n += 2

print(["!","+","-","?"][n])