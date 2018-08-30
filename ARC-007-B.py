N,M = map(int,input().split())
D = [i for i in range(N+1)]
nowD = 0
for i in range(M):
    nextD = int(input())
    for j in range(1,N+1):
        if D[j]==nextD:
            D[j] = nowD
            nowD = nextD
            break

for i in range(N):
    print(D[i+1])