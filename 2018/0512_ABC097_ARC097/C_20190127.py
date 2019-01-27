S = input()
K = int(input())

Ans = []
for k in range(5):
    for i in range(len(S)-k):
        s = S[i:i+k+1]
        if s not in Ans:
            Ans.append(s)

Ans.sort()
print(Ans[K-1])