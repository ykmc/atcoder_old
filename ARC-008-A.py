N = int(input())

a,b = N//10,N%10
print(100*a+15*b if b<=6 else 100*(a+1))