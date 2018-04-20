from collections import Counter
N = int(input())
A = Counter(list(map(int,input().split())))
Ans = 0
for n,c in A.most_common():
    Ans = max(Ans,A[n]+A[n-1]+A[n+1])
print(Ans)