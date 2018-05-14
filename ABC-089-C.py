from collections import Counter
N = int(input())
S = []
for i in range(N):
    s = input()
    if s[0] in ["M","A","R","C","H"]:
        S.append(s[0])
C = Counter(S).most_common()
lenC = len(C)
Ans = 0
for i in range(lenC):
    for j in range(i+1,lenC):
        for k in range(j+1,lenC):
            Ans += C[i][1]*C[j][1]*C[k][1]
print(Ans)
