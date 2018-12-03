N,K = map(int,input().split())
W,P = [],[]
for i in range(N):
    w,p = map(int,input().split())
    W.append(w)
    P.append(p)

def check(per):
    salt,water,A = 0,0,[]
    # 目標に不足する食塩の量, 水, 濃度 のリストを作る
    for i in range(N):
        A.append([W[i]*(per - P[i]*0.01), W[i], P[i]])
    for d,w,p in sorted(A)[:K]:
        salt  += w*p*0.01
        water += w
    return salt/water >= per

# 可能な濃度を二分探索で絞り込む
high,low = 1,0
for i in range(1000):
    mid = (high+low)/2
    if check(mid):
        low = mid
    else:
        high = mid

print(low*100)