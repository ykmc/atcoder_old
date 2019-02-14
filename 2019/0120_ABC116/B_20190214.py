N = int(input())

s = set()
ans = 0
while N not in s:
    s.add(N)
    if N%2==0:
        N //= 2
    else:
        N = 3*N+1
    ans += 1

print(ans+1)