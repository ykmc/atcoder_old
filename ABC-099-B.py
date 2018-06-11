a,b = map(int,input().split())
d = b-a
total = 0
for i in range(1,d+1):
    total += i

print(total - b)
