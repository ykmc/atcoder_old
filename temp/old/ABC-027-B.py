N = int(input())
A = list(map(int,input().split()))

if sum(A)%N != 0:
    print(-1)
else:
    Ans = 0
    total,cnt = 0,0
    avg = sum(A)/N
    for i in range(N):
        total += A[i]
        cnt += 1
        if total/cnt == avg:
            continue
        Ans += 1
    print(Ans)