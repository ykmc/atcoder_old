N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
Ans = 0
for i in range(N):
    total = 0
    for j in range(N):
        if i == j:
            total += A1[j]+A2[j]
        elif i > j:
            total += A1[j]
        else:
            total += A2[j]
    Ans = max(Ans,total)
print(Ans)