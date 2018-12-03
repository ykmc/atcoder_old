Ans = 0
for _ in range(3):
    s,e = map(int,input().split())
    Ans += s*e//10
print(Ans)
