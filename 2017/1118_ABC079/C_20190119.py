D = input()

ops = []
for i in range(1 << 3):
    op = ""
    xx = bin(i)[2::].zfill(3)
    for x in xx:
        if x=="0":
            op += "+"
        else:
            op += "-"
    ops.append(op)

for op in ops:
    res = D[0]
    for i in range(3):
        res += op[i]+D[i+1]
    if eval(res)==7:
        print(res + "=7")
        break
