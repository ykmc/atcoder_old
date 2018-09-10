N = int(input())

Ans = ""
while N!=0:
    Ans = str(N%2) +Ans
    N = (N - N%2)//2
    N *= -1

print(Ans if Ans!="" else 0)