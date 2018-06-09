C = list(input() for i in range(4))
for i in range(4):
    print(C[3-i][::-1])