N = int(input())
A = list(map(int,input().split()))

ans = 0
xor = 0
l,r = 0,0

while r < N:
    if xor^A[r] == xor+A[r]:
        ans += r-l+1
        xor ^= A[r]
    else:
        while xor^A[r] != xor+A[r]:
            xor ^= A[l]
            l += 1
        xor ^= A[r]
        ans += r-l+1
    r += 1

print(ans)