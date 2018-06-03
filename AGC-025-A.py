N = int(input())
Ans = 0
while N >=1:
    Ans += N%10
    N //= 10
print(Ans if Ans != 1 else 10)
