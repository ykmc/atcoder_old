N = int(input())
S = input()

i,s = 1,"b"
L = ["b"]
while len(s) <= 100:
    if i%3 == 1:
        s = "a" + s + "c"
    elif i%3 == 2:
        s = "c" + s + "a"
    else:
        s = "b" + s + "b"
    L.append(s)
    i += 1


if S in L:
    print(L.index(S))
else:
    print(-1)
