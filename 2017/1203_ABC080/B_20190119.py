N = input()

total = 0
for n in N:
    total += int(n)

print("Yes" if int(N)%total==0 else "No")
