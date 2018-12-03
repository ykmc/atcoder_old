N = int(input())
Nbin = "{0:04b}".format(N)
x = 8
print(Nbin.count("1"))
for i in Nbin:
    if i=="1":
        print(x)
    x = x//2
