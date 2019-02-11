C = [0]*4
for _ in range(3):
    a,b = map(int,input().split())
    C[a-1] += 1
    C[b-1] += 1

ans = "YES"
for c in C:
    if c==3:
        ans = "NO"
        break

print(ans)