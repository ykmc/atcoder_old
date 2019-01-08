N = int(input())
S = input()

ans,tmp = 0,0
for s in S:
    if s=="I":
        tmp += 1
    else:
        tmp -= 1
    ans = max(ans,tmp)

print(ans)