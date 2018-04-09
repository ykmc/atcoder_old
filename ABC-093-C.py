A,B,C = map(int,input().split())
dif = max(A,B,C)*3 - (A+B+C)
if dif%2 == 0:
    print(dif//2)
else:
    print(dif//2+2)