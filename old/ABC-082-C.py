from collections import Counter
N = int(input())
A = Counter(list(map(int,input().split()))).most_common()
S = 0
for i,c in A:
    if i == c:
        continue
    elif i > c:
        S += c
    else:
        S += c-i
print(S)
