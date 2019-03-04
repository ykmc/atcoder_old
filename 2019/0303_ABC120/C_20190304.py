S = input()
cnt0,cnt1 = 0,0
for s in S:
    if s=="0":
        cnt0 += 1
    else:
        cnt1 += 1
print(min(cnt0,cnt1)*2)