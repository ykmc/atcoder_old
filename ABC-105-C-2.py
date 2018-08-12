N = int(input())

print(N%(-2),N//(-2))

Ans = ""
while N!=0:
    Ans = str(N%2) +Ans
    N = (N - N%2)//2
    N *= -1

print(Ans)