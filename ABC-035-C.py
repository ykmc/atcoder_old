N,Q = map(int,input().split())

# 1-indexedのため+1, 最後の要素選択時の余白で+1
A = [0]*(N+2)
for i in range(Q):
    l,r = map(int,input().split())
    A[l] += 1
    A[r+1] -= 1

# 累積和しつつ偶奇判定
for i in range(1,N+2):
    A[i] = (A[i] + A[i-1]) % 2

print("".join(map(str,A[1:N+1])))