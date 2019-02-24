N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

ans = 0
d = 1 << 32
for i in range(N):
    if abs((T - H[i]*0.006) - A) < d:
        d = abs((T - H[i]*0.006) - A)
        ans = i

print(ans+1)