S,C = map(int,input().split())

ans = min(S,C//2)
if C >= S*2:
    C = C - S*2
    ans += C//4

print(ans)

