S = input()

ans,cnt = 0,0
for s in S:
    if s in "ACGT":
        cnt += 1
        ans = max(ans,cnt)
    else:
        cnt = 0
print(ans)
