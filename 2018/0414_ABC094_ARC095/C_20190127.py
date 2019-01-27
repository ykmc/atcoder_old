N = int(input())
X = list(map(int,input().split()))

left  = sorted(X)[N//2-1]
right = sorted(X)[N//2]
for i in range(N):
    if X[i]<=left:
        print(right)
    else:
        print(left)