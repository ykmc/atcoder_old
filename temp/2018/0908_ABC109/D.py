H,W = map(int,input().split())
A = []*H
for i in range(H):
    A.append(list(map(int,input().split())))

for h in range(H):
    for w in range(W):
        A[h][w] %= 2


Ans = []
for h in range(H):
    if h%2==0:
        for w in range(W-1):
            if A[h][w]==1:
                Ans.append([h+1,w+1,h+1,w+2])
                A[h][w+1] += 1
        if A[h][W-1]==1 and h+1!=H:
            Ans.append([h+1,W,h+2,W])
            A[h+1][W-1] += 1
    else:
        for w in range(W-1):
            wt = W-1-w
            if A[h][wt]==1:
                Ans.append([h+1,wt+1,h+1,wt])
                A[h][wt-1] += 1
        if A[h][0]==1 and h+1!=H:
            Ans.append([h+1,1,h+2,1])
            A[h+1][0] += 1

print(len(Ans))
for ans in Ans:
    print(" ".join(map(str,ans)))
