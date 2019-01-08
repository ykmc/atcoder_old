X = int(input())
ans = (X//11)*2
if X%11==0:
    ans += 0
elif X%11<7:
    ans += 1
else:
    ans += 2

print(ans)