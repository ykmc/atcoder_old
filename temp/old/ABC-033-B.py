N = int(input())
SP = list()
for i in range(N):
    s,p = input().split()
    p = int(p)
    SP.append((s,p))

SP.sort(key = lambda x:x[1], reverse=True)

total = 0
for i in range(N):
    total += SP[i][1]

print(SP[0][0] if SP[0][1] > total/2 else "atcoder")