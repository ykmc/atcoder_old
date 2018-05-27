S = input()
A = S.split("+")
Ans = len([a for a in A if a.count("0") == 0])
print(Ans)