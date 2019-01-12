from itertools import accumulate
N,W = map(int,input().split())
V = [[] for _ in range(4)]
w0 = 0
for i in range(N):
    w,v = map(int,input().split())
    if i==0:
        V[0].append(v)
        w0 = w
    else:
        V[w - w0].append(v)

# 降順ソート
for i in range(4):
    V[i].sort(reverse=True)

# 累積和
S = [[] for _ in range(4)]
for i in range(4):
    S[i] = [0] + list(accumulate(V[i]))

# 全探索
ans = 0
for i0 in range(len(S[0])):
    for i1 in range(len(S[1])):
        for i2 in range(len(S[2])):
            for i3 in range(len(S[3])):
                if w0*i0 + (w0+1)*i1 + (w0+2)*i2 + (w0+3)*i3 <= W:
                    ans = max(ans, S[0][i0]+S[1][i1]+S[2][i2]+S[3][i3])

print(ans)
