N = int(input())
T = list(map(int,input().split()))
V = list(map(int,input().split()))
v = [0]*(sum(T)*2+1)
t,Ti = 0,0
for i in range(N):
    Ti += T[i]*2
    v[t] = min(v[t],V[i])
    while t < Ti:
        if v[t] < V[i]:
            v[t+1] = v[t]+0.5
        else:
            v[t+1] = min(v[t],V[i])
        t += 1
sumT = sum(T)*2
v[sumT] = 0
t,Ti = sumT,sumT
for i in range(N):
    Ti -= T[N-i-1]*2
    while t > Ti:
        if v[t-1] > v[t]+0.5:
            v[t-1] = v[t]+0.5
        t -= 1
Ans = 0
for i in range(sumT):
    Ans += (v[i]+v[i+1])*0.5/2

print(Ans)