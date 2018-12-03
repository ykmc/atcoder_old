N,M,A,B = map(int,input().split())

for i in range(M):
    c = int(input())
    if N <= A:
        N += B
    if N-c >=0:
        N -= c
    else:
        i += 1
        break
else:
    i = "complete"

print(i)
