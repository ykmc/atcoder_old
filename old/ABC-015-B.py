import math
N = int(input())
A = list(map(int,input().split()))
S = sum(a for a in A if a!=0)
lenS = len(A) - A.count(0)
print(math.ceil(S/lenS))