N = int(input())
M = list(map(int,input().split()))

Ans = 0
for m in M:
    Ans += max(80-m,0)

print(Ans)