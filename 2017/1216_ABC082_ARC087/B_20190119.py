S = input()
T = input()

SS = [s for s in S]
TT = [t for t in T]
SS.sort()
TT.sort(reverse=True)
S = "".join(SS)
T = "".join(TT)

print("Yes" if S<T else "No")