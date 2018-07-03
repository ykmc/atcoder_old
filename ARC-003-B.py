N = int(input())
S = []
for i in range(N):
    S.append(input()[::-1])

S.sort()

for i in range(N):
    print(S[i][::-1])
