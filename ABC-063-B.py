from collections import Counter
S = input()
C = Counter(S).most_common(1)
print("yes" if C[0][1]==1 else "no")