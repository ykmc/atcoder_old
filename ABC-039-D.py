import copy
H,W = map(int,input().split())
S = []
for i in range(H):
    l = input()
    S.append([l[i] for i in range(W)])

dx,dy = [-1,0,1],[-1,0,1]
T = [["#" for _ in range(W)] for _ in range(H)]
for hi in range(H):
    for wi in range(W):
        if S[hi][wi] == ".":
            for x in dx:
                for y in dy:
                    if 0 <= wi+x < W and 0 <= hi+y < H:
                        T[hi+y][wi+x] = "."

R = copy.deepcopy(T)
for hi in range(H):
    for wi in range(W):
        if T[hi][wi] == "#":
            for x in dx:
                for y in dy:
                    if 0 <= wi+x < W and 0 <= hi+y < H:
                        R[hi+y][wi+x] = "#"

if S==R:
    print("possible")
    for i in range(H):
        print("".join(T[i]))
else:
    print("impossible")