N = int(input())
S = input()

S1,S2 = S[:N],S[N:][::-1]

from itertools import product
B = list(product([0,1], repeat=N))

D1 = {}
Ans = 0

for bb in B:
    red,blue = "",""
    cnt = 0
    for i,b in enumerate(bb):
        if b == 0:
            red += S1[i]
            cnt += 1
        else:
            blue += S1[i]
    key = (cnt,red+blue[::-1])
    if key not in D1.keys():
        D1[key] = 1
    else:
        D1[key] += 1

for bb in B:
    red,blue = "",""
    cnt = 0
    for i,b in enumerate(bb):
        if b == 1:
            red += S2[i]
            cnt += 1
        else:
            blue += S2[i]
    key = (cnt,red+blue[::-1])
    if key in D1.keys():
        Ans += D1[key]

print(Ans)