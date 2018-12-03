H,W,Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
PQ = []
for i in range(Q):
    PQ.append(map(int,input().split()))

x1,x2,y1,y2 = [0],[0],[0],[0]
for i in range(W):
    if i%2==0:
        x1.append(x1[i]+B[i])
        x2.append(x2[i])
    else:
        x1.append(x1[i])
        x2.append(x2[i]+B[i])
for i in range(H):
    if i%2==0:
        y1.append(y1[i]+A[i])
        y2.append(y2[i])
    else:
        y1.append(y1[i])
        y2.append(y2[i]+A[i])

# 座標の指定がxy逆なことに注意
def calc(y,x):
    Sb = x1[x]*y1[y] + x2[x]*y2[y]
    Sw = x1[x]*y2[y] + x2[x]*y1[y]
    return Sb-Sw

for pq in PQ:
    px,py,qx,qy = pq
    px,py = px-1,py-1
    print(calc(qx,qy)-calc(px,qy)-calc(qx,py)+calc(px,py))
