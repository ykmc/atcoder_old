K,S = map(int,input().split())
Ans = 0
for x in range(K+1):
    for y in range(K+1):
        if x+y <= S and S-(x+y) <= K:
            Ans += 1
print(Ans)
