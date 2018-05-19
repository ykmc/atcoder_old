N = int(input())
print("{0:02d}:{1:02d}:{2:02d}".format(N//3600,(N%3600)//60,N%60))