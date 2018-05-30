from collections import Counter
N = int(input())
A = [int(input()) for _ in range(N)]

C = Counter(A).most_common()
Ans = 0
for c in C:
    i,cnt = c
    Ans += cnt-1
print(Ans)