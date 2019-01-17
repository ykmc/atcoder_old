H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

B = [-1]*(H*W)
bi = 0
for i in range(N):
    for _ in range(A[i]):
        B[bi] = i+1
        bi += 1

Ans = []
for h in range(H):
    Ans.append(B[h*W:(h+1)*W])

for h in range(H):
    if h%2==0:
        print(" ".join(map(str,Ans[h])))
    else:
        Ans[h].reverse()
        print(" ".join(map(str,Ans[h])))