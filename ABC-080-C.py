N = int(input())

F,P,b,T = [],[],1,-9999999999

for i in range(N):
    F.append(list(map(int,input().split())))
for i in range(N):
    P.append(list(map(int,input().split())))

while b < 1 << 10:
    bs = "{0:10b}".format(b)
    bsi = 0
    S = [0]*N
    for c in bs:
        if c == "1":
            for i in range(N):
                S[i] += F[i][bsi]
        bsi += 1
    t = 0
    for i in range(N):
        t += P[i][S[i]]
    if T < t:
        T = t
    b += 1
print(T)

