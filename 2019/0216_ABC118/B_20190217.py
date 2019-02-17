N,M = map(int,input().split())
A = []
for i in range(N):
    KA = list(map(int,input().split()))
    A.append(KA[1:])

ans = A[0]
for i in range(1,N):
    t = []
    for a in A[i]:
        if a in ans:
            t.append(a)
    ans = t

print(len(ans))