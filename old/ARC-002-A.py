Y = int(input())

Ans = "NO"
if Y%4==0:
    Ans = "YES"
if Y%100==0:
    Ans = "NO"
if Y%400==0:
    Ans = "YES"

print(Ans)