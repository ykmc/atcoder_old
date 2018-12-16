N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)

ans1, ans2 = 0,0

maxA = max(A)
B = [1]
t = 1
while t < maxA:
    t *= 2
    B.append(t)

d = dict()
for i in range(N):
    if A[i] in d:
        d[A[i]] += 1
    else:
         d[A[i]] = 1

for i in range(N):
    t = 2**len(bin(A[i])[2::]) - A[i]
    if t in d:
        if t != A[i]:
            if d[t]>0 and d[A[i]]>0:
                ans2 += 1
                d[t] -= 1
                d[A[i]] -= 1
        else:
            if d[t] > 1:
                ans2 += 1
                d[t] -= 2


print(ans1+ans2)
