N = int(input())
A = list(map(int,input().split()))
Ans,t,prev = 0,0,0
for i in range(N):
    if A[i] > prev:
        t += 1
    else:
        t = 1
    prev = A[i]
    Ans += t
print(Ans)
