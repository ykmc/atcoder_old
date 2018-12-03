from collections import Counter
C = Counter(input())
R = "Yes"
for k,v in C.most_common():
    if v%2 == 1:
        R = "No"
        break
print(R)