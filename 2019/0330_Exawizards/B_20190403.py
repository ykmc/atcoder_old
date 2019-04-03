N = int(input())
S = input()

ans = 0
for s in S:
    if s=="R":
        ans += 1
    else:
        ans -= 1
print("Yes" if ans>0 else "No")