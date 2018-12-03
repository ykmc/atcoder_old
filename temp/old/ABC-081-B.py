N = int(input())
A = list(map(int,input().split()))
c = 0
while 1:
    if list(map(lambda x: x%2, A)) == [0 for _ in range(N)]:
        A = list(map(lambda x: x//2, A))
        c += 1
    else:
        break
print(c)