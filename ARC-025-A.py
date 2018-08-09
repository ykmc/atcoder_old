D = list(map(int,input().split()))
J = list(map(int,input().split()))

Ans = 0
for i in range(7):
    Ans += max(D[i],J[i])

print(Ans)