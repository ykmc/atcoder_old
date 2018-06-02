O = input()
E = input()

post = ""
if len(O) != len(E):
    post = O[-1:]

Ans = ""
for i in range(len(E)):
    Ans += O[i]+E[i]

print(Ans+post)
