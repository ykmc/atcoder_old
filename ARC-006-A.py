E = set(input().split())
B = input()
L = set(input().split())

cnt = len(E&L)

Ans = 0
if cnt == 6:
    Ans = 1
elif cnt == 5:
    Ans = 2 if B in L else 3
elif cnt == 4:
    Ans = 4
elif cnt == 3:
    Ans = 5

print(Ans)