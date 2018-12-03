N,S,T = map(int,input().split())
W = int(input())
Ans = 1 if S<=W and W<=T else 0

for i in range(N-1):
    W += int(input())
    if S<=W and W<=T:
        Ans += 1

print(Ans)