S = input()
Q = int(input())
A = list(map(int,input().split()))
B,X = [],[]
for i in range(Q):
    b,x = map(int,input().split())
    B.append(b)
    X.append(x)
MOD = 10**9+7

pos = []
lenS = len(S)
ai = 0
repS = ""
for i in range(lenS):
    if S[i] == "a":
        repS += str(A[ai])
        ai += 1
        pos.append(i)
    else:
        repS += S[i]

for i in range(Q):
    t = pos[B[i]-1]
    print(eval(repS[0:t] + str(X[i]) + repS[t+1:]) % MOD)

# evalでは処理しきれないっぽい
# DFSで計算処理をかけば間に合う？