A,B,C = map(int,input().split())
K = int(input())
m = max(A,B,C)
e = (A+B+C) - m
print(m*(2**K)+e)
