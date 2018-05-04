A,B,C = map(int,input().split())
Ans = "NO"
for i in range(1,101):
    if (A*i)%B==C:
        Ans="YES"
        break
print(Ans)