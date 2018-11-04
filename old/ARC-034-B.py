N = int(input())

Ans = []
# 10**18 までなので、桁和の最大値は9*18 < 180
for i in range(180,0,-1):
    n = N-i
    if n<0:
        continue
    S = str(n)
    total = 0
    for s in S:
        total += int(s)
    if n+total == N:
        Ans.append(n)

print(len(Ans))
for ans in Ans:
    print(ans)
