N,K = map(int,input().split())
AB = []
for i in range(N):
    a,b = map(int,input().split())
    AB.append((a,b))

AB.sort()

cnt = 0
for ab in AB:
    a,b = ab
    cnt += b
    if cnt >= K:
        print(a)
        break
