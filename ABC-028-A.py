N = int(input())
Ans = ""
if N <= 59:
    Ans = "Bad"
elif N <= 89:
    Ans = "Good"
elif N <= 99:
    Ans = "Great"
elif N == 100:
    Ans = "Perfect"

print(Ans)
