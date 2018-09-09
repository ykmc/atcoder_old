N = int(input())
W = []
for i in range(N):
    W.append(input())

from collections import Counter
counter = Counter(W).most_common()

Ans = "Yes"
if counter[0][1]>1:
    Ans = "No"
else:
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            Ans = "No"

print(Ans) 
