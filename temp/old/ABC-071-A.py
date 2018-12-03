X,A,B = map(int,input().split())
print("A" if abs(A-X) < abs(B-X) else "B")