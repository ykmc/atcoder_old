N = int(input())

S = str(N)
total = 0
for s in S:
    total += int(s)

print("Yes" if N%total==0 else "No")