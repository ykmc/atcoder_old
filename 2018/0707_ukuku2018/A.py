T = int(input())
X = []
for i in range(T):
    X.append(int(input()))

# とりあえずフィボナッチ数列を求める
fn = 100
F = [0]*fn
F[0],F[1] = 1,1
for i in range(2,fn):
    F[i] = F[i-1]+F[i-2]

# 対応する項差的なものを求める
D = [0]*fn
for i in range(1,fn):
    D[i] = F[i-1]

# 与えられた整数からF[i]を引いて、D[i]で割り切れればOK
# a=1,b=その時の商
for i in range(T):
    x = X[i]
    B = []
    for j in range(1,fn):
        if (x - F[j])%D[j]==0:
            # フィボナッチ数列と一致する場合に0になるので1との最小値を取る
            B.append(max((x - F[j])//D[j]+1,1))
    print(1,min(B))
