N = int(input())
AB = [tuple(map(int,input().split())) for _ in range(N)]

X = []
for (a,b) in AB:
    X.append((a+b,b))

X.sort(reverse=True)
pa,pb = 0,0
for i in range(N):
    ab,b = X[i]
    pb += b
    if i%2==0:
        pa += ab

print(pa-pb)