N = int(input())
CSF = [tuple(map(int,input().split())) for _ in range(N-1)]

Ans = []
for i in range(N):
    t = 0
    for j in range(i,N-1):
        (c,s,f) = CSF[j]
        if t <= s:
            t = s+c
        else:
            t = s+((t-s-1)//f+1)*f+c
    Ans.append(t)

for ans in Ans:
    print(ans)

