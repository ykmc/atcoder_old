from itertools import permutations
N,M = map(int,input().split())
E = [[False for _ in range(N)] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    E[a-1][b-1] = True
    E[b-1][a-1] = True

P = permutations([i for i in range(1,N)])

ans = 0
for pp in P:
    l = len(pp)
    ni,mi = 0,0
    chk = True
    for p in pp:
        mi = p
        if not E[ni][mi]:
            chk = False
            break
        ni = p
    if chk:
        ans += 1

print(ans)


