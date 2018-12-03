X,A,B = map(int,input().split())

if A>=B:
    print("delicious")
elif B-A <= X:
    print("safe")
else:
    print("dangerous")