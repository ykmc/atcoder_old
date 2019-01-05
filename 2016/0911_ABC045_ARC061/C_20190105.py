from itertools import product
S = input()

ans = 0
ops = list(product("+ ", repeat=len(S)-1))
for op in ops:
    ans += eval((S[0]+"".join(x+y for (x,y) in zip(op,S[1::]))).replace(" ",""))

print(ans)