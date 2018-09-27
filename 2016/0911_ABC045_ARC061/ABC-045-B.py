S = {}
S["a"] = input()
S["b"] = input()
S["c"] = input()

p = "a"
while len(S[p]) > 0:
    x = S[p][0]
    S[p] = S[p][1:]
    p = x
print(p.upper())