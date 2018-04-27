N = int(input())
Ans = 0
for i in range(N):
    l,r = map(int,input().split())
    Ans += r-l+1
print(Ans)
