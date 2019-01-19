N = int(input())
F = ["".join(input().split()) for _ in range(N)]
P = [list(map(int,input().split())) for _ in range(N)]

Ans = -9999999999
for i in range(1 << 10):
    xx = bin(i)[2::].zfill(10)
    if xx == "0000000000":
        continue
    
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(10):
            if xx[j]=="1" and F[i][j]=="1":
                cnt += 1
        ans += P[i][cnt]

    Ans = max(Ans,ans)

print(Ans)

