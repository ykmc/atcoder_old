N = int(input())
S = input()
Ans = 0
for i in range(N):
    s1 = set(list(S[0:i+1]))
    s2 = set(list(S[i+1:N]))
    Ans = max(Ans,len(s1&s2))
print(Ans)