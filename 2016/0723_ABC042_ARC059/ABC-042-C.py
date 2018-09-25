N,K = map(int,input().split())
D = set(input().split())
while True:
    if not set(str(N)) & D:
        break
    N += 1
print(N)