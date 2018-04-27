A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
if S+T >= K:
    print(A*S + B*T - (S+T)*C)
else:
    print(A*S + B*T)