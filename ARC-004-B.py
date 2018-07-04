N = int(input())
D = []
for i in range(N):
    D.append(int(input()))

sumD = sum(D)
maxD = max(D)
minD = 0
if N == 1:
    minD = D[0]
else:
    minD = maxD*2-sumD if maxD > sumD-maxD else 0

print(sumD)
print(minD)