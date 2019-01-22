N = int(input())
print("{:02d}:{:02d}:{:02d}".format(N//3600, (N%3600)//60, N%60))