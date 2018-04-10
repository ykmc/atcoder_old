N,H = map(int,input().split())
a,b = [0]*N,[0]*N
for i in range(N):
    a[i],b[i] = map(int,input().split()) 
ma = max(a)
count=0
for bi in sorted(b, reverse=True):
    if bi<ma:
        break
    count += 1
    H -= bi
    if H<=0:
        break
if H > 0:
    if H%ma == 0:
        count += H//ma
    else:
        count += H//ma +1
print(count)

