H,W = map(int,input().split())
A = []
for i in range(H):
    a = input()
    A.append(a)

ansW,ansH = [],[]
for hi in range(H):
    for wi in range(W):
        if A[hi][wi] == "#":
            break
    else:
        ansH.append(hi)
for wi in range(W):
    for hi in range(H):
        if A[hi][wi] == "#":
            break
    else:
        ansW.append(wi)

Ans = []
for hi in range(H):
    if hi not in ansH:
        ans = ""
        for wi in range(W):
            if wi not in ansW:
                ans += A[hi][wi]
        Ans.append(ans)

for ans in Ans:
    print(ans)

