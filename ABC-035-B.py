from collections import Counter
S = input()
T = int(input())
C = Counter(S)
dx,dy = abs(C["L"]-C["R"]),abs(C["U"]-C["D"])
dq = C["?"]
if T==1: 
    print(dx+dy+dq)
else:
    d = dx+dy-dq
    if d > 0:
        print(d)
    else:
        if d%2 == 0:
            print(0)
        else:
            print(1)
        