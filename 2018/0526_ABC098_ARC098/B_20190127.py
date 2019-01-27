N = int(input())
S = input()

ans = 0
for i in range(N):
    s1 = set(list(S[:i+1]))
    s2 = set(list(S[i+1:]))
    ans = max(ans,len(s1&s2))

print(ans)