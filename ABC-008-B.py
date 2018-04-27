from collections import Counter
N = int(input())
S = [input() for _ in range(N)]
C = Counter(S).most_common(1)
print(C[0][0])