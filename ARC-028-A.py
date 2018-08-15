N,A,B = map(int,input().split())

r = N%(A+B)
print("Ant" if 0< r <= A else "Bug")