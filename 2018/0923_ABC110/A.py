A,B,C = map(int,input().split())
X = [A,B,C]
X.sort(reverse=True)

print(X[0]*10+X[1]+X[2])