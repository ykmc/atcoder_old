N = int(input())
S = []
for i in range(N):
    a,b,c,d,e = map(int,input().split())
    S.append(a+b+c+d+e*110/900)

print(max(S))