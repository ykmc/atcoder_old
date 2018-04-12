N,L = map(int,input().split())
A = []
for i in range(N):
    A.append(input())
print("".join(sorted(A)))