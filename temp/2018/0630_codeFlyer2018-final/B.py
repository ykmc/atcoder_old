from bisect import bisect_left
from bisect import bisect_right

N,Q = map(int,input().split())
X = list(map(int,input().split()))
C,D = [],[]
for i in range(Q):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)

S = [0]*(N+1)
for i in range(N):
    S[i+1] = S[i]+X[i]

for i in range(Q):
    ans = 0
    l = bisect_left(X,C[i]-D[i])
    m = bisect_left(X,C[i])
    r = bisect_right(X,C[i]+D[i])
    ans += (m-l)*C[i] - (S[m]-S[l])
    ans += -((r-m)*C[i] - (S[r]-S[m]))
    ans += (N-(r-l))*D[i]
    print(ans)