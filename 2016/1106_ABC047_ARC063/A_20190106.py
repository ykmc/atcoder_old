C = list(map(int,input().split()))
C.sort()
print("Yes" if C[0]+C[1]==C[2] else "No")