from collections import Counter
N = int(input())
A = list(map(int,input().split()))
C = Counter(A).items()
M = len(C)
print(M if (N-M)%2==0 else M-1)

