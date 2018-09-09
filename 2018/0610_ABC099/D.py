N,C = map(int,input().split())
D = []
for i in range(C):
    d = list(map(int,input().split()))
    D.append(d)
A = []
for i in range(N):
    a = list(map(int,input().split()))
    A.append(a)

X0,X1,X2 = [],[],[]
for i in range(N):
    for j in range(N):
        if (i+j)%3 == 0:
            X0.append(A[i][j])
        elif (i+j)%3 == 1:
            X1.append(A[i][j])
        else:
            X2.append(A[i][j])

# それぞれの集合を塗り替える場合のコストを計算
Xn = [X0,X1,X2]
cost = [[0 for _ in range(C)] for _ in range(3)]
for i in range(3):
    for c in range(1,C+1):
        Ans = 0
        for x in Xn[i]:
            if x != c:
                Ans += D[x-1][c-1]
        cost[i][c-1] = Ans

Y0 = cost[0]
Y1 = cost[1]
Y2 = cost[2]
Ans = 1000000000000000
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i != j and j != k and k != i:
                Ans = min(Ans, Y0[i]+Y1[j]+Y2[k])

print(Ans)
