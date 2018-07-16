N = int(input())

P = []
t = 1
for i in range(N):
    t *= (N-i)/N
    P.append(t*(i+1)/N)

e = (N+1)/2
Ans = 0
for i in range(N):
    Ans += P[i]*e*(i+1)

print(Ans)