N,D = map(int,input().split())
X = list(map(int,input().split()))

# R[i] : 点iより右にD以内にある点の数
R = [0]*N
ri,cnt = 0,0
for li in range(N):
    while ri < N and X[ri] - X[li] <= D:
        cnt += 1
        ri += 1
    # 自分自身を除く
    R[li] = cnt-1
    cnt -= 1

# L[i] : 点iより左にD以内にある点の数
# 右から尺取りかくとバグりそうなので、リストを反転して尺取りし、結果を反転することで求める
L = [0]*N
revX = X[::-1]
ri,cnt = 0,0
for li in range(N):
    while ri < N and abs(revX[ri] - revX[li]) <= D:
        cnt += 1
        ri += 1
    # 自分自身を除く
    L[li] = cnt-1
    cnt -= 1
L = L[::-1]

# A : i<j<k の3点がD以内に含まれる場合の数を求める
# L : left(i) から2点選び、それぞれj,kとおけば条件を満たす
A = 0
for i in range(N):
    A += L[i]*(L[i]-1)//2

# B : i<j<k で Xj-Xi<=D, Xk-Xj<=Dの場合の数を求める
# 中点 j を固定して考えた時に
# 左点の候補は L : left(i)
# 右点の候補は R : right(i)
# なので単純に掛け合わせれば良い
# j は中点なので 1<j<N-1
B = 0
for j in range(1,N-1):
    B += L[j]*R[j]

# 求める答えは B-A
print(B-A)
