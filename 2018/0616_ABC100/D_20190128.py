N,M = map(int,input().split())
XYZ = [tuple(map(int,input().split())) for _ in range(N)]

Ans = 0
for xs in [1,-1]:
    for ys in [1,-1]:
        for zs in [1,-1]:
            A = []
            for (x,y,z) in XYZ:
                A.append(x*xs + y*ys + z*zs)
            A.sort(reverse=True)
            ans = 0
            for i in range(M):
                ans += A[i]
            Ans = max(Ans,ans)

print(Ans)
