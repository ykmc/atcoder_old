N,Q = map(int,input().split())
A = list(map(int,input().split()))
X = []
for i in range(Q):
    X.append(int(input()))

# 高橋君が右から最大とれる数
max_cnt = (N+1)//2
# 配列
taka = [0]*max_cnt
for i in range(1,max_cnt):
    # この値より
    taka[i] = (A[N-1-i] + A[N-1-i*2])/2

# 右からの累積和
S = [0]*N
S[N-1] = A[N-1]
for i in range(1,N):
    S[N-1-i] = S[N-i]+ A[N-1-i]
T = [0]*N
if N%2==0:
    T[0]=A[1]
    T[1]=A[1]
    for i in range(1,N//2):
        T[i*2] = T[i*2-1] + A[i*2]
        T[i*2+1] = T[i*2-1] + A[i*2]
else:
    T[0]=A[0]
    T[1]=A[0]
    for i in range(1,N//2):
        T[i*2] = T[i*2-1] + A[i*2+1]
        T[i*2+1] = T[i*2-1] + A[i*2+1]


for i in range(Q):
    getr = 0
    for j in range(1,len(taka)):
        if X[i] > taka[j]:
            getr = j
            break
    if getr==0:
        print(S[N-max_cnt])
    else:
        print(S[N-j],T[N-1-j*2])
