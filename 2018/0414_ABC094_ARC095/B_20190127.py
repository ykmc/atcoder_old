N,M,X = map(int,input().split())
A = list(map(int,input().split()))

ans1,ans2 = 0,0
for i in range(X,N):
    if i in A:
        ans1 += 1
for i in range(X,-1,-1):
    if i in A:
        ans2 += 1
print(min(ans1,ans2))