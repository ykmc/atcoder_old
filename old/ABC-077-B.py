N = int(input())
while True:
    if N**.5 - int(N**.5) == 0:
        break
    N -= 1
print(N)