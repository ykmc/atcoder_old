S = input()

L = len(S)
if S[0]=="0" or S[-1]=="1":
    print(-1)
    exit()
for i in range(L-2):
    if S[i] != S[L-2-i]:
        print(-1)
        exit()

pv = 1
for i in range(L-1):
    nv = i+2
    # 現頂点から次の頂点へ、長さを確保
    if S[i]=="1":
        print(pv,nv)
        pv = nv
    # 現頂点への葉とする
    else:
        print(pv,nv)

