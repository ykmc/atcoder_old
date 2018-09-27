from itertools import product
S = input()
i,L = 0,len(S)
ops = list(product(" +", repeat=L-1))

T = 0
for op in ops:
    W = ""
    for i in range(L-1):
        W += S[i]+op[i]
    W += S[L-1]
    T += eval(W.replace(" ",""))
print(T)