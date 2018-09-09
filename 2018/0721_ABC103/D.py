N,M = map(int,input().split())
AB = []
for i in range(M):
    a,b = map(int,input().split())
    AB.append((a,b))

AB.sort()

Ans = 0
l,r = 1,N
for ab in AB:
    a,b = ab
    if r <= a:
        Ans += 1
        l,r = a,b
    else:
        l = max(l,a)
        r = min(r,b)
else:
    Ans += 1

print(Ans)