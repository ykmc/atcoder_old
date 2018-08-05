N = int(input())

Ans = ""
if N < 1200:
    Ans = "ABC"
elif N < 2800:
    Ans = "ARC"
else:
    Ans = "AGC"

print(Ans) 