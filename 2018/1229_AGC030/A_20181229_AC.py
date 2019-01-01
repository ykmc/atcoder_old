A,B,C = map(int,input().split())

if A+B < C:
    print(min(A+B,C)+B+1)
else:
    print(B+C)