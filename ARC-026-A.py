N,A,B = map(int,input().split())

print(A*max(N-5,0) + B*min(N,5))