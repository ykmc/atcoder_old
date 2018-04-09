N = int(input())
D,X = map(int,input().split())
A,num = [],0
for i in range(N):
    A.append(int(input()))
for i in range(N):
    num = num + (D-1)//A[i] + 1
print(num+X)