from collections import defaultdict
N = int(input())

F = [True]*(N+1)
F[0]=F[1]=False
P = []

for i in range(2,N+1):
    if F[i]==True:
        P.append(i)
        for j in range(i*2,N+1,i):
            F[j]=False

dic = defaultdict(int)
for i in range(2,N+1):
    for p in P:
        while i%p==0:
            dic[p] += 1
            i = i//p
        if i==1:
            break

ans = 1
modulo = 10**9+7
for v in dic.values():
    ans *= (v+1)
    ans %= modulo

print(ans)