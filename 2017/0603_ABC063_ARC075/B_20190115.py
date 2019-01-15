from collections import Counter
S = input()
C = Counter(S).most_common()

ans = "yes"
for _k,v in C:
    if v>1:
        ans = "no"

print(ans)