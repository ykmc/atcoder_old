N = int(input())
W = input().split()
T = ["TAKAHASHIKUN","Takahashikun","takahashikun"]
W[N-1] = W[N-1][:-1]

Ans = 0
for w in W:
    if w in T:
        Ans += 1

print(Ans)