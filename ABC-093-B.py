A,B,K = map(int,input().split())
for i in range(min(K,B-A+1)):
    print(A+i)
for i in range(max(B-K+1,A+K),B+1):
    print(i)