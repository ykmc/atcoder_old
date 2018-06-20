x,y = map(int,input().split())

A = [1,3,5,7,8,10,12]
B = [4,6,9,11]

print("Yes" if (x in A and y in A) or (x in B and y in B) else "No")