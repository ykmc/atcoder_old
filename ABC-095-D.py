N,C = map(int,input().split())
X,V = [],[]
for i in range(N):
    x,v = map(int,input().split())
    X.append(x)
    V.append(v)
Xa,Xb = [X[0]]+[0]*(N-1),[0]*(N-1)+[C-X[N-1]]
for i in range(1,N):
    Xa[i] = X[i] - X[i-1]
for i in range(N-1):
    Xb[N-2-i] = X[N-1-i] - X[N-2-i]

Point1,Point2 = [],[]
point = 0
for i in range(N):
    point = point - Xa[i] + V[i]
    Point1.append(point)
point = 0
for i in range(N):
    point = point - Xb[N-1-i] + V[N-1-i]
    Point2.append(point)

#順方向に食べ続けていく場合に、何個目で過去最高を更新するか
N1,N2 = [],[]
if Point1[0] > Point1[1]:
    N1.append(0)
for i in range(1,N-1):
    if Point1[i+1] < Point1[i] and Point1[i-1] < Point1[i]:
        N1.append(i)
if Point1[N-1] == max(Point1):
    N1.append(N-1)
#逆方向に食べ続けていく場合に、何個目で過去最高を更新するか
if Point2[0] > Point2[1]:
    N2.append(0)
for i in range(1,N-1):
    if Point2[i+1] < Point2[i] and Point2[i-1] < Point2[i]:
        N2.append(i)
if Point2[N-1] == max(Point2):
    N2.append(N-1)

Ans = 0
#順方向に食べ、逆方向に最大限まで食べる
for i in N1:
    #順方向に食べて停止した時点のポイント
    point = Point1[i]
    Ans = max(Ans,point)
    #0まで戻るのに必要なポイント
    point -= X[i]
    #逆方向にどこまで食べられるか
    for j in N2:
        if j < N-1-i:
            point += Point2[j]
            Ans = max(Ans,point)

#逆方向に食べ、順方向に・・・
for i in N2:
    point = Point2[i]
    Ans = max(Ans,point)
    #0まで戻るのに必要なポイント
    point -= (C - X[N-1-i])
    for j in N1:
        #
        if j < N-1-i:
            point += Point1[j]
            Ans = max(Ans,point)

#出力
print(Ans)



    