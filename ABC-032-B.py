S = input()
K = int(input())

Ans = set()
if len(S) >= K:
    for i in range(len(S)-K+1):
        Ans.add(S[i:i+K])

print(len(Ans))