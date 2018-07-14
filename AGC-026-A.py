N = int(input())
A = list(map(int,input().split()))

Ans = 0
sub = 1
for i in range(N-1):
    if A[i]==A[i+1]:
        sub += 1
    else:
        Ans += sub//2
        sub = 1
else:
    Ans += sub//2

print(Ans)
