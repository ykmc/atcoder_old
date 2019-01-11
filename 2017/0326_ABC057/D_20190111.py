N,A,B = map(int,input().split())
V = list(map(int,input().split()))

V.sort(reverse=True)

sumV = 0
for i in range(A):
    sumV += V[i]
ans1 = sumV/A

# 
cntV0 = 0
for i in range(N):
    if V[i]==V[0]:
        cntV0 += 1
ans2 = 1
if cntV0 > A:
    ans2 = 0
    for i in range(A,min(cntV0,B)+1):
        tmp = 1
        c = cntV0
        r = i
        for j in range(r):
            tmp *= c-j
            tmp //= j+1
        ans2 += tmp
else:
    cntV1,cntV2 = 0,0
    for i in range(N):
        if V[i]==V[A-1]:
            cntV1 += 1
        elif V[i]>V[A-1]:
            cntV2 += 1
    if cntV1+cntV2 > A:
        c = cntV1
        r = A-cntV2
        for i in range(r):
            ans2 *= c-i
            ans2 //= i+1


print(ans1, ans2)