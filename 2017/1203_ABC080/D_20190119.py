N,C = map(int,input().split())
STC = [[] for _ in range(C)]
for i in range(N):
    s,t,c = map(int,input().split())
    STC[c-1].append((s,t))

lenA = 200001
A = [[0]*lenA for _ in range(C)]
for i in range(C):
    for (s,t) in STC[i]:
        # pythonで累積和はこうやれば早いのか！
        A[i][s*2-1:t*2] = [1]*(t*2-s*2+1)

Ans = [0]*lenA
for i in range(C):
    for j in range(lenA):
        if A[i][j] > 0:
            Ans[j] += 1

print(max(Ans))
