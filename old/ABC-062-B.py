H,W = map(int,input().split())
A = []
A.append("#"*(W+2))
for i in range(H):
    A.append("#"+input()+"#")
A.append("#"*(W+2))

for i in range(H+2):
    print(A[i])