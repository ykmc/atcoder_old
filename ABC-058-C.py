from collections import Counter
N = int(input())
D = {chr(x+97):100 for x in range(26)}
for i in range(N):
    C = Counter(input())
    for j in range(26):
        x = chr(j+97)
        D[x] = min(D[x],C[x])
Ans = ""
for i in range(26):
    x = chr(i+97)
    Ans += x*D[x]
print(Ans)