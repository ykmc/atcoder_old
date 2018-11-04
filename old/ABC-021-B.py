from collections import Counter
N = int(input())
a,b = map(int,input().split())
K = int(input())
P = list(map(int,input().split()))
P.append(a)
P.append(b)
C = Counter(P).most_common()
print("YES" if C[0][1]==1 else "NO")