C = [[] for _ in range(3)]
for i in range(3):
    C[i] = list(map(int,input().split()))

dy1,dy2 = C[1][0]-C[0][0], C[2][0]-C[1][0]
dx1,dx2 = C[0][1]-C[0][0], C[0][2]-C[0][1]

Ans = "Yes"
for i in range(1,3):
    if C[1][i]-C[0][i] != dy1 or C[2][i]-C[1][i] != dy2:
        Ans = "No"
        break
    if C[i][1]-C[i][0] != dx1 or C[i][2]-C[i][1] != dx2:
        Ans = "No"
        break

print(Ans)
