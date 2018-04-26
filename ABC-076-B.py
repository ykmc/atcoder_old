N,K = int(input()),int(input())
Ans = 1
for i in range(N):
    if Ans < K:
        Ans *= 2
    else:
        Ans += K
print(Ans)