N,K = map(int,input().split())
T = [int(input()) for _ in range(N)] 

Ans = -1
S = T[0]+T[1]+T[2]
if S < K:
    Ans = 3
else:
    for i in range(N-3):
        S = S+T[i+3]-T[i]
        if S < K:
            Ans = i+4
            break

print(Ans)
