N,A,B = map(int,input().split())
t = 0
for i in range(N+1):
    s = 0
    for j in str(i):
        s += int(j)
    if A <= s and s <= B:
        t += i
print(t)