A = int(input())
Ans = 0
for i in range(1,A+1):
    Ans = max(Ans, i*(A-i))
print(Ans)