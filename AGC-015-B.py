S = input()
N = len(S)
Ans = 0
for i in range(N):
    if S[i]=="U":
        Ans += (N-i-1) + 2*i
    else:
        Ans += 2*(N-i-1) + i
print(Ans)
