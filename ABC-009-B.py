from collections import Counter
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
C = Counter(A).most_common()
C.sort(reverse=True)
print(C[1][0])