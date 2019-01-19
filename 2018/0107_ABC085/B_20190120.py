N = int(input())
D = [int(input()) for _ in range(N)]
from collections import Counter
C = list(Counter(D).most_common())
print(len(C))