N = int(input())
Ans = 0
for _ in range(N):
    a,b = map(int,input().split())
    Ans += a*b
print(int(Ans*1.05))