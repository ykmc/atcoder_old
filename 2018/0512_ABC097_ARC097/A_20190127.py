A,B,C,D = map(int,input().split())
print("Yes" if abs(A-C)<=D or abs(A-B)<=D and abs(B-C)<=D else "No")