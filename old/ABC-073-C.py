from collections import Counter
N = int(input())
A,Ans = [],0
for i in range(N):
    A.append(int(input()))
cA = Counter(A).most_common()
for k,v in cA:
    if v%2 != 0:
        Ans += 1
print(Ans)