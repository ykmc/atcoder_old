A,B = map(int,input().split())

Ans = "No"
for c in range(1,4):
    if (A*B*c)%2 == 1:
        Ans = "Yes"

print(Ans)