N = int(input())
XU = [tuple(input().split()) for _ in range(N)]

ans = 0
for (x,u) in XU:
    if u=="JPY":
        ans += int(x)
    else:
        ans += float(x)*380000

print(ans)
