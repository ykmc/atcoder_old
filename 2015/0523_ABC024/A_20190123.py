A,B,C,K = map(int,input().split())
S,T = map(int,input().split())

ans = A*S+B*T
if S+T >= K:
    ans -= (S+T)*C

print(ans)