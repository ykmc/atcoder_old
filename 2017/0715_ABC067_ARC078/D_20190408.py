N = int(input())
A = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    A[a-1].append(b-1)
    A[b-1].append(a-1)

B = [False]*N
visited = [True]*N

Fp,Sp = 0,0
Fi,Si = [0],[N-1]

while B != visited:
    # Fennec
    nextXi = []
    for i in Fi:
        if not B[i]:
            B[i] = True
            Fp += 1
            nextXi.extend(A[i])
    Fi = nextXi
    # Snuke
    nextXi = []
    for i in Si:
        if not B[i]:
            B[i] = True
            Sp += 1
            nextXi.extend(A[i])
    Si = nextXi

print("Fennec" if Fp>Sp else "Snuke")