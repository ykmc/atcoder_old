A,B,C,D = map(int,input().split())
print(max(min(B,D)-max(A,C),0))