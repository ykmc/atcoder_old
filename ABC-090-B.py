A,B = map(int,input().split())
n=0
for i in range(A,B+1):
    if i == int(str(i)[::-1]):
        n+=1
print(n)