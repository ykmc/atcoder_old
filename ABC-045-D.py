from collections import Counter
H,W,N = map(int,input().split())
Bs = []
for i in range(N):
    x,y = map(int,input().split())
    for xx in range(3):
        for yy in range(3):
            tx,ty = x-xx,y-yy
            if 1<=tx and tx<=H-2 and 1<=ty and ty<=W-2:
                Bs.append((tx,ty))
C = [0]*10
for (x,y),v in Counter(Bs).most_common():
    C[v] += 1
C[0] = (H-2)*(W-2)-sum(C)
for i in range(10):
    print(C[i])
    