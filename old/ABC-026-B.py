import math

N = int(input())
R = []
for i in range(N):
    R.append(int(input()))

R.sort(reverse=True)
Ans = 0
for i in range(N):
    if i%2==0:
        Ans += R[i]**2
    else:
        Ans -= R[i]**2

print(Ans*math.pi)

