N,D,K = map(int,input().split())
LR = [tuple(map(int,input().split())) for _ in range(D)]
ST = [tuple(map(int,input().split())) for _ in range(K)]

ans = []
for (s,t) in ST:
    if s<t:
        for i in range(D):
            l,r = LR[i]
            if l<=s<=r:
                s = r
            if s>=t:
                ans.append(i+1)
                break
    else:
        for i in range(D):
            l,r = LR[i]
            if l<=s<=r:
                s = l
            if s<=t:
                ans.append(i+1)
                break

for a in ans:
    print(a)
