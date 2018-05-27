S = input()
A = S.split("+")
Ans = len([a for a in A if eval(a) != 0])
print(Ans)