A,B = map(int,input().split())
X = []
for i in range(100):
    if i<50:
        X.append(["."]*100)
    else:
        X.append(["#"]*100)

A = A-1
q,r = A//50, A%50
for i in range(q):
    for j in range(50):
        X[99-i*2][j*2] = "."
for i in range(r):
    X[51][i*2] = "."

B = B-1
q,r = B//50, B%50
for i in range(q):
    for j in range(50):
        X[i*2][j*2] = "#"
for i in range(r):
    X[48][i*2] = "#"

print(100,100)
for x in X:
    print("".join(x))
