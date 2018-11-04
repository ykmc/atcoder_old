from itertools import accumulate
N,W = map(int,input().split())

w0,v0 = map(int,input().split())
W0,W1,W2,W3 = [],[],[],[]
W0.append(v0)
for i in range(1,N):
    w,v = map(int,input().split())
    if w == w0:
        W0.append(v)
    elif w == w0+1:
        W1.append(v)
    elif w == w0+2:
        W2.append(v)
    else:
        W3.append(v)

W0.sort(reverse=True)
W1.sort(reverse=True)
W2.sort(reverse=True)
W3.sort(reverse=True)
V0 = [0]+list(accumulate(W0))
V1 = [0]+list(accumulate(W1))
V2 = [0]+list(accumulate(W2))
V3 = [0]+list(accumulate(W3))

Ans = 0
for i0 in range(len(V0)):
    for i1 in range(len(V1)):
        for i2 in range(len(V2)):
            for i3 in range(len(V3)):
                if w0*i0 + (w0+1)*i1 + (w0+2)*i2 + (w0+3)*i3 <= W:
                    Ans = max(Ans,V0[i0]+V1[i1]+V2[i2]+V3[i3])

print(Ans)