L,R = map(int,input().split())
l = sorted(map(int,input().split()))
r = sorted(map(int,input().split()))

Ans = 0
for i in range(10,41):
    Ans += min(l.count(i),r.count(i))

print(Ans)