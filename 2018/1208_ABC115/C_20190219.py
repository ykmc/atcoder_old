N,K = map(int,input().split())
H = [int(input()) for _ in range(N)]

H.sort()
ans = 10**10
for i in range(N-K+1):
    ans = min(ans, H[i-1+K]-H[i])

print(ans)