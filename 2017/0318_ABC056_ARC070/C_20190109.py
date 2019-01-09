X = int(input())

S = 0
for i in range(1,1000000):
    S += i
    if S >= X:
        break

print(i)
