N,M = map(int,input().split())
Ans = [0]*N
for i in range(M):
    a,b = map(int,input().split())
    Ans[a-1] += 1
    Ans[b-1] += 1

for i in range(N):
    print(Ans[i])