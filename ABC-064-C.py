N = int(input())
A = list(map(int,input().split()))
S,red = set([]),0
for i in range(N):
    rank = A[i]//400
    if rank < 8:
        S.add(rank)
    else:
        red += 1
print(max(1,len(S)),len(S)+red)