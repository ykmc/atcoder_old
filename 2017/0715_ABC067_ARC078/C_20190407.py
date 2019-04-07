N = int(input())
A = list(map(int,input().split()))

p1 = 0
p2 = sum(A)
diff = 9999999999999999
for i in range(N-1):
    p1 += A[i]
    p2 -= A[i]
    diff = min(diff, abs(p1-p2))

print(diff)