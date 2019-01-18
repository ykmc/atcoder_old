# N が3桁固定なので、単純に連結するだけでもよい
# N = input()
# print("ABC"+N)

N = int(input())
print("ABC"+"{:03d}".format(N))
