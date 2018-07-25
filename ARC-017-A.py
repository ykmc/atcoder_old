N = int(input())

root = N**.5
i = 2
Ans = "YES"
while i <= root:
    if N%i==0:
        Ans = "NO"
        break
    i += 1

print(Ans)